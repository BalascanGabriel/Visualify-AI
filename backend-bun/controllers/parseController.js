// controllers/parseController.js
const parserAgent = require('../agents/parserAgent');
const { buildMindMap } = require('../utils/mindmapUtils');

exports.handleParsing = async (req, res) => {
  try {
    const { text } = req.body;

    if (!text) {
      return res.status(400).json({ message: 'No text provided' });
    }

    const parsedData = await parserAgent.parseText(text);

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
    console.error('❌ Error parsing with Gemini:', error);
    res.status(500).json({ message: 'Server error', error: error.message });
  }
};
