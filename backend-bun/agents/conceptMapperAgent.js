const { sendToGemini } = require('../services/geminiService');
const { generateManimScenes } = require('./mediaGenerator/manimAgent');
const fs = require('fs');
const path = require('path');

async function generateConceptAnimations(structura) {
  try {
    // Creăm directoarele necesare dacă nu există
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const mediaDir = path.join(__dirname, '../media/animations');
    
    fs.mkdirSync(scenesDir, { recursive: true });
    fs.mkdirSync(mediaDir, { recursive: true });

    // Extragem toate conceptele din structură
    const toateConceptele = structura.reduce((acc, capitol) => {
      capitol.subcapitole.forEach(subcapitol => {
        acc.push(...subcapitol.concepte);
      });
      return acc;
    }, []);

    // Generăm scenele Manim pentru concepte
    await generateManimScenes(toateConceptele);

    return true;
  } catch (error) {
    console.error('❌ Eroare la generarea animațiilor:', error);
    return false;
  }
}

module.exports = { generateConceptAnimations };
