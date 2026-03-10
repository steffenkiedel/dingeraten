// i18n.js — Lokalisierung DE/EN

const i18n = {
  _strings: {},

  async load(lang) {
    const resp = await fetch(`./locales/${lang}.json`);
    if (!resp.ok) throw new Error(`Cannot load locale: ${lang}`);
    this._strings = await resp.json();
    document.documentElement.lang = lang;
  },

  // Gibt den übersetzten String zurück. Unterstützt dot-notation: t('game.send')
  // Platzhalter: t('game.questionCounter', {n: 3, max: 20})
  t(key, vars = {}) {
    const parts = key.split('.');
    let val = this._strings;
    for (const part of parts) {
      if (val == null) return key;
      val = val[part];
    }
    if (typeof val !== 'string') return key;
    return val.replace(/\{(\w+)\}/g, (_, k) => vars[k] ?? `{${k}}`);
  },

  // Aktualisiert alle Elemente mit data-i18n Attribut
  applyAll() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      const translation = this.t(key);
      if (translation !== key) el.textContent = translation;
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.dataset.i18nPlaceholder;
      const translation = this.t(key);
      if (translation !== key) el.placeholder = translation;
    });
  }
};
