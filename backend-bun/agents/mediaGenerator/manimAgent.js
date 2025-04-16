const fs = require('fs');
const path = require('path');
const { sendToGemini } = require('../../services/geminiService');

const TEMPLATE = (sceneName, geminiCode) => {
  return `from manim import *

class ${sceneName}(Scene):
    def construct(self):
${geminiCode}`;
};

const slugify = (text) => {
  if (typeof text !== 'string') {
    text = text.text || String(text);
  }
  return text
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]/g, '_')
    .replace(/_+/g, '_')
    .toLowerCase()
    .slice(0, 50);
};

const getPromptForConcept = (conceptText) => {
  return `You are a world-class educational animator working on the Visualify AI platform.

Generate a deeply explanatory, cinematic, and visually mind-blowing Manim (Python) animation that clearly teaches the following concept:

"${conceptText}"

Educational Goals:
- Explain step-by-step with progressive visual logic
- Use animated metaphors, geometry, and interactive transitions
- Fit in a 20–30 second window (not shorter, not longer)
- Designed for high-school or university-level students

Scene Setup:
- Frame size: 854x480 (16:9)
- Split layout:
  • Top 20% → Title (bold, clear)
  • Middle 60% → Visual explanation
  • Bottom 20% → Summary or final insight

Visual & Style Guidelines:
- Text in English only
- Title: Text(..., font_size=48, color=BLUE)
- Explanation text: Text(..., font_size=32, color=WHITE) with .scale_to_fit_width(...)
- Summary: Text(..., font_size=36, color=GREEN)

Text Rules:
- If a text is too long, split it on multiple lines using \\n
- Never allow any text to go outside the frame
- When a new explanation starts, remove previous texts using FadeOut(...)
- Avoid overlapping any visual elements
- Animate captions using Write(...), FadeIn(...), Transform(...)

Animation & Flow:
1. Show the title (fade in)
2. Introduce the concept gradually (start simple, then build complexity)
3. Use visuals like:
   - Arrows, graphs, number lines, vectors, parametric curves
   - Geometry (triangles, angles, coordinate systems)
   - Dynamic transformations and camera movement
4. Use advanced effects where fitting:
   - Rotate, GrowArrow, Create, SurroundingRectangle, 3D effects
   - VGroup(...).arrange(...) for layout organization
5. End with a concise summary or insight

Restrictions:
- Return only valid, properly indented Python Manim code
- Use Manim Community Edition (Python 3.10+)
- No external assets (images, logos, internet links)
- Use Tex(...) only for LaTeX formulas and wrap only real math in $...$
- Do not use $$, markdown, or comments
- Do not include any Romanian text

The animation should look like it belongs in a 3Blue1Brown or Kurzgesagt video: elegant, clear, detailed, well-organized, and powerful.`;
};


const cleanPythonCode = (code) => {
  try {
    if (typeof code === 'object') {
      code = code.raw || code.text || JSON.stringify(code);
    }
    code = String(code);
    
    // Extragem codul dintre ```python și ```
    const match = code.match(/```python\s*([\s\S]*?)\s*```/);
    if (match) {
      code = match[1];
    }

    // Eliminăm diacriticele și caracterele speciale din text
    code = code.replace(/Text\("([^"]+)"/g, (match, text) => {
      return `Text("${text
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/[^\x00-\x7F]/g, '')}"`;
    });

    // Eliminăm def construct duplicat dacă există
    code = code.replace(/def construct\(self\):\s*/g, '');

    // Curățăm și indentăm codul corect
    const cleanedCode = code
      .split('\n')
      .map(line => line.trim()) // Eliminăm spațiile existente
      .filter(line => {
        return line && 
          !line.startsWith('from') && 
          !line.startsWith('class') &&
          !line.startsWith('def');
      })
      .map(line => ' '.repeat(8) + line) // Exact 8 spații pentru indentare
      .join('\n');

    // Verificăm dacă avem elementele necesare
    if (!cleanedCode.includes('title =') || 
        !cleanedCode.includes('self.play(') || 
        !cleanedCode.includes('self.wait')) {
      throw new Error('Cod invalid - lipsesc elemente esențiale');
    }

    return cleanedCode;
  } catch (error) {
    console.error('❌ Eroare la curățarea codului:', error);
    // Template de backup fără diacritice și cu indentare corectă
    return `        title = Text("${conceptText
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')}", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)`;
  }
};

const generateManimScenes = async (concepts = []) => {
  try {
    console.log(`🎬 Începe generarea pentru ${concepts.length} concepte...`);
    
    const outputDir = path.join(__dirname, '../../scripts/animator/generated_scenes');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const sceneOrder = [];
    const generatedFiles = [];

    for (const [index, concept] of concepts.entries()) {
      const sceneNumber = String(index + 1).padStart(2, '0');
      const conceptText = concept.text || concept;
      const sceneName = `Scene${sceneNumber}_${slugify(conceptText)}`;
      
      console.log(`\n🎯 Generare scenă ${sceneNumber}: ${conceptText}`);
      
      try {
        const prompt = getPromptForConcept(conceptText);
        const geminiResponse = await sendToGemini(prompt);
        const pythonCode = TEMPLATE(sceneName, cleanPythonCode(geminiResponse));
        
        const outputFile = path.join(outputDir, `${sceneName}.py`);
        fs.writeFileSync(outputFile, pythonCode);
        
        generatedFiles.push(outputFile);
        sceneOrder.push({
          sceneName,
          concept: conceptText,
          filePath: outputFile
        });
        
        console.log(`✅ Script generat: ${sceneName}.py`);
      } catch (error) {
        console.error(`❌ Eroare la scena ${sceneNumber}:`, error.message);
        // Continuăm cu următoarea scenă
      }
    }

    // Salvăm ordinea scenelor
    fs.writeFileSync(
      path.join(outputDir, 'scene_order.json'),
      JSON.stringify(sceneOrder, null, 2)
    );

    return sceneOrder;
  } catch (error) {
    console.error('❌ Eroare generală:', error);
    throw error;
  }
};

module.exports = {
  generateManimScenes,
  cleanPythonCode,
  getPromptForConcept,
  slugify
};