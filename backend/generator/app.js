const cfg = window.CONFIG;

document.documentElement.style.setProperty('--bg', cfg.theme.background);
document.documentElement.style.setProperty('--text', cfg.theme.text);

function tick() {
  const now = new Date();
  document.getElementById("time").innerText =
    now.toLocaleTimeString();
  changeFrame(now);
}


function toMinutes(timeStr) {
  const [h, m] = timeStr.split(":").map(Number);
  return h * 60 + m;
}

function nowInMinutes() {
  const now = new Date();
  return now.getHours() * 60 + now.getMinutes();
}

function changeFrame() {
  // const now = new Date();
  curr_frame = null;
  timeframes = cfg.timeframes;

  nowMinutes = nowInMinutes()
  for (const frame of timeframes){

    if (nowMinutes >= toMinutes(frame.start) && nowMinutes <= toMinutes(frame.end)){
        document.getElementById("frame-name").innerText = frame.name;
      }
  }
}

setInterval(tick, cfg.refresh_interval);
tick();
