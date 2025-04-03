const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');
const util = require('util');
const execPromise = util.promisify(exec);

exports.renderManimScenes = async (req, res) => {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const outputDir = path.join(__dirname, '../media/animations');

    // Creăm directorul pentru output dacă nu există
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    const files = fs.readdirSync(scenesDir).filter(file => file.endsWith('.py'));
    const renderResults = [];

    for (const file of files) {
      const sceneName = path.basename(file, '.py');
      const inputPath = path.join(scenesDir, file);
      
      try {
        console.log(`🎬 Randare pentru scena: ${sceneName}`);
        
        // Modificăm comanda pentru a specifica output-ul
        const command = `manim -qm -o "${outputDir}" "${inputPath}"`;
        const { stdout, stderr } = await execPromise(command);
        console.log('Manim output:', stdout);
        
        const expectedOutput = path.join(outputDir, `${sceneName}.mp4`);
        if (fs.existsSync(expectedOutput)) {
          renderResults.push({
            scene: sceneName,
            status: 'success',
            path: `/media/animations/${sceneName}.mp4`
          });
        } else {
          throw new Error('Fișierul MP4 nu a fost generat');
        }
      } catch (error) {
        console.error(`❌ Eroare la randarea scenei ${sceneName}:`, error);
        renderResults.push({
          scene: sceneName,
          status: 'error',
          error: error.message
        });
      }
    }

    res.json({
      message: 'Procesul de randare s-a încheiat',
      results: renderResults
    });

  } catch (error) {
    console.error('❌ Eroare la randarea animațiilor:', error);
    res.status(500).json({ 
      message: 'Eroare la randarea animațiilor', 
      error: error.message 
    });
  }
}; 