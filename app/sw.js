// sw.js — Service Worker (Cache-First für App + Daten, Network für API)

const CACHE_NAME = 'dingeraten-v1';

const APP_SHELL = [
  './index.html',
  './css/main.css',
  './js/state.js',
  './js/i18n.js',
  './js/data-loader.js',
  './js/game-engine.js',
  './js/openai-client.js',
  './js/qa-engine.js',
  './js/speech.js',
  './js/app.js',
  './locales/de.json',
  './locales/en.json',
  './manifest.json'
];

const DATA_FILES = [
  '../data/laender.json',
  '../data/hauptstaedte.json',
  '../data/gemuese.json',
  '../data/obst.json',
  '../data/tiere.json'
];

// Install: Alle App-Dateien und Daten cachen
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll([...APP_SHELL, ...DATA_FILES]);
    }).then(() => self.skipWaiting())
  );
});

// Activate: Alte Caches löschen
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Fetch: OpenAI immer online, alles andere Cache-First
self.addEventListener('fetch', event => {
  const url = event.request.url;

  // OpenAI API: niemals cachen
  if (url.includes('openai.com') || url.includes('api.openai')) {
    event.respondWith(fetch(event.request));
    return;
  }

  // flagcdn.com Bilder: Network-First mit Cache-Fallback
  if (url.includes('flagcdn.com')) {
    event.respondWith(
      fetch(event.request)
        .then(resp => {
          if (resp.ok) {
            const clone = resp.clone();
            caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
          }
          return resp;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  // Alles andere: Cache-First
  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request))
  );
});
