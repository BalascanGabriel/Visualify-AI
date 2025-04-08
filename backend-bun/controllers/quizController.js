const path = require('path');
const fs = require('fs');
const { generateQuizzes } = require('../agents/quizGenerator');

exports.generateQuizzes = async (req, res) => {
  try {
    // Citim structura salvată
    const structurePath = path.join(__dirname, '../temp/last_structure.json');
    if (!fs.existsSync(structurePath)) {
      return res.status(400).json({
        message: 'Nu există o structură generată. Rulați mai întâi /api/generate'
      });
    }

    const structure = JSON.parse(fs.readFileSync(structurePath, 'utf8'));
    console.log('📚 Structura citită:', structure);

    if (!structure.structura || !Array.isArray(structure.structura)) {
      return res.status(400).json({
        message: 'Structura salvată este invalidă',
        structure
      });
    }

    console.log('📝 Începe generarea quiz-urilor...');
    const quizzes = await generateQuizzes(structure.structura);
    console.log('✅ Quiz-uri generate:', quizzes);

    // Salvăm quiz-urile generate
    const quizzesDir = path.join(__dirname, '../temp');
    if (!fs.existsSync(quizzesDir)) {
      fs.mkdirSync(quizzesDir, { recursive: true });
    }

    const quizzesPath = path.join(quizzesDir, 'generated_quizzes.json');
    fs.writeFileSync(quizzesPath, JSON.stringify(quizzes, null, 2));
    console.log('💾 Quiz-uri salvate în:', quizzesPath);

    res.json({
      message: 'Quiz-uri generate cu succes',
      quizzes
    });

  } catch (error) {
    console.error('❌ Eroare la generarea quiz-urilor:', error);
    res.status(500).json({
      message: 'Eroare la generarea quiz-urilor',
      error: error.message,
      stack: error.stack
    });
  }
};

exports.getQuizzes = async (req, res) => {
  try {
    const quizzesPath = path.join(__dirname, '../temp/generated_quizzes.json');
    console.log('🔍 Căutare quiz-uri în:', quizzesPath);

    if (!fs.existsSync(quizzesPath)) {
      console.log('❌ Nu s-au găsit quiz-uri');
      return res.status(404).json({
        message: 'Nu există quiz-uri generate. Rulați mai întâi /api/quizzes/generate'
      });
    }

    const quizzes = JSON.parse(fs.readFileSync(quizzesPath, 'utf8'));
    console.log('✅ Quiz-uri găsite:', Object.keys(quizzes).length);

    res.json(quizzes);

  } catch (error) {
    console.error('❌ Eroare la citirea quiz-urilor:', error);
    res.status(500).json({
      message: 'Eroare la citirea quiz-urilor',
      error: error.message,
      stack: error.stack
    });
  }
}; 