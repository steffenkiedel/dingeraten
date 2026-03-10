// data-loader.js — JSON-Datenbanken laden und cachen

const DataLoader = {
  _cache: {},
  _loading: {},

  async load(category) {
    if (this._cache[category]) return this._cache[category];
    if (this._loading[category]) return this._loading[category];

    this._loading[category] = fetch(`../data/${category}.json`)
      .then(r => {
        if (!r.ok) throw new Error(`Failed to load ${category}.json`);
        return r.json();
      })
      .then(data => {
        this._cache[category] = data;
        delete this._loading[category];
        return data;
      });

    return this._loading[category];
  },

  // Alle Kategorien im Hintergrund vorladen
  preload() {
    const categories = ['laender', 'hauptstaedte', 'gemuese', 'obst', 'tiere'];
    categories.forEach(cat => this.load(cat).catch(() => {}));
  },

  // Items nach Schwierigkeit filtern
  getByDifficulty(items, difficulty) {
    return items.filter(item => item.difficulty === difficulty);
  }
};
