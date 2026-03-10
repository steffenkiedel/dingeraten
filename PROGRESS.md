# Dingeraten — Fortschritt

## Status: 🟡 In Entwicklung

## Phasen

| Phase | Status | Beschreibung |
|---|---|---|
| 1 — Fundament | ✅ | index.html, CSS, JS-Module, Service Worker |
| 2 — Daten | ✅ | 5 Kategorien mit je 10-30 Items |
| 3 — Deploy | ⬜ | GitHub Pages |

## Fertig
- Projektstruktur (WAT Framework)
- Alle HTML-Screens (Start, Setup, Game, Result)
- CSS (responsive, Animationen, Dark/Light kompatibel)
- state.js, i18n.js, data-loader.js, game-engine.js
- qa-engine.js (Online/Offline Q&A Routing)
- openai-client.js (GPT-4o-mini)
- speech.js (Web Speech API)
- app.js (Navigation, Event-Listener)
- manifest.json + sw.js (PWA)
- Lokalisierung DE/EN (locales/)
- Daten: laender.json (30 Länder), tiere.json (30 Tiere)
- Daten: gemuese.json, obst.json, hauptstaedte.json

## Offen
- [ ] PWA-Icons generieren (192px + 512px)
- [ ] GitHub Repository erstellen + Pages aktivieren
- [ ] Mehr Items pro Kategorie (Ziel: 50-80)
- [ ] tools/generate_items.py für Batch-Generierung

## Bekannte Probleme
- Noch keine echten PWA-Icons (Platzhalter nötig)
- Service Worker cached Bilder von flagcdn.com noch nicht beim ersten Start

## Technologie
- HTML/CSS/JS (kein Framework)
- OpenAI API (gpt-4o-mini) für Online-Q&A
- Keyword-Matching für Offline-Q&A
- Web Speech API für Mikrofon-Eingabe
- GitHub Pages für Hosting
