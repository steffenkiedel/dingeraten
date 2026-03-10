// app.js — Initialisierung, Navigation, Event-Listener

// ===== Screen-Navigation =====
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active', 'screen-enter'));
  const screen = document.getElementById(id);
  screen.classList.add('active', 'screen-enter');
}

// ===== Sprachsteuerung =====
async function switchLanguage(lang) {
  GameState.saveLanguage(lang);
  await i18n.load(lang);
  i18n.applyAll();
  updateLangButtons(lang);
}

function updateLangButtons(lang) {
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  document.querySelectorAll('[data-settings-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.settingsLang === lang);
  });
}

// ===== Setup-Screen Steuerung =====
function updateStartButton() {
  const btn = document.getElementById('btn-start-game');
  btn.disabled = !(GameState.category && GameState.difficulty);
}

// ===== Game starten =====
async function startGame() {
  const item = await GameEngine.selectItem(GameState.category, GameState.getEffectiveDifficulty());
  if (!item) {
    alert(i18n.t('errors.loadFailed'));
    return;
  }

  GameState.reset();
  GameState.currentItem = item;
  GameState.gameStatus = 'playing';

  // Category Badge
  const catEmojis = { laender: '🌍', hauptstaedte: '🏛️', gemuese: '🥦', obst: '🍎', tiere: '🦁' };
  const badge = document.getElementById('game-category-badge');
  badge.textContent = catEmojis[GameState.category] + ' ' + i18n.t(`setup.categories.${GameState.category}`);

  // Counter reset
  updateCounter();

  // History leeren
  const history = document.getElementById('qa-history');
  history.innerHTML = `<div id="qa-empty" class="qa-empty">
    <span class="emoji">🤔</span>
    <p>${i18n.t('game.inputPlaceholder').replace(' ...', '!')}</p>
  </div>`;

  // Input leeren
  document.getElementById('game-input').value = '';
  document.getElementById('btn-send').disabled = true;

  showScreen('screen-game');
}

function updateCounter() {
  const el = document.getElementById('game-question-counter');
  el.textContent = `${GameState.questionCount} / ${GameState.maxQuestions}`;
}

// ===== Q&A-History rendern =====
function addQABubbles(question, answer, type) {
  const history = document.getElementById('qa-history');

  // Empty-State entfernen
  const empty = document.getElementById('qa-empty');
  if (empty) empty.remove();

  const item = document.createElement('div');
  item.className = 'qa-item';
  item.innerHTML = `
    <div class="bubble bubble-question">${escapeHtml(question)}</div>
    <div class="bubble bubble-answer ${type}">${escapeHtml(answer)}</div>
  `;
  history.appendChild(item);
  history.scrollTop = history.scrollHeight;
}

function showThinking() {
  const history = document.getElementById('qa-history');
  const empty = document.getElementById('qa-empty');
  if (empty) empty.remove();

  const el = document.createElement('div');
  el.id = 'thinking-indicator';
  el.className = 'qa-item';
  el.innerHTML = `<div class="thinking"><span></span><span></span><span></span></div>`;
  history.appendChild(el);
  history.scrollTop = history.scrollHeight;
  return el;
}

function removeThinking() {
  const el = document.getElementById('thinking-indicator');
  if (el) el.remove();
}

function addHintBubble(hint) {
  const history = document.getElementById('qa-history');
  const empty = document.getElementById('qa-empty');
  if (empty) empty.remove();

  const item = document.createElement('div');
  item.className = 'qa-item';
  item.innerHTML = `<div class="bubble bubble-answer hint">💡 ${escapeHtml(hint)}</div>`;
  history.appendChild(item);
  history.scrollTop = history.scrollHeight;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ===== Frage senden =====
async function sendQuestion() {
  const input = document.getElementById('game-input');
  const question = input.value.trim();
  if (!question) return;

  input.value = '';
  document.getElementById('btn-send').disabled = true;

  if (GameState.questionCount >= GameState.maxQuestions) {
    openGuessDialog();
    return;
  }

  const thinking = showThinking();
  let result;
  try {
    result = await QAEngine.answer(question, GameState.currentItem, GameState.qaHistory, GameState.language);
  } catch (e) {
    console.error(e);
    result = { answer: i18n.t('errors.apiError'), type: 'unclear' };
  }
  removeThinking();

  GameState.addQA(question, result.answer, result.type);
  addQABubbles(question, result.answer, result.type);
  updateCounter();

  if (GameState.questionCount >= GameState.maxQuestions) {
    setTimeout(openGuessDialog, 800);
  }
}

// ===== Tipp =====
function showHint() {
  const hint = GameState.nextHint();
  if (!hint) {
    addHintBubble(i18n.t('game.noMoreHints'));
  } else {
    addHintBubble(hint);
  }
}

// ===== Guess Dialog =====
function openGuessDialog() {
  document.getElementById('guess-input').value = '';
  document.getElementById('overlay-guess').classList.add('active');
  document.getElementById('guess-input').focus();
}

function closeGuessDialog() {
  document.getElementById('overlay-guess').classList.remove('active');
}

function checkGuess() {
  const input = document.getElementById('guess-input').value.trim();
  if (!input) return;

  const correct = GameEngine.checkAnswer(input, GameState.currentItem, GameState.language);
  closeGuessDialog();

  if (correct) {
    GameState.gameStatus = 'won';
    GameState.onCorrectAnswer();
    showResult(true);
  } else {
    // Falsche Antwort als QA-Eintrag zeigen
    const wrongMsg = i18n.t('answers.wrong');
    addQABubbles(input, wrongMsg, 'wrong');
    GameState.addQA(input, wrongMsg, 'wrong');
    updateCounter();
  }
}

// ===== Result-Screen =====
function showResult(won) {
  const item = GameState.currentItem;
  const lang = GameState.language;

  document.getElementById('result-status').textContent = won
    ? i18n.t('result.wonTitle')
    : i18n.t('result.lostTitle');

  // Bild: Flagge für Länder, Emoji sonst
  const flagEl = document.getElementById('result-flag');
  const imageEl = document.getElementById('result-image');
  if (item.flag_url) {
    flagEl.src = item.flag_url;
    flagEl.classList.remove('hidden');
    imageEl.classList.add('hidden');
  } else {
    imageEl.textContent = item.emoji || '❓';
    imageEl.classList.remove('hidden');
    flagEl.classList.add('hidden');
  }

  document.getElementById('result-name').textContent = item.name[lang] || item.name.de;
  document.getElementById('result-description').textContent = item.description[lang] || item.description.de;
  document.getElementById('result-fun-fact').textContent = item.fun_fact[lang] || item.fun_fact.de;

  const statsEl = document.getElementById('result-stats');
  if (GameState.hintsUsed > 0) {
    statsEl.textContent = i18n.t('result.questionsWithHints', { n: GameState.questionCount, h: GameState.hintsUsed });
  } else {
    statsEl.textContent = i18n.t('result.questions', { n: GameState.questionCount });
  }

  showScreen('screen-result');
}

// ===== Settings =====
function openSettings() {
  const overlay = document.getElementById('overlay-settings');
  const keyInput = document.getElementById('settings-api-key');
  keyInput.value = GameState.apiKey || '';
  document.getElementById('key-status').textContent = '';
  updateLangButtons(GameState.language);
  overlay.classList.add('active');
}

function closeSettings() {
  document.getElementById('overlay-settings').classList.remove('active');
}

async function testApiKey() {
  const key = document.getElementById('settings-api-key').value.trim();
  const statusEl = document.getElementById('key-status');
  statusEl.textContent = '...';
  statusEl.className = 'key-status';

  const valid = await OpenAIClient.testKey(key);
  statusEl.textContent = valid ? i18n.t('settings.apiKeyValid') : i18n.t('settings.apiKeyInvalid');
  statusEl.className = 'key-status ' + (valid ? 'valid' : 'invalid');
}

function saveSettings() {
  const key = document.getElementById('settings-api-key').value.trim();
  GameState.saveApiKey(key || null);
  closeSettings();
}

// ===== Init =====
async function init() {
  GameState.loadLanguage();
  GameState.loadApiKey();

  await i18n.load(GameState.language);
  i18n.applyAll();
  updateLangButtons(GameState.language);

  // Daten vorladen
  DataLoader.preload();
}

// ===== Event-Listener =====
document.addEventListener('DOMContentLoaded', () => {
  init();

  // Start-Screen
  document.getElementById('btn-play').addEventListener('click', () => showScreen('screen-setup'));
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.addEventListener('click', () => switchLanguage(btn.dataset.lang));
  });

  // Setup-Screen
  document.getElementById('btn-back-start').addEventListener('click', () => showScreen('screen-start'));
  document.getElementById('btn-settings').addEventListener('click', openSettings);

  document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.category-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      GameState.category = card.dataset.category;
      updateStartButton();
    });
  });

  document.querySelectorAll('.difficulty-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.difficulty-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      GameState.difficulty = parseInt(btn.dataset.difficulty);
      updateStartButton();
    });
  });

  document.getElementById('btn-start-game').addEventListener('click', startGame);

  // Game-Screen
  document.getElementById('btn-back-setup').addEventListener('click', () => {
    if (confirm(GameState.language === 'de' ? 'Spiel abbrechen?' : 'Quit this game?')) {
      showScreen('screen-setup');
    }
  });

  const gameInput = document.getElementById('game-input');
  gameInput.addEventListener('input', () => {
    document.getElementById('btn-send').disabled = !gameInput.value.trim();
  });
  gameInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') sendQuestion();
  });

  document.getElementById('btn-send').addEventListener('click', sendQuestion);
  document.getElementById('btn-hint').addEventListener('click', showHint);
  document.getElementById('btn-know').addEventListener('click', openGuessDialog);

  // Guess Dialog
  document.getElementById('btn-guess-cancel').addEventListener('click', closeGuessDialog);
  document.getElementById('btn-guess-submit').addEventListener('click', checkGuess);
  document.getElementById('guess-input').addEventListener('keydown', e => {
    if (e.key === 'Enter') checkGuess();
  });
  document.getElementById('overlay-guess').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeGuessDialog();
  });

  // Settings
  document.getElementById('btn-test-key').addEventListener('click', testApiKey);
  document.getElementById('btn-settings-save').addEventListener('click', saveSettings);
  document.querySelectorAll('[data-settings-lang]').forEach(btn => {
    btn.addEventListener('click', () => switchLanguage(btn.dataset.settingsLang));
  });
  document.getElementById('overlay-settings').addEventListener('click', e => {
    if (e.target === e.currentTarget) closeSettings();
  });

  // Result-Screen
  document.getElementById('btn-play-again').addEventListener('click', () => {
    startGame();
  });
  document.getElementById('btn-new-category').addEventListener('click', () => {
    GameState.sessionCorrect = 0;
    GameState.currentProgressLevel = 1;
    showScreen('screen-setup');
  });

  // Mikrofon
  document.getElementById('btn-mic').addEventListener('click', () => {
    SpeechInput.toggle(
      (text) => {
        document.getElementById('game-input').value = text;
        document.getElementById('btn-send').disabled = !text.trim();
      },
      GameState.language
    );
  });
});
