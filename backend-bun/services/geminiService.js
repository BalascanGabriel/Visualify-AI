const axios = require('axios');
require('dotenv').config();

const sendToGemini = async (prompt) => {
  try {
    console.log('🤖 Prompt către Gemini:', prompt.slice(0, 100) + '...');

    const response = await axios.post(
      'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
      {
        contents: [{ parts: [{ text: prompt }] }]
      },
      {
        headers: { 'Content-Type': 'application/json' },
        params: { key: process.env.GEMINI_API_KEY }
      }
    );

    let raw = response.data.candidates?.[0]?.content?.parts?.[0]?.text || '';
    console.log('✅ Răspuns de la Gemini:', raw.slice(0, 100) + '...');

    // Dacă prompt-ul cere cod Manim, returnăm răspunsul brut
    if (prompt.includes('cod Manim')) {
      return raw;
    }

    // Pentru JSON, extragem conținutul dintre marcajele ```json
    const jsonMatch = raw.match(/```json\n?([\s\S]*?)\n?```/);
    if (jsonMatch) {
      try {
        // Eliminăm comentariile înainte de parsare
        const jsonText = jsonMatch[1]
          .split('\n')
          .filter(line => !line.trim().startsWith('//'))
          .join('\n');
        return JSON.parse(jsonText);
      } catch (e) {
        console.error('❌ Eroare la parsarea JSON-ului extras:', e);
      }
    }

    // Încercăm să parsăm direct răspunsul
    try {
      return JSON.parse(raw);
    } catch (e) {
      console.warn('⚠️ Nu s-a putut parsa JSON-ul, returnăm răspunsul brut');
      return { raw };
    }

  } catch (error) {
    console.error("❌ Error from Gemini:", error.response?.data || error.message);
    throw new Error('Failed to fetch response from Gemini');
  }
};

module.exports = {
  sendToGemini
};