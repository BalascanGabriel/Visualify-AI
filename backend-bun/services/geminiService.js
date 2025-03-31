const axios = require('axios');
require('dotenv').config();

exports.sendToGemini = async (prompt) => {
  try {
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

    // 🧼 Curățare robustă: scoatem tot ce e între blocurile ```
    raw = raw.replace(/```json\n?/, '').replace(/```/, '').trim();

    try {
      return JSON.parse(raw);
    } catch (e) {
      console.warn('⚠️ Nu s-a putut parsa JSON-ul, returnăm brut.');
      return { raw };
    }
  } catch (error) {
    console.error("❌ Error from Gemini:", error.response?.data || error.message);
    throw new Error('Failed to fetch response from Gemini');
  }
};