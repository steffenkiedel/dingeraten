// state.js — Globales Spielzustands-Objekt

const GameState = {
  // Einstellungen
  language: 'de',       // 'de' | 'en'
  apiKey: null,         // OpenAI API-Key aus localStorage

  // Setup
  category: null,       // 'laender' | 'hauptstaedte' | 'gemuese' | 'obst' | 'tiere'
  difficulty: null,     // 1 | 2 | 3 | 4 (4 = steigend)

  // Laufendes Spiel
  currentItem: null,    // Komplettes Item-Objekt
  questionCount: 0,
  maxQuestions: 20,
  qaHistory: [],        // [{question, answer, type}] type: 'yes'|'no'|'partial'|'unclear'|'wrong'
  hintsUsed: 0,
  gameStatus: 'idle',   // 'idle' | 'playing' | 'won' | 'lost'

  // Progression für Schwierigkeit "steigend"
  sessionCorrect: 0,    // Richtig erratene Items in dieser Session
  currentProgressLevel: 1,

  reset() {
    this.currentItem = null;
    this.questionCount = 0;
    this.qaHistory = [];
    this.hintsUsed = 0;
    this.gameStatus = 'idle';
  },

  addQA(question, answer, type) {
    this.qaHistory.push({ question, answer, type });
    this.questionCount++;
  },

  nextHint() {
    if (!this.currentItem) return null;
    const hints = this.currentItem.hints;
    if (this.hintsUsed >= hints.length) return null;
    const hint = hints[this.hintsUsed];
    this.hintsUsed++;
    return hint[this.language] || hint['de'];
  },

  getEffectiveDifficulty() {
    if (this.difficulty !== 4) return this.difficulty;
    return this.currentProgressLevel;
  },

  onCorrectAnswer() {
    this.sessionCorrect++;
    if (this.difficulty === 4) {
      if (this.sessionCorrect % 3 === 0 && this.currentProgressLevel < 3) {
        this.currentProgressLevel++;
      }
    }
  },

  loadApiKey() {
    this.apiKey = localStorage.getItem('dingeraten_api_key') || null;
  },

  saveApiKey(key) {
    this.apiKey = key;
    if (key) {
      localStorage.setItem('dingeraten_api_key', key);
    } else {
      localStorage.removeItem('dingeraten_api_key');
    }
  },

  loadLanguage() {
    this.language = localStorage.getItem('dingeraten_lang') || 'de';
  },

  saveLanguage(lang) {
    this.language = lang;
    localStorage.setItem('dingeraten_lang', lang);
  }
};
