const fs = require('fs');
const path = require('path');
const { sendToGemini } = require('../../services/geminiService');

const TEMPLATE = (sceneName, geminiCode) => {
  // Curățăm codul primit de la Gemini
  const cleanedCode = geminiCode
    .split('\n')
    .map(line => line.trim()) // Eliminăm spațiile de la început și sfârșit
    .filter(line => line) // Eliminăm liniile goale
    .join('\n');

  return `from manim import *

config.tex_template.add_to_preamble(r"""
\\usepackage{amsmath}
\\usepackage{amssymb}
""")

class ${sceneName}(Scene):
    def construct(self):
${cleanedCode.split('\n').map(line => '        ' + line).join('\n')}
`;
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

const cleanPythonCode = (code) => {
  // Verificăm dacă avem răspuns de la Gemini în format obiect
  if (typeof code === 'object') {
    if (code.raw) {
      code = code.raw;
    } else if (code.text) {
      code = code.text;
    }
  }
  
  // Ne asigurăm că avem un string
  code = String(code);

  // Extragem codul Python dintre marcaje ```python
  const pythonMatch = code.match(/```python\n?([\s\S]*?)\n?```/);
  if (pythonMatch) {
    return pythonMatch[1].trim();
  }

  // Dacă nu găsim marcaje, returnăm codul așa cum e
  return code.trim();
};

const getPromptForConcept = (conceptText) => {
  return `Generează cod Python Manim pentru a explica conceptul: "${conceptText}".
Folosește MathTex pentru formule matematice și Text pentru text normal.

Exemplu format corect:
# Titlu
title = Text("${conceptText}", color=BLUE_A)
title.scale(1.2).to_edge(UP)
self.play(Write(title))

# Explicație
explanation = Text("Explicație simplă", color=WHITE)
explanation.next_to(title, DOWN)
self.play(FadeIn(explanation))

# Formule matematice (folosește MathTex, nu Tex)
formula = MathTex(r"\\sin(\\theta) = \\frac{a}{c}")
formula.next_to(explanation, DOWN)
self.play(Write(formula))

# Demonstrație
circle = Circle(color=YELLOW)
self.play(Create(circle))

# Final
self.wait()
self.play(
    FadeOut(title),
    FadeOut(explanation),
    FadeOut(formula),
    FadeOut(circle)
)

IMPORTANT:
1. Folosește MathTex pentru ORICE formulă matematică
2. Folosește Text pentru text normal
3. Pune întotdeauna r"" pentru stringurile LaTeX
4. Include \\ înainte de simbolurile LaTeX (\\sin, \\cos, \\tan, etc.)

Returnează DOAR codul Python pentru interiorul metodei construct(), fără alte elemente.`;
};

const generateManimScenes = async (concepts = []) => {
  try {
    console.log(`🎬 Începe generarea pentru ${concepts.length} concepte...`);
    
    const outputDir = path.join(__dirname, '../../scripts/animator/generated_scenes');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    console.log('📁 Director output:', outputDir);

    const sceneOrder = [];
    const generatedFiles = [];

    for (const [index, concept] of concepts.entries()) {
      try {
        const sceneNumber = String(index + 1).padStart(2, '0');
        const conceptText = concept.text || concept;
        const sceneName = `Scene${sceneNumber}_${slugify(conceptText)}`;
        console.log(`\n🎯 Generare scenă ${sceneNumber}: ${conceptText}`);

        const prompt = getPromptForConcept(conceptText);
        console.log('📝 Trimitere prompt către Gemini...');
        
        let attempts = 0;
        let pythonCode;
        
        while (attempts < 3) {
          try {
            const geminiResponse = await sendToGemini(prompt);
            const cleanCode = cleanPythonCode(geminiResponse);
            
            // Verificăm dacă avem cod Python valid
            if (cleanCode && cleanCode.includes('title =') && !cleanCode.includes('[object Object]')) {
              pythonCode = TEMPLATE(sceneName, cleanCode);
              break;
            }
            throw new Error('Cod Python invalid');
          } catch (error) {
            attempts++;
            console.log(`⚠️ Încercare ${attempts}/3 eșuată:`, error.message);
            await new Promise(resolve => setTimeout(resolve, 1000));
          }
        }

        if (!pythonCode) {
          throw new Error('Nu s-a putut genera cod Python valid după 3 încercări');
        }

        const outputFile = path.join(outputDir, `${sceneName}.py`);
        fs.writeFileSync(outputFile, pythonCode);
        console.log(`✅ Script generat: ${outputFile}`);
        
        generatedFiles.push(outputFile);
        sceneOrder.push({
          sceneName,
          concept: conceptText,
          filePath: outputFile,
          context: {
            capitol: concept.capitol,
            subcapitol: concept.subcapitol
          }
        });

      } catch (error) {
        console.error(`❌ Eroare la generarea scenei ${index + 1}:`, error);
      }
    }

    // Salvăm ordinea scenelor
    fs.writeFileSync(
      path.join(outputDir, 'scene_order.json'),
      JSON.stringify(sceneOrder, null, 2)
    );

    console.log('\n✨ Generare completă:');
    console.log('- Scene generate:', sceneOrder.length);
    console.log('- Fișiere Python:', generatedFiles.length);
    console.log('- Fișiere generate:', generatedFiles);

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