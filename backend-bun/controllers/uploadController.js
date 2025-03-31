// controllers/uploadController.js
const pdfParser = require('../utils/pdfParser');
const wordParser = require('../utils/wordParser');
const path = require('path');
const fs = require('fs');

exports.handleUpload = async (req, res) => {
  try {
    if (!req.files || !req.files.file) {
      return res.status(400).json({ message: 'No file uploaded' });
    }

    const file = req.files.file;
    const ext = path.extname(file.name).toLowerCase();

    const uploadPath = path.join(__dirname, '..', 'uploads', file.name);
    await file.mv(uploadPath);

    let extractedText = '';

    if (ext === '.pdf') {
      extractedText = await pdfParser(uploadPath);
    } else if (ext === '.docx') {
      extractedText = await wordParser(uploadPath);
    } else {
      return res.status(400).json({ message: 'Unsupported file type' });
    }

    // Ștergem fișierul după parsare
    fs.unlinkSync(uploadPath);

    res.status(200).json({ text: extractedText });
  } catch (err) {
    console.error('❌ Upload error:', err);
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
