const express = require('express');
const multer = require('multer');
const pdfParse = require('pdf-parse');
const axios = require('axios');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

// Serve the media folder statically
app.use("/media", express.static(path.join(__dirname, "media")));

// Configure Multer for file uploads
const uploadMiddleware = multer({ dest: 'uploads/' });

app.post('/upload', uploadMiddleware.single('pdf'), async (req, res) => {
    try {
        const pdfPath = req.file.path;

        // Read and parse PDF
        const pdfBuffer = fs.readFileSync(pdfPath);
        const pdfData = await pdfParse(pdfBuffer);
        const pdfText = pdfData.text;

        // Send text to Gemini API
        const geminiUrl = `https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key=${process.env.GEMINI_API_KEY}`;
        const prompt = `
        Extract the main concepts and formulas from the following text and generate Manim animation code to visually explain them.
        Do NOT use external images or non-standard classes. Use ONLY built-in Manim classes like Text, MathTex, Line, Arrow, Circle, Rectangle, Dot.
        Return ONLY Python code without explanations:

        ${pdfText}
        `;

        const geminiResponse = await axios.post(geminiUrl, {
            contents: [{ parts: [{ text: prompt }] }]
        });

        const responseText = geminiResponse.data.candidates[0].content.parts[0].text;

        // Extract Manim code from response
        const match = responseText.match(/```python(.*?)```/s);
        if (!match) {
            return res.status(400).json({ status: 'error', message: 'No valid Manim code found.' });
        }

        const manimCode = match[1].trim();
        const scriptPath = './scripts/generated_script.py';
        fs.writeFileSync(scriptPath, manimCode);

        // Extract class name
        const sceneMatch = manimCode.match(/class\s+(\w+)\s*\(Scene\)/);
        const sceneName = sceneMatch ? sceneMatch[1] : "DefaultScene";

        // Run Manim to generate video
        execSync(`manim -ql ${scriptPath} ${sceneName}`);

        const videoPath = `/media/videos/generated_script/480p15/${sceneName}.mp4`;

        // Remove uploaded PDF file after processing
        fs.unlinkSync(pdfPath);

        if (fs.existsSync(path.join(__dirname, videoPath))) {
            return res.json({ status: 'success', videoUrl: videoPath });
        } else {
            res.json({ status: 'success', videoUrl: `/videos/${sceneName}.mp4` });

        }

    } catch (error) {
        console.error(error);
        res.status(500).json({ status: 'error', message: error.message });
    }
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});
