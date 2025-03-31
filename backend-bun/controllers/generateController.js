// controllers/generateController.js
const path = require('path');
const fs = require('fs');
const pdfParser = require('../utils/pdfParser');
const wordParser = require('../utils/wordParser');
const parserAgent = require('../agents/parserAgent');
const { buildMindMap } = require('../utils/mindmapUtils');

exports.generateCourseFromFile = async (req, res) => {
  try {
    if (!req.files || !req.files.file) {
      return res.status(400).json({ message: 'No file uploaded' });
    }

    const file = req.files.file;
    const ext = path.extname(file.name).toLowerCase();
    const tempPath = path.join(__dirname, '..', 'uploads', file.name);

    await file.mv(tempPath);

    let extractedText = '';

    if (ext === '.pdf') {
      extractedText = await pdfParser(tempPath);
    } else if (ext === '.docx') {
      extractedText = await wordParser(tempPath);
    } else {
      return res.status(400).json({ message: 'Unsupported file type' });
    }

    fs.unlinkSync(tempPath); // curățăm după extragere

    const parsedData = await parserAgent.parseText(extractedText);

    if (!parsedData.structura) {
      return res.status(400).json({
        message: 'Structura generată de Gemini este invalidă.',
        raw: parsedData.raw || null
      });
    }

    const mindmap = buildMindMap(parsedData.structura);

    res.status(200).json({
      rezumat: parsedData.rezumat,
      structura: parsedData.structura,
      mindmap
    });

  } catch (error) {
    console.error('❌ generateCourseFromFile error:', error);
    res.status(500).json({ message: 'Server error', error: error.message });
  }
};
