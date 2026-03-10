// openai-client.js — OpenAI API Integration

const OpenAIClient = {
  API_URL: 'https://api.openai.com/v1/chat/completions',
  MODEL: 'gpt-4o-mini',

  async ask(item, qaHistory, question, language) {
    const key = GameState.apiKey;
    if (!key) throw new Error('No API key');

    const langName = language === 'de' ? 'Deutsch' : 'English';
    const systemPrompt = `Du bist der Spielleiter des Kinderspiels 'Dingeraten'.
Das gesuchte Wort ist: "${item.name[language] || item.name.de}".
Kontext: ${item.qa_context}

Regeln:
- Antworte NUR mit: "Ja", "Nein", "Teilweise" oder einer kurzen Rückfrage bei Unklarheit (max. 1 Satz)
- NIEMALS das gesuchte Wort verraten oder Hinweise darauf geben
- Wenn du unsicher bist, sage "Das weiß ich leider nicht"
- Halluziniere NICHT — nur was du sicher weißt
- Antworte auf ${langName}, kurz (max. 2 Sätze)`;

    const messages = [{ role: 'system', content: systemPrompt }];

    // Bisheriger Q&A-Verlauf als Kontext
    for (const qa of qaHistory.slice(-8)) {
      messages.push({ role: 'user', content: qa.question });
      messages.push({ role: 'assistant', content: qa.answer });
    }
    messages.push({ role: 'user', content: question });

    const resp = await fetch(this.API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${key}`
      },
      body: JSON.stringify({
        model: this.MODEL,
        messages,
        max_tokens: 80,
        temperature: 0.1
      }),
      signal: AbortSignal.timeout(10000)
    });

    if (!resp.ok) throw new Error(`OpenAI API error: ${resp.status}`);
    const data = await resp.json();
    return data.choices[0].message.content.trim();
  },

  async testKey(key) {
    if (!key) return false;
    try {
      const resp = await fetch('https://api.openai.com/v1/models', {
        headers: { 'Authorization': `Bearer ${key}` },
        signal: AbortSignal.timeout(5000)
      });
      return resp.ok;
    } catch {
      return false;
    }
  },

  isOnline() {
    return navigator.onLine;
  }
};
