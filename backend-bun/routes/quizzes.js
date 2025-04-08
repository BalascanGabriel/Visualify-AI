const express = require('express');
const router = express.Router();
const quizController = require('../controllers/quizController');

// Generează quiz-uri noi
router.post('/generate', quizController.generateQuizzes);

// Obține quiz-urile existente
router.get('/', quizController.getQuizzes);

module.exports = router; 