document.addEventListener('DOMContentLoaded', () => {
    const generateQuestionBtn = document.getElementById('generateQuestionBtn');
    const questionArea = document.getElementById('question');
    const topicSelector = document.getElementById('topic');

    // Gomb eseménykezelő
    generateQuestionBtn.addEventListener('click', async () => {
        const selectedTopic = topicSelector.value;

        // API-hívás
        try {
            const response = await fetch('http://127.0.0.1:8000/api/chatbot/generate-question', {

                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic: selectedTopic }),
            });

            if (response.ok) {
                const data = await response.json();
                questionArea.textContent = data.question;
            } else {
                questionArea.textContent = 'Hiba történt a kérdés generálásakor.';
            }
        } catch (error) {
            questionArea.textContent = 'Nem sikerült csatlakozni a szerverhez.';
            console.error(error);
        }
    });

    document.getElementById("submit-answer").addEventListener("click", async () => {
        const question = document.getElementById("question-display").innerText;
        const userAnswer = document.getElementById("user-answer").value;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/chatbot/interview', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question, user_answer: userAnswer }),
            });

            const data = await response.json();
            document.getElementById("feedback-display").innerText = data.feedback;
        } catch (error) {
            console.error("Hiba történt: ", error);
            document.getElementById("feedback-display").innerText = "Nem sikerült kapcsolódni a szerverhez.";
        }
    });

});
