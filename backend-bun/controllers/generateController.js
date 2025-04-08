// controllers/generateController.js
const path = require('path');
const fs = require('fs');
const pdfParser = require('../utils/pdfParser');
const wordParser = require('../utils/wordParser');
const parserAgent = require('../agents/parserAgent');
const { buildMindMap } = require('../utils/mindmapUtils');

exports.generateCourseFromFile = async (req, res) => {
  try {
    console.log('🚀 Începe procesul de generare...');

    if (!req.files || !req.files.file) {
      return res.status(400).json({ message: 'No file uploaded' });
    }

    const file = req.files.file;
    console.log('📁 Fișier primit:', file.name);

    const ext = path.extname(file.name).toLowerCase();
    const tempPath = path.join(__dirname, '..', 'uploads', file.name);

    // Creăm directorul uploads dacă nu există
    const uploadsDir = path.join(__dirname, '..', 'uploads');
    if (!fs.existsSync(uploadsDir)) {
      fs.mkdirSync(uploadsDir, { recursive: true });
    }

    try {
      await file.mv(tempPath);
      console.log('✅ Fișier salvat temporar:', tempPath);
    } catch (moveError) {
      console.error('❌ Eroare la salvarea fișierului:', moveError);
      return res.status(500).json({ message: 'Error saving file', error: moveError.message });
    }

    let extractedText = '';

    try {
      if (ext === '.pdf') {
        console.log('📄 Parsare PDF...');
        extractedText = await pdfParser(tempPath);
      } else if (ext === '.docx') {
        console.log('📄 Parsare DOCX...');
        extractedText = await wordParser(tempPath);
      } else {
        return res.status(400).json({ message: 'Unsupported file type' });
      }
      console.log('✅ Text extras cu succes');
    } catch (parseError) {
      console.error('❌ Eroare la parsarea fișierului:', parseError);
      return res.status(500).json({ message: 'Error parsing file', error: parseError.message });
    }

    try {
      // Curățăm fișierul temporar
      fs.unlinkSync(tempPath);
      console.log('🧹 Fișier temporar șters');
    } catch (unlinkError) {
      console.warn('⚠️ Nu s-a putut șterge fișierul temporar:', unlinkError);
    }

    try {
      console.log('🤖 Trimitere text către Gemini...');
      const parsedData = await parserAgent.parseText(extractedText);
      console.log('✅ Răspuns primit de la Gemini');

      if (!parsedData || !parsedData.structura) {
        console.error('❌ Date invalide de la Gemini:', parsedData);
        return res.status(400).json({
          message: 'Structura generată de Gemini este invalidă.',
          raw: parsedData?.raw || null
        });
      }

      console.log('🗺️ Generare mindmap...');
      const mindmap = buildMindMap(parsedData.structura);

      // Salvăm structura pentru referință ulterioară
      const tempDir = path.join(__dirname, '../temp');
      if (!fs.existsSync(tempDir)) {
        fs.mkdirSync(tempDir, { recursive: true });
      }
      fs.writeFileSync(
        path.join(tempDir, 'last_structure.json'),
        JSON.stringify(parsedData, null, 2)
      );
      console.log('💾 Structură salvată în temp/last_structure.json');

      // Generăm animațiile Manim
      console.log('🎬 Începe generarea scripturilor Manim...');
      const conceptMapperAgent = require('../agents/conceptMapperAgent');
      try {
        // Verificăm dacă directorul există
        const scenesDir = path.join(__dirname, '../scripts/animator/generated_scenes');
        if (!fs.existsSync(scenesDir)) {
          fs.mkdirSync(scenesDir, { recursive: true });
        }

        // Ștergem scripturile vechi înainte de generare
        if (fs.existsSync(scenesDir)) {
          fs.readdirSync(scenesDir)
            .filter(file => file.endsWith('.py'))
            .forEach(file => {
              const filePath = path.join(scenesDir, file);
              console.log('🗑️ Ștergere:', filePath);
              fs.unlinkSync(filePath);
            });
        }

        // Ștergem și scene_order.json dacă există
        const orderFile = path.join(scenesDir, 'scene_order.json');
        if (fs.existsSync(orderFile)) {
          console.log('🗑️ Ștergere:', orderFile);
          fs.unlinkSync(orderFile);
        }

        console.log('📁 Generare în:', scenesDir);
        const scenes = await conceptMapperAgent.generateConceptAnimations(parsedData.structura);
        console.log('✅ Scripturi Manim generate:', scenes.length);

        // Verificăm dacă s-au generat scripturile
        const generatedFiles = fs.readdirSync(scenesDir)
          .filter(file => file.endsWith('.py'));
        console.log('📝 Scripturi generate:', generatedFiles);

        if (generatedFiles.length === 0) {
          throw new Error('Nu s-au generat scripturile Python');
        }

        res.status(200).json({
          rezumat: parsedData.rezumat,
          structura: parsedData.structura,
          mindmap,
          scenes,
          generatedFiles,
          message: "Conținutul a fost generat cu succes!"
        });
      } catch (error) {
        console.error('❌ Eroare la generarea animațiilor:', error);
        res.status(500).json({
          message: 'Eroare la generarea animațiilor',
          error: error.message,
          stack: error.stack
        });
      }

    } catch (processError) {
      console.error('❌ Eroare la procesarea datelor:', processError);
      res.status(500).json({ 
        message: 'Error processing data', 
        error: processError.message,
        stack: processError.stack 
      });
    }

  } catch (error) {
    console.error('❌ Eroare generală în generateCourseFromFile:', error);
    res.status(500).json({ 
      message: 'Server error', 
      error: error.message,
      stack: error.stack 
    });
  }
};
