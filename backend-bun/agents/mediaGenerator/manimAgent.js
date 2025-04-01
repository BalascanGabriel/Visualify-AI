const fs = require('fs');
const path = require('path');
const { sendToGemini } = require('../../services/geminiService');

const TEMPLATE = (sceneName, geminiCode) => `
from manim import *

class ${sceneName}(Scene):
    def construct(self):
${geminiCode.split('\n').map(line => '        ' + line).join('\n')}
`;

const slugify = (text) => {
  return text
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]/g, '_')
    .replace(/_+/g, '_')
    .toLowerCase()
    .slice(0, 50);
};

exports.generateManimScenes = async (concepts = []) => {
  const outputDir = path.join(__dirname, '../../scripts/animator/generated_scenes');
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

  let idx = 1;
  for (const concept of concepts) {
    const sceneName = `Scene${idx}_${slugify(concept)}`;
    const prompt = `Scrie un cod Manim pentru a explica conceptul tehnic: "${concept}". 
Fii animat, educativ și folosește explicații vizuale. Doar cod Python Manim în răspuns.`;

    try {
      const result = await sendToGemini(prompt);
      const code = result.raw || result;

      const fullScript = TEMPLATE(sceneName, code);
      const filePath = path.join(outputDir, `${sceneName}.py`);

      fs.writeFileSync(filePath, fullScript, 'utf-8');
      console.log(`✅ Generat: ${filePath}`);
    } catch (err) {
      console.error(`❌ Eroare pentru conceptul "${concept}":`, err.message);
    }

    idx++;
  }
};
