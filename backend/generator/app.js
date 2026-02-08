const cfg = window.CONFIG;

document.documentElement.style.setProperty('--bg', cfg.theme.background);
document.documentElement.style.setProperty('--text', cfg.theme.text);

function tick() {
  const now = new Date();
  document.getElementById("time").innerText =
    now.toLocaleTimeString();
}

setInterval(tick, cfg.refresh_interval);
tick();