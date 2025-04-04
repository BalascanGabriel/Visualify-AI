const { sendToGemini } = require('../services/geminiService');
const { generateManimScenes } = require('./mediaGenerator/manimAgent');
const fs = require('fs');
const path = require('path');

async function generateConceptAnimations(structura) {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const mediaDir = path.join(__dirname, '../media/animations');
    
    fs.mkdirSync(scenesDir, { recursive: true });
    fs.mkdirSync(mediaDir, { recursive: true });

    console.log('📚 Structura primită:', JSON.stringify(structura, null, 2));

    // Extragem conceptele în ordinea din structură
    const toateConceptele = [];
    
    // Parcurgem structura în ordine
    for (const capitol of structura) {
      console.log(`📑 Procesare capitol: ${capitol.capitol}`);
      
      if (!capitol.subcapitole || !Array.isArray(capitol.subcapitole)) {
        console.error('❌ Capitol invalid:', capitol);
        continue;
      }

      for (const subcapitol of capitol.subcapitole) {
        console.log(`  📖 Subcapitol: ${subcapitol.subcapitol}`);
        
        if (!subcapitol.concepte || !Array.isArray(subcapitol.concepte)) {
          console.error('❌ Subcapitol invalid:', subcapitol);
          continue;
        }

        const concepteValide = subcapitol.concepte
          .filter(concept => 
            concept && 
            typeof concept === 'string' &&
            concept.length > 10 &&
            !concept.toLowerCase().includes('exerciții') &&
            !concept.toLowerCase().includes('aplicarea')
          );
        
        console.log(`    ✨ Concepte găsite: ${concepteValide.length}`);
        console.log('    📝 Concepte:', concepteValide);
        
        // Adăugăm metadata pentru a ține evidența contextului
        const concepteCuContext = concepteValide.map(concept => ({
          text: concept,
          capitol: capitol.capitol,
          subcapitol: subcapitol.subcapitol
        }));
        
        toateConceptele.push(...concepteCuContext);
      }
    }

    console.log(`🔍 Total concepte găsite: ${toateConceptele.length}`);
    if (toateConceptele.length === 0) {
      throw new Error('Nu s-au găsit concepte valide pentru generare');
    }

    console.log('📝 Concepte:', JSON.stringify(toateConceptele, null, 2));
    
    // Generăm scenele Manim cu contextul complet
    const scenes = await generateManimScenes(toateConceptele);
    
    // Verificăm dacă s-au generat scene
    if (!scenes || scenes.length === 0) {
      throw new Error('Nu s-au generat scene Manim');
    }
    
    console.log('🎬 Scene generate:', scenes.length);

    return scenes;
  } catch (error) {
    console.error('❌ Eroare la generarea animațiilor:', error);
    throw error;
  }
}

module.exports = { generateConceptAnimations };
