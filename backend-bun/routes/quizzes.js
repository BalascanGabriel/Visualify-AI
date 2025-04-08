const express = require('express');
const router = express.Router();
const quizController = require('../controllers/quizController');

router.post('/generate', quizController.generateQuizzes);
router.get('/', quizController.getQuizzes);

module.exports = router; 