// speech.js — Web Speech API (Mikrofon-Eingabe)

const SpeechInput = {
  _recognition: null,
  _listening: false,

  isSupported() {
    return 'SpeechRecognition' in window || 'webkitSpeechRecognition' in window;
  },

  toggle(onResult, language) {
    if (!this.isSupported()) {
      alert(language === 'de'
        ? 'Spracherkennung wird in diesem Browser nicht unterstützt.'
        : 'Speech recognition is not supported in this browser.');
      return;
    }

    if (this._listening) {
      this.stop();
    } else {
      this.start(onResult, language);
    }
  },

  start(onResult, language) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    this._recognition = new SpeechRecognition();
    this._recognition.lang = language === 'de' ? 'de-DE' : 'en-US';
    this._recognition.interimResults = false;
    this._recognition.maxAlternatives = 1;
    this._recognition.continuous = false;

    this._recognition.onstart = () => {
      this._listening = true;
      document.getElementById('btn-mic').classList.add('listening');
    };

    this._recognition.onresult = (event) => {
      const text = event.results[0][0].transcript;
      onResult(text);
      this.stop();
    };

    this._recognition.onerror = () => { this.stop(); };
    this._recognition.onend = () => { this.stop(); };

    this._recognition.start();
  },

  stop() {
    this._listening = false;
    document.getElementById('btn-mic').classList.remove('listening');
    if (this._recognition) {
      try { this._recognition.stop(); } catch {}
      this._recognition = null;
    }
  }
};
