const fs = require('fs');
const path = require('path');
const { sendToGemini } = require('../../services/geminiService');

const TEMPLATE = (sceneName, geminiCode) => `from manim import *

class ${sceneName}(Scene):
    def construct(self):
${geminiCode.split('\n').map(line => '        ' + line).join('\n')}
`;

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
  // Verificăm dacă avem un obiect în loc de string
  if (typeof code === 'object' && code.raw) {
    code = code.raw;
  }

  // Ne asigurăm că avem un string
  code = String(code);

  // Extragem codul dintre marcajele ```python și ```
  const match = code.match(/```python\n?([\s\S]*?)\n?```/);
  if (match) {
    code = match[1];
  }

  return code
    .replace(/```python\n?/g, '')
    .replace(/```\n?/g, '')
    .replace(/°/g, 'degree')
    .trim();
};

const getPromptForConcept = (conceptText) => {
  return `Generează cod Python Manim pentru a explica conceptul: "${conceptText}".
Răspunde DOAR cu un bloc de cod Python între marcaje \`\`\`python și \`\`\`.

Folosește acest format pentru animații:

1. LAYOUT:
   - Titlul sus (to_edge(UP))
   - Textul explicativ în stânga sau dreapta
   - Animațiile în centru
   - Formulele sub animații

2. CULORI ȘI STIL:
   - Folosește culori diferite pentru evidențiere (BLUE, RED, YELLOW, GREEN)
   - Text alb pe fundal închis pentru contrast

3. ANIMAȚII:
   - FadeIn/FadeOut pentru tranziții line
   - Transform pentru modificări elegante
   - Create pentru desene progresive

4. POZIȚIONARE:
   - arrange_submobjects pentru aliniere
   - next_to pentru poziționare relativă
   - shift pentru ajustări fine

Exemplu de răspuns așteptat:

\`\`\`python
# Titlu
title = Text("${conceptText}", color=BLUE)
title.to_edge(UP)
self.play(Write(title))

# Text explicativ în stânga
explanation = Text("Explicație", color=WHITE)
explanation.to_edge(LEFT)
self.play(FadeIn(explanation))

# Animație principală în centru
main_animation = Circle(color=YELLOW)
main_animation.move_to(ORIGIN)
self.play(Create(main_animation))

# Formulă sub animație
formula = MathTex("f(x)", color=WHITE)
formula.next_to(main_animation, DOWN)
self.play(Write(formula))
\`\`\``;
};

exports.generateManimScenes = async (concepts = []) => {
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
        
        const geminiResponse = await sendToGemini(prompt);
        const cleanCode = cleanPythonCode(geminiResponse);
        
        const pythonCode = TEMPLATE(sceneName, cleanCode);
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