const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');
const util = require('util');
const execPromise = util.promisify(exec);

const slugify = (text) => {
  return text
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-zA-Z0-9]/g, '_')
    .replace(/_+/g, '_')
    .toLowerCase()
    .slice(0, 50);
};

const reconstructSceneOrder = async () => {
  const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
  
  // Încercăm să citim structura originală din fișierul generat de /api/generate
  const structurePath = path.join(__dirname, '../temp/last_structure.json');
  let orderedConcepts = [];

  if (fs.existsSync(structurePath)) {
    try {
      const structure = JSON.parse(fs.readFileSync(structurePath, 'utf8'));
      // Extragem conceptele în ordinea din structură
      structure.structura.forEach(capitol => {
        capitol.subcapitole.forEach(subcapitol => {
          orderedConcepts.push(...subcapitol.concepte);
        });
      });
    } catch (error) {
      console.warn('⚠️ Nu s-a putut citi structura originală, folosim ordinea alfabetică');
    }
  }

  const files = fs.readdirSync(scenesDir).filter(file => file.endsWith('.py'));
  let sceneOrder;

  if (orderedConcepts.length > 0) {
    // Construim ordinea bazată pe structura originală
    sceneOrder = orderedConcepts.map((concept, idx) => {
      const sceneName = `Scene${String(idx + 1).padStart(2, '0')}_${slugify(concept)}`;
      const filePath = path.join(scenesDir, `${sceneName}.py`);
      
      return {
        sceneName,
        concept,
        filePath,
        order: idx + 1
      };
    }).filter(scene => fs.existsSync(scene.filePath)); // Păstrăm doar scenele care există
  } else {
    // Fallback la ordinea numerică din nume
    sceneOrder = files.sort().map((file, idx) => {
      const sceneName = path.basename(file, '.py');
      const concept = sceneName.split('_').slice(1).join('_');
      
      return {
        sceneName,
        concept,
        filePath: path.join(scenesDir, file),
        order: idx + 1
      };
    });
  }

  // Salvăm ordinea reconstruită
  fs.writeFileSync(
    path.join(scenesDir, 'scene_order.json'),
    JSON.stringify(sceneOrder, null, 2)
  );

  return sceneOrder;
};

exports.renderManimScenes = async (req, res) => {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const sceneFiles = fs.readdirSync(scenesDir).filter(file => file.endsWith('.py'));
    console.log('🐍 Scripturi Python găsite:', sceneFiles);

    const renderResults = [];

    for (const sceneFile of sceneFiles) {
      const sceneName = path.basename(sceneFile, '.py');
      console.log(`🎬 Randare pentru scena: ${sceneName}`);
      
      try {
        const command = `manim -ql --format=mp4 "${path.join(scenesDir, sceneFile)}" ${sceneName}`;
        console.log('🚀 Rulare comandă:', command);
        
        const { stdout } = await execPromise(command);
        console.log('📺 Output Manim:', stdout);

        // Calea corectă către fișierul generat
        const sourceVideoPath = path.join(__dirname, '../media/videos', sceneName, '480p15', `${sceneName}.mp4`);
        
        if (fs.existsSync(sourceVideoPath)) {
          // Copiem în directorul animations
          const animationDir = path.join(__dirname, '../media/animations');
          if (!fs.existsSync(animationDir)) {
            fs.mkdirSync(animationDir, { recursive: true });
          }
          
          const finalPath = path.join(animationDir, `${sceneName}.mp4`);
          fs.copyFileSync(sourceVideoPath, finalPath);

          renderResults.push({
            scene: sceneName,
            status: 'success',
            path: `/media/animations/${sceneName}.mp4`
          });
          
          console.log(`✅ Video generat și copiat: ${finalPath}`);
        } else {
          throw new Error(`Video-ul nu a fost generat la: ${sourceVideoPath}`);
        }

      } catch (error) {
        console.error(`❌ Eroare la randarea scenei ${sceneName}:`, error);
        renderResults.push({
          scene: sceneName,
          status: 'error',
          error: error.message
        });
        // Continuăm cu următoarea scenă chiar dacă aceasta a eșuat
      }

      // Pauză mică între scene pentru a evita supraîncărcarea
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    res.json({
      message: 'Randare completă',
      results: renderResults
    });

  } catch (error) {
    console.error('❌ Eroare la randare:', error);
    res.status(500).json({
      message: 'Eroare la randare',
      error: error.message
    });
  }
};

exports.combineVideos = async (req, res) => {
  try {
    const animationsDir = path.join(__dirname, '../media/animations');
    const coursesDir = path.join(__dirname, '../media/courses');
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');

    // Creăm directoarele dacă nu există
    if (!fs.existsSync(animationsDir)) {
      fs.mkdirSync(animationsDir, { recursive: true });
    }
    if (!fs.existsSync(coursesDir)) {
      fs.mkdirSync(coursesDir, { recursive: true });
    }

    // Verificăm dacă avem fișiere MP4
    const mp4Files = fs.readdirSync(animationsDir)
      .filter(file => file.endsWith('.mp4'));

    console.log('📁 Fișiere MP4 găsite:', mp4Files);

    if (mp4Files.length === 0) {
      return res.status(400).json({
        message: 'Nu s-au găsit videoclipuri pentru combinat. Rulați mai întâi /api/render/manim',
        error: 'NO_VIDEOS_FOUND'
      });
    }

    // Citim ordinea scenelor
    const orderFile = path.join(scenesDir, 'scene_order.json');
    if (!fs.existsSync(orderFile)) {
      return res.status(400).json({
        message: 'Nu s-a găsit fișierul de ordine a scenelor',
        error: 'NO_SCENE_ORDER'
      });
    }

    const sceneOrder = JSON.parse(fs.readFileSync(orderFile, 'utf8'));
    console.log('📝 Ordine scene:', sceneOrder);

    // Creăm fișierul de input pentru ffmpeg
    const inputListPath = path.join(coursesDir, 'input_list.txt');
    const videoList = sceneOrder
      .map(scene => {
        const videoPath = path.join(animationsDir, `${scene.sceneName}.mp4`);
        if (fs.existsSync(videoPath)) {
          return `file '${videoPath}'`;
        }
        return null;
      })
      .filter(Boolean);

    if (videoList.length === 0) {
      return res.status(400).json({
        message: 'Nu s-au găsit videoclipuri pentru combinat. Rulați mai întâi /api/render/manim',
        error: 'NO_VIDEOS_FOUND'
      });
    }

    fs.writeFileSync(inputListPath, videoList.join('\n'));

    // Generăm numele cursului
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const outputPath = path.join(coursesDir, `curs_${timestamp}.mp4`);

    // Combinăm videoclipurile
    const command = `ffmpeg -f concat -safe 0 -i "${inputListPath}" -c copy "${outputPath}"`;
    await execPromise(command);

    // Ștergem fișierul temporar
    fs.unlinkSync(inputListPath);

    res.json({
      message: 'Videoclipurile au fost combinate cu succes',
      outputPath: `/media/courses/curs_${timestamp}.mp4`
    });

  } catch (error) {
    console.error('❌ Eroare la combinarea videoclipurilor:', error);
    res.status(500).json({
      message: 'Eroare la combinarea videoclipurilor',
      error: error.message
    });
  }
};

// Endpoint pentru a vedea statusul și lista scenelor
exports.getStatus = async (req, res) => {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const animationsDir = path.join(__dirname, '../media/animations');
    const coursesDir = path.join(__dirname, '../media/courses');
    const orderFile = path.join(scenesDir, 'scene_order.json');

    console.log('📁 Verificare directoare și fișiere:');
    console.log('- scenesDir:', fs.existsSync(scenesDir));
    console.log('- animationsDir:', fs.existsSync(animationsDir));
    console.log('- coursesDir:', fs.existsSync(coursesDir));
    console.log('- scene_order.json:', fs.existsSync(orderFile));

    // Citim scene_order.json
    let sceneOrder = [];
    if (fs.existsSync(orderFile)) {
      sceneOrder = JSON.parse(fs.readFileSync(orderFile, 'utf8'));
      console.log('📝 Scene în ordine:', sceneOrder.length);
    }

    // Verificăm scripturile Python
    const pythonFiles = fs.existsSync(scenesDir) 
      ? fs.readdirSync(scenesDir)
          .filter(f => f.endsWith('.py'))
      : [];
    console.log('🐍 Scripturi Python:', pythonFiles);

    // Verificăm animațiile randate
    const renderedAnimations = fs.existsSync(animationsDir)
      ? fs.readdirSync(animationsDir)
          .filter(f => f.endsWith('.mp4'))
      : [];
    console.log('🎬 Animații randate:', renderedAnimations);

    // Verificăm cursurile
    const finalCourses = fs.existsSync(coursesDir)
      ? fs.readdirSync(coursesDir)
          .filter(f => f.endsWith('.mp4'))
      : [];

    // Calculăm progresul
    const totalScenes = sceneOrder.length;
    const renderedScenes = renderedAnimations.length;
    const renderProgress = totalScenes > 0 
      ? Math.round((renderedScenes / totalScenes) * 100) 
      : 0;

    res.json({
      status: {
        hasStructure: sceneOrder.length > 0,
        totalScenes,
        renderedScenes,
        renderProgress: `${renderProgress}%`,
        hasFinalCourse: finalCourses.length > 0
      },
      scenes: sceneOrder.map(scene => ({
        name: scene.sceneName,
        concept: scene.concept,
        filePath: scene.filePath,
        isRendered: renderedAnimations.includes(`${scene.sceneName}.mp4`),
        context: scene.context
      })),
      latestCourse: finalCourses.length > 0 
        ? `/media/courses/${finalCourses[finalCourses.length - 1]}`
        : null
    });

  } catch (error) {
    console.error('❌ Eroare la obținerea statusului:', error);
    res.status(500).json({
      message: 'Eroare la obținerea statusului',
      error: error.message
    });
  }
};

// Endpoint pentru a lista scenele în ordinea corectă
exports.getSceneOrder = async (req, res) => {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const orderFile = path.join(scenesDir, 'scene_order.json');
    
    if (!fs.existsSync(orderFile)) {
      // Reconstruim ordinea dacă nu există
      const sceneOrder = await reconstructSceneOrder();
      res.json({
        message: 'Ordine reconstruită din fișierele existente',
        scenes: sceneOrder
      });
    } else {
      const sceneOrder = JSON.parse(fs.readFileSync(orderFile, 'utf8'));
      res.json({
        message: 'Ordine existentă găsită',
        scenes: sceneOrder
      });
    }
  } catch (error) {
    console.error('❌ Eroare la obținerea ordinii scenelor:', error);
    res.status(500).json({
      message: 'Eroare la obținerea ordinii scenelor',
      error: error.message
    });
  }
};

exports.resetScenes = async (req, res) => {
  try {
    const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
    const animationsDir = path.join(__dirname, '../media/animations');
    const videosDir = path.join(__dirname, '../media/videos');  // Adăugat
    const coursesDir = path.join(__dirname, '../media/courses');
    const tempDir = path.join(__dirname, '../temp');
    
    // Funcție helper pentru ștergerea recursivă
    const cleanDirectory = (dir) => {
      if (fs.existsSync(dir)) {
        fs.readdirSync(dir).forEach(file => {
          const curPath = path.join(dir, file);
          if (fs.lstatSync(curPath).isDirectory()) {
            // Șterge recursiv subdirectoarele
            cleanDirectory(curPath);
            fs.rmdirSync(curPath);
          } else {
            // Șterge fișierele
            fs.unlinkSync(curPath);
          }
        });
      }
    };

    // Curăță toate directoarele
    cleanDirectory(scenesDir);
    cleanDirectory(animationsDir);
    cleanDirectory(videosDir);     // Adăugat
    cleanDirectory(coursesDir);
    cleanDirectory(tempDir);

    // Recreează directoarele goale
    [scenesDir, animationsDir, videosDir, coursesDir, tempDir].forEach(dir => {
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
    });

    res.json({ 
      message: 'Reset complet efectuat',
      status: {
        scenesDeleted: true,
        animationsDeleted: true,
        videosDeleted: true,      // Adăugat
        coursesDeleted: true,
        tempDeleted: true
      }
    });
  } catch (error) {
    console.error('❌ Eroare la reset:', error);
    res.status(500).json({ 
      message: 'Eroare la reset',
      error: error.message 
    });
  }
}; 