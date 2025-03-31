// routes/parse.js
const express = require('express');
const router = express.Router();
const parseController = require('../controllers/parseController');

router.post('/', parseController.handleParsing);

module.exports = router;
