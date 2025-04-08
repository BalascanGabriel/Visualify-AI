const { sendToGemini } = require('../services/geminiService');

const generateQuizForConcept = async (concept, context) => {
  try {
    console.log(`📝 Generare quiz pentru: "${concept}" în contextul:`, context);

    const prompt = `Generează 3 întrebări de tip quiz pentru conceptul: "${concept}"
Context: Capitol - "${context.capitol}", Subcapitol - "${context.subcapitol}"

Returnează în format JSON cu următoarea structură:
{
  "concept": "${concept}",
  "questions": [
    {
      "question": "întrebarea",
      "type": "multiple_choice",
      "options": [
        "A. prima opțiune",
        "B. a doua opțiune", 
        "C. a treia opțiune",
        "D. a patra opțiune",
        "E. a cincea opțiune (opțional)"
      ],
      "correct_answers": ["A", "C"],  // Literele corespunzătoare răspunsurilor corecte
      "explanation": "explicație detaliată pentru răspunsurile corecte"
    }
  ]
}

IMPORTANT:
1. Toate opțiunile TREBUIE să înceapă cu "A.", "B.", "C.", etc.
2. Pot exista mai multe răspunsuri corecte
3. În correct_answers pune DOAR literele (A, B, C, etc.)
4. Folosește 4-5 opțiuni pentru fiecare întrebare
5. Explicația trebuie să justifice toate răspunsurile corecte`;

    const response = await sendToGemini(prompt);
    console.log(`✅ Quiz generat pentru: "${concept}"`);
    return response;
  } catch (error) {
    console.error(`❌ Eroare la generarea quiz pentru ${concept}:`, error);
    return {
      concept,
      error: error.message,
      questions: []
    };
  }
};

const generateQuizzes = async (structura) => {
  console.log('📚 Începe generarea quiz-urilor pentru structura:', structura);

  const quizzes = {
    capitole: []
  };

  for (const capitol of structura) {
    console.log(`\n🔍 Procesare capitol: ${capitol.capitol}`);
    
    const capitolQuiz = {
      capitol: capitol.capitol,
      subcapitole: []
    };

    for (const subcapitol of capitol.subcapitole) {
      console.log(`  📖 Subcapitol: ${subcapitol.subcapitol}`);
      
      const subcapitolQuiz = {
        subcapitol: subcapitol.subcapitol,
        concepte: []
      };

      for (const concept of subcapitol.concepte) {
        try {
          console.log(`    ✨ Concept: ${concept}`);
          const quiz = await generateQuizForConcept(concept, {
            capitol: capitol.capitol,
            subcapitol: subcapitol.subcapitol
          });
          subcapitolQuiz.concepte.push(quiz);
          // Pauză mică între cereri pentru a nu supraîncărca API-ul
          await new Promise(resolve => setTimeout(resolve, 1000));
        } catch (error) {
          console.error(`❌ Eroare la quiz pentru ${concept}:`, error);
          subcapitolQuiz.concepte.push({
            concept,
            error: error.message,
            questions: []
          });
        }
      }

      capitolQuiz.subcapitole.push(subcapitolQuiz);
    }

    quizzes.capitole.push(capitolQuiz);
  }

  console.log('✅ Generare quiz-uri completă');
  return quizzes;
};

module.exports = {
  generateQuizzes
}; 