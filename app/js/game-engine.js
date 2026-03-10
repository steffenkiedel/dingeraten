// game-engine.js — Spiellogik: Item auswählen, Antwort prüfen

const GameEngine = {
  _usedIds: new Set(),

  async selectItem(category, difficulty) {
    const allItems = await DataLoader.load(category);
    let pool = DataLoader.getByDifficulty(allItems, difficulty);

    // Bereits gespielte Items ausschließen
    let fresh = pool.filter(item => !this._usedIds.has(item.id));
    if (fresh.length === 0) {
      // Alle Items einmal gesehen → Reset
      pool.forEach(item => this._usedIds.delete(item.id));
      fresh = pool;
    }

    if (fresh.length === 0) return null;

    const item = fresh[Math.floor(Math.random() * fresh.length)];
    this._usedIds.add(item.id);
    return item;
  },

  // Prüft ob die Rateantwort korrekt ist (tolerant, case-insensitive)
  checkAnswer(input, item, lang) {
    const normalize = str => str.toLowerCase()
      .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss')
      .replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();

    const guess = normalize(input);
    const nameDe = normalize(item.name.de);
    const nameEn = normalize(item.name.en || '');
    const nameLang = normalize(item.name[lang] || '');

    // Exakter Match oder enthält den Namen
    return guess === nameDe || guess === nameEn || guess === nameLang
      || guess.includes(nameDe) || (nameDe.length > 3 && nameDe.includes(guess) && guess.length > 3)
      || (nameEn && (guess.includes(nameEn) || (nameEn.length > 3 && nameEn.includes(guess) && guess.length > 3)));
  },

  reset() {
    this._usedIds.clear();
  }
};
