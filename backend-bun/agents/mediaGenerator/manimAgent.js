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
  return `Generează cod Python Manim pentru conceptul: "${conceptText}".
Folosește acest format pentru a asigura că totul se încadrează în ecran (854x480):

        # Setăm dimensiunea scenei și calculăm proporțiile
        FRAME_WIDTH = config.frame_width
        FRAME_HEIGHT = config.frame_height
        
        # Împărțim scena în zone pentru organizare mai bună
        TOP_SECTION = FRAME_HEIGHT * 0.2      # 20% pentru titlu
        MIDDLE_SECTION = FRAME_HEIGHT * 0.6   # 60% pentru demonstrație
        BOTTOM_SECTION = FRAME_HEIGHT * 0.2   # 20% pentru text explicativ
        
        # Titlu - scalat automat să încapă pe un rând
        title = Text(
            "${conceptText}",
            font_size=36,
            color=BLUE
        )
        title.scale_to_fit_width(FRAME_WIDTH * 0.9)  # Folosim 90% din lățime
        title.to_edge(UP, buff=0.5)
        
        # Explicație inițială - scalată proporțional
        explanation = Text(
            "Prima parte a explicației",
            font_size=28,
            color=WHITE
        )
        explanation.scale_to_fit_width(FRAME_WIDTH * 0.8)  # Folosim 80% din lățime
        explanation.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # Demonstrație - centrată și scalată în secțiunea din mijloc
        demo_container = Rectangle(
            width=FRAME_WIDTH * 0.8,
            height=MIDDLE_SECTION * 0.8,
            stroke_opacity=0
        ).move_to(ORIGIN)
        
        demo = VGroup(
            Circle(radius=2, color=BLUE),
            Arrow(LEFT*2, RIGHT*2, color=WHITE)
        ).arrange(RIGHT, buff=1)
        
        # Scalăm demonstrația să se încadreze în container
        demo.move_to(demo_container.get_center())
        scale_factor = min(
            demo_container.width / demo.width,
            demo_container.height / demo.height
        ) * 0.9
        demo.scale(scale_factor)
        
        self.play(Create(demo))
        self.wait(2)
        self.play(FadeOut(demo))
        
        # Concluzie - scalată și poziționată în partea de jos
        conclusion = Text(
            "Concluzie finală",
            font_size=28,
            color=GREEN
        )
        conclusion.scale_to_fit_width(FRAME_WIDTH * 0.8)
        conclusion.next_to(title, DOWN, buff=0.8)
        
        self.play(FadeIn(conclusion))
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(conclusion)
        )
        self.wait()

IMPORTANT:
- Împarte scena în secțiuni proporționale (20-60-20)
- Scalează textele relativ la lățimea frame-ului (90% titlu, 80% text)
- Centrează și scalează demonstrațiile în containerul lor
- Menține spațiere consistentă între elemente
- Asigură-te că nimic nu iese din frame

Returnează DOAR codul Python, fără explicații sau comentarii extra.`;
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