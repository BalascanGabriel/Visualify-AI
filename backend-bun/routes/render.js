const express = require('express');
const router = express.Router();
const renderController = require('../controllers/renderController');

router.post('/manim', renderController.renderManimScenes);

module.exports = router; 