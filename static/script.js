async function translateText() {
    const text = document.getElementById('translateText').value;
    const targetLanguage = document.getElementById('languageSelect').value;
    const response = await fetch('/translate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text, target_language: targetLanguage })
    });
    const result = await response.json();
    document.getElementById('translationResult').innerText = result.translated_text;
}

async function askQuestion() {
    const question = document.getElementById('question').value;
    const context = document.getElementById('context').value;
    const response = await fetch('/question/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question, context })
    });
    const result = await response.json();
    document.getElementById('questionResult').innerText = result.answer;
}