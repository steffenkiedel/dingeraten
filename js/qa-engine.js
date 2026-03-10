// qa-engine.js — Online/Offline Q&A Routing + Keyword-Pattern-Matching

const QAEngine = {
  // ===== Hauptfunktion =====
  async answer(question, item, qaHistory, language) {
    // Ebene 1: Online + API-Key vorhanden
    if (OpenAIClient.isOnline() && GameState.apiKey) {
      try {
        const text = await OpenAIClient.ask(item, qaHistory, question, language);
        const type = this._classifyAnswer(text, language);
        return { answer: text, type };
      } catch (e) {
        console.warn('OpenAI failed, falling back to offline:', e.message);
      }
    }

    // Ebene 2: Offline-Matching
    return this._offlineAnswer(question, item, language);
  },

  // Klassifiziert eine Antwort in einen Bubble-Typ für das Styling
  _classifyAnswer(text, lang) {
    const t = text.toLowerCase();
    const yesWords = lang === 'de'
      ? ['ja', 'korrekt', 'richtig', 'genau', 'stimmt']
      : ['yes', 'correct', 'right', 'exactly', 'indeed'];
    const noWords = lang === 'de'
      ? ['nein', 'falsch', 'nicht', 'kein', 'keine']
      : ['no', 'not', 'wrong', 'incorrect', "isn't", "aren't"];
    const partialWords = lang === 'de'
      ? ['teilweise', 'bedingt', 'kommt darauf']
      : ['partly', 'partially', 'depends', 'sort of'];

    if (yesWords.some(w => t.startsWith(w))) return 'yes';
    if (noWords.some(w => t.startsWith(w))) return 'no';
    if (partialWords.some(w => t.includes(w))) return 'partial';
    return 'unclear';
  },

  // ===== Offline-Matching =====
  _offlineAnswer(question, item, lang) {
    const q = question.toLowerCase()
      .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss');

    const facts = item.facts;
    const cat = item.category;

    const YES  = lang === 'de' ? 'Ja.' : 'Yes.';
    const NO   = lang === 'de' ? 'Nein.' : 'No.';
    const DUNNO = lang === 'de'
      ? 'Das weiß ich leider nicht genau. Frag etwas anderes!'
      : "I'm not sure about that. Try a different question!";

    // ===== Länder =====
    if (cat === 'laender' || cat === 'hauptstaedte') {
      if (this._has(q, ['europa', 'european', 'europe'])) {
        return this._bool(facts.continent === 'Europa', YES, NO);
      }
      if (this._has(q, ['asien', 'asia', 'asian'])) {
        return this._bool(facts.continent === 'Asien', YES, NO);
      }
      if (this._has(q, ['afrika', 'africa', 'african'])) {
        return this._bool(facts.continent === 'Afrika', YES, NO);
      }
      if (this._has(q, ['nordamerika', 'north america', 'sued', 'south america', 'sudamerika', 'latein', 'latin'])) {
        const na = this._has(q, ['nord', 'north']);
        const sa = this._has(q, ['sued', 'south', 'latein', 'latin', 'sued', 'sud']);
        if (na) return this._bool(facts.continent === 'Nordamerika', YES, NO);
        if (sa) return this._bool(facts.continent === 'Südamerika', YES, NO);
        return this._bool(['Nordamerika', 'Südamerika'].includes(facts.continent), YES, NO);
      }
      if (this._has(q, ['ozeanien', 'oceania', 'australien', 'australia'])) {
        return this._bool(facts.continent === 'Australien/Ozeanien', YES, NO);
      }
      if (this._has(q, ['meer', 'sea', 'ocean', 'kuste', 'coast', 'meereszugang'])) {
        return this._bool(facts.has_sea_access === true, YES, NO);
      }
      if (this._has(q, ['gross', 'large', 'big', 'flache', 'area', 'grosse', 'groesser'])) {
        const area = facts.area_km2;
        if (!area) return { answer: DUNNO, type: 'unclear' };
        return this._bool(area > 200000, YES, NO);
      }
      if (this._has(q, ['klein', 'small', 'little'])) {
        const area = facts.area_km2;
        if (!area) return { answer: DUNNO, type: 'unclear' };
        return this._bool(area < 50000, YES, NO);
      }
      if (this._has(q, ['viel einwohner', 'viele einwohner', 'many people', 'bevolker', 'million'])) {
        const pop = facts.population_million;
        if (!pop) return { answer: DUNNO, type: 'unclear' };
        return this._bool(pop > 50, YES, NO);
      }
      if (this._has(q, ['eu', 'europaische union', 'european union'])) {
        return this._bool(facts.in_eu === true, YES, NO);
      }
      if (this._has(q, ['insel', 'island'])) {
        return this._bool(facts.is_island === true, YES, NO);
      }
      if (this._has(q, ['englisch', 'english', 'spricht man englisch'])) {
        return this._bool(
          Array.isArray(facts.language)
            ? facts.language.some(l => l.toLowerCase().includes('englisch') || l.toLowerCase().includes('english'))
            : (facts.language || '').toLowerCase().includes('englisch'),
          YES, NO
        );
      }
      if (this._has(q, ['deutsch', 'german', 'spricht man deutsch'])) {
        return this._bool(
          (facts.language || '').toLowerCase().includes('deutsch'),
          YES, NO
        );
      }
    }

    // ===== Tiere =====
    if (cat === 'tiere') {
      if (this._has(q, ['saugetier', 'mammal', 'warm', 'warm-blooded'])) {
        return this._bool(facts.type === 'Säugetier', YES, NO);
      }
      if (this._has(q, ['vogel', 'bird', 'fliegen', 'fly', 'fliegt'])) {
        return this._bool(facts.type === 'Vogel', YES, NO);
      }
      if (this._has(q, ['reptil', 'reptile', 'schlange', 'snake', 'eidechse', 'lizard'])) {
        return this._bool(facts.type === 'Reptil', YES, NO);
      }
      if (this._has(q, ['fisch', 'fish', 'wasser', 'water', 'schwimm'])) {
        return this._bool(facts.type === 'Fisch' || facts.habitat === 'Wasser' || facts.habitat === 'Meer', YES, NO);
      }
      if (this._has(q, ['haustier', 'pet', 'domestic', 'zahm'])) {
        return this._bool(facts.domestic === true, YES, NO);
      }
      if (this._has(q, ['gross', 'large', 'big', 'grosse', 'riesig', 'giant'])) {
        return this._bool(facts.size === 'groß' || facts.size === 'sehr groß', YES, NO);
      }
      if (this._has(q, ['klein', 'small', 'tiny', 'winzig'])) {
        return this._bool(facts.size === 'klein', YES, NO);
      }
      if (this._has(q, ['vier beine', '4 beine', 'four leg', 'vierbeiner', 'vierfussig'])) {
        return this._bool(facts.legs === 4, YES, NO);
      }
      if (this._has(q, ['keine beine', 'no legs', 'beinlos'])) {
        return this._bool(facts.legs === 0, YES, NO);
      }
      if (this._has(q, ['fleischfresser', 'carnivore', 'fleisch', 'meat', 'jager', 'predator'])) {
        return this._bool(facts.diet === 'Fleischfresser' || facts.diet === 'Raubtier', YES, NO);
      }
      if (this._has(q, ['pflanzenfresser', 'herbivore', 'pflanze', 'gras', 'grass'])) {
        return this._bool(facts.diet === 'Pflanzenfresser', YES, NO);
      }
      if (this._has(q, ['afrika', 'africa', 'african', 'savanne', 'savanna'])) {
        const cont = Array.isArray(facts.continent) ? facts.continent : [facts.continent];
        return this._bool(cont.some(c => c && c.includes('Afrika')), YES, NO);
      }
      if (this._has(q, ['gefahrdet', 'endangered', 'aussterben', 'extinct'])) {
        return this._bool(facts.endangered === true, YES, NO);
      }
      if (this._has(q, ['fell', 'fur', 'haare', 'hair'])) {
        return this._bool(facts.has_fur === true, YES, NO);
      }
    }

    // ===== Gemüse =====
    if (cat === 'gemuese') {
      if (this._has(q, ['rot', 'red', 'rote'])) {
        const colors = Array.isArray(facts.color) ? facts.color : [facts.color];
        return this._bool(colors.some(c => c && c.includes('rot')), YES, NO);
      }
      if (this._has(q, ['grun', 'green', 'grune'])) {
        const colors = Array.isArray(facts.color) ? facts.color : [facts.color];
        return this._bool(colors.some(c => c && (c.includes('grün') || c.includes('grun') || c.includes('green'))), YES, NO);
      }
      if (this._has(q, ['unter der erde', 'underground', 'unter erde', 'boden', 'wurzel', 'root'])) {
        return this._bool(facts.grows_underground === true, YES, NO);
      }
      if (this._has(q, ['roh essen', 'raw', 'roh'])) {
        return this._bool(facts.edible_raw === true, YES, NO);
      }
      if (this._has(q, ['sommer', 'summer', 'warm'])) {
        const seasons = Array.isArray(facts.season) ? facts.season : [facts.season];
        return this._bool(seasons.some(s => s && s.includes('Sommer')), YES, NO);
      }
      if (this._has(q, ['in deutschland', 'germany', 'deutschland', 'bekannt', 'haufig', 'common'])) {
        return this._bool(facts.common_in_germany === true, YES, NO);
      }
    }

    // ===== Obst =====
    if (cat === 'obst') {
      if (this._has(q, ['baum', 'tree', 'auf einem baum', 'on a tree'])) {
        return this._bool(facts.grows_on === 'Baum', YES, NO);
      }
      if (this._has(q, ['strauch', 'bush', 'beere', 'berry'])) {
        return this._bool(facts.grows_on === 'Strauch' || facts.grows_on === 'Busch', YES, NO);
      }
      if (this._has(q, ['sus', 'sweet', 'zucker', 'sugar'])) {
        return this._bool(facts.taste && facts.taste.includes('süß'), YES, NO);
      }
      if (this._has(q, ['sauer', 'sour', 'acid'])) {
        return this._bool(facts.taste && facts.taste.includes('sauer'), YES, NO);
      }
      if (this._has(q, ['tropisch', 'tropical', 'exotisch', 'exotic'])) {
        return this._bool(facts.tropical === true, YES, NO);
      }
      if (this._has(q, ['rot', 'red'])) {
        const colors = Array.isArray(facts.color) ? facts.color : [facts.color];
        return this._bool(colors.some(c => c && c.includes('rot')), YES, NO);
      }
      if (this._has(q, ['gelb', 'yellow'])) {
        const colors = Array.isArray(facts.color) ? facts.color : [facts.color];
        return this._bool(colors.some(c => c && c.includes('gelb')), YES, NO);
      }
      if (this._has(q, ['in deutschland', 'germany', 'heimisch', 'local', 'einheimisch'])) {
        return this._bool(facts.common_in_germany === true, YES, NO);
      }
    }

    // Kein Pattern gefunden
    return { answer: DUNNO, type: 'unclear' };
  },

  _has(question, keywords) {
    return keywords.some(kw => question.includes(kw));
  },

  _bool(condition, yes, no) {
    return condition
      ? { answer: yes, type: 'yes' }
      : { answer: no, type: 'no' };
  }
};
