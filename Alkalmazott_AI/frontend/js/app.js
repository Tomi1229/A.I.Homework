const messagesDiv = document.getElementById("messages");
const inputField = document.getElementById("user-input");

function appendMessage(text, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(sender === "user" ? "user-message" : "bot-message");
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function sendMessage() {
    const userInput = inputField.value.trim();
    if (userInput === "") return;

    // Felhasználói üzenet hozzáadása
    appendMessage(userInput, "user");
    inputField.value = "";

    // Küldés a backendhez
    fetch("http://127.0.0.1:8000/ask-ai", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            appendMessage(data.question, "bot");
        })

        .catch(error => {
            console.error("Hiba történt:", error);
        });
}

async function submitAnswer() {
    const userAnswer = document.getElementById("user-answer").value;

    if (!userAnswer.trim()) {
        alert("Kérlek, válaszolj a kérdésre!");
        return;
    }

    try {
        const response = await fetch("http://localhost:8000/ask-ai", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                job_title: jobTitle,
                previous_answer: userAnswer,
            }),
        });

        if (!response.ok) {
            throw new Error(`Hiba történt: ${response.statusText}`);
        }

        const data = await response.json();

        // Ellenőrizzük, hogy van-e "question" kulcs a válaszban
        if (!data.question) {
            throw new Error("A backend nem küldött kérdést.");
        }

        document.getElementById("chat-box").innerHTML += `
            <div class="bot-message">Chatbot: ${data.question}</div>
        `;
        document.getElementById("chat-box").scrollTop = document.getElementById("chat-box").scrollHeight;
    } catch (error) {
        console.error("Hiba történt az API hívás során:", error);
        alert("Hiba történt a kérdés feldolgozása közben.");
    }
}

if (!data.question) {
    document.getElementById("chat-box").innerHTML += `
        <div class="bot-message error">Chatbot: Sajnos nem tudok válaszolni erre a kérdésre.</div>
    `;
} else {
    document.getElementById("chat-box").innerHTML += `
        <div class="bot-message">Chatbot: ${data.question}</div>
    `;
}
