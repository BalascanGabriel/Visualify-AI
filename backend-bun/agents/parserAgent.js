// agents/parserAgent.js
const geminiService = require('../services/geminiService');

exports.parseText = async (text) => {
  const prompt = `
Am următorul conținut educațional:

"""${text}"""

1️⃣ Fă un rezumat scurt, clar și educațional.
2️⃣ Împarte conținutul pe capitole și subcapitole relevante.
3️⃣ Sub fiecare subcapitol, extrage conceptele cheie.

Răspunsul tău trebuie să fie format JSON cu următoarea structură:

{
  "rezumat": "...",
  "structura": [
    {
      "capitol": "Nume Capitol",
      "subcapitole": [
        {
          "subcapitol": "Nume Subcapitol",
          "concepte": ["concept 1", "concept 2", ...]
        }
      ]
    }
  ]
}
`;

  const result = await geminiService.sendToGemini(prompt);
  return result;
};
