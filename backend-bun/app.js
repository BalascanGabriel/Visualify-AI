// app.js
const express = require('express');
const cors = require('cors');
const fileUpload = require('express-fileupload');

const uploadRoutes = require('./routes/upload');

const app = express();

app.use(cors());
app.use(express.json());
app.use(fileUpload());

app.use('/api/upload', uploadRoutes); // ✅ Rutele de upload

const parseRoutes = require('./routes/parse');
app.use('/api/parse', parseRoutes);

const generateRoutes = require('./routes/generate');
app.use('/api/generate', generateRoutes);


// Health check
app.get('/', (req, res) => {
  res.send('🚀 Backend is alive!');
});

module.exports = app;
