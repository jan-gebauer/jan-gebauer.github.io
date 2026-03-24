// ── COUNTER ──────────────────────────────────────────
let count = 0;

function adjustCounter(n) {
  count += n;
  const el = document.getElementById('counter-val');
  el.textContent = count;
  el.style.color = count < 0 ? 'var(--pink)' : count === 0 ? 'var(--dark)' : 'var(--blue)';
  el.classList.remove('pop');
  void el.offsetWidth;
  el.classList.add('pop');
  setTimeout(() => el.classList.remove('pop'), 200);
}

function resetCounter() {
  count = 0;
  const el = document.getElementById('counter-val');
  el.textContent = '0';
  el.style.color = 'var(--dark)';
}

// ── DICE ─────────────────────────────────────────────
function updateDicePreview() {
  const n = parseInt(document.getElementById('dice-count').value);
  const display = document.getElementById('dice-display');
  display.innerHTML = '';
  for (let i = 0; i < n; i++) {
    const d = document.createElement('span');
    d.className = 'die';
    d.textContent = '?';
    display.appendChild(d);
  }
  document.getElementById('dice-total').textContent = 'Ready to roll!';
}

function rollDice() {
  const n     = parseInt(document.getElementById('dice-count').value);
  const sides = parseInt(document.getElementById('dice-sides').value);
  const display = document.getElementById('dice-display');
  const totalEl = document.getElementById('dice-total');

  display.innerHTML = '';
  const results = [];
  for (let i = 0; i < n; i++) {
    const val = Math.floor(Math.random() * sides) + 1;
    results.push(val);
    const die = document.createElement('span');
    die.className = 'die rolling';
    die.textContent = val;
    display.appendChild(die);
    die.style.animationDelay = (i * 60) + 'ms';
  }

  const total = results.reduce((a, b) => a + b, 0);
  setTimeout(() => {
    if (n === 1) {
      totalEl.textContent = `You rolled a ${total}! ${total === sides ? '🎉' : ''}`;
    } else {
      totalEl.textContent = `Total: ${total} (${results.join(' + ')})`;
    }
  }, 400);
}
