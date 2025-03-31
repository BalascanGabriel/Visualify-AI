// agents/mediaGenerator/imageAgent.js
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const STABLE_DIFFUSION_URL = 'http://127.0.0.1:7860/sdapi/v1/txt2img'; // local WebUI

const generateImage = async (prompt, conceptId) => {
  try {
    const response = await axios.post(STABLE_DIFFUSION_URL, {
      prompt,
      steps: 20,
      width: 512,
      height: 512
    });

    const base64Image = response.data.images[0];
    const imageBuffer = Buffer.from(base64Image, 'base64');

    const imagePath = path.join(__dirname, '..', '..', 'media', 'images', `${conceptId}.png`);
    fs.writeFileSync(imagePath, imageBuffer);

    return `/media/images/${conceptId}.png`;
  } catch (err) {
    console.error(`❌ Failed to generate image for concept: ${prompt}`, err.message);
    return null;
  }
};

module.exports = { generateImage };
