// utils/pdfParser.js
const fs = require('fs');
const pdfParse = require('pdf-parse');

module.exports = async (filePath) => {
  const buffer = fs.readFileSync(filePath);
  const data = await pdfParse(buffer);
  return data.text;
};
