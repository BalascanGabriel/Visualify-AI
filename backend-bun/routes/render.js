const express = require('express');
const router = express.Router();
const renderController = require('../controllers/renderController');
const { sendToGemini } = require('../services/geminiService');

router.post('/manim', renderController.renderManimScenes);
router.post('/combine', renderController.combineVideos);
router.get('/status', renderController.getStatus);
router.get('/scene-order', renderController.getSceneOrder);
router.post('/reset', renderController.resetScenes);

router.post('/test-gemini', async (req, res) => {
  try {
    const prompt = `Scrie cod Python Manim pentru a explica conceptul: "Cercul unitate".
Scrie DOAR codul din metoda construct(), fără importuri și fără definirea clasei.
Folosește doar clase și funcții din biblioteca Manim.
Exemplu format așteptat:
    # Creăm un cerc
    circle = Circle()
    self.play(Create(circle))
    
    # Adăugăm text
    text = Text("Hello")
    self.play(Write(text))

Returnează DOAR codul Python pentru metoda construct(), fără alte elemente.`;

    console.log('🧪 Test Gemini - Trimitere prompt...');
    const result = await sendToGemini(prompt);
    console.log('✅ Test Gemini - Răspuns primit:', result);

    res.json({
      success: true,
      result
    });
  } catch (error) {
    console.error('❌ Eroare test Gemini:', error);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

module.exports = router; 