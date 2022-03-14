const Selector = (q) => document.querySelectorAll(q);
const Creator = (...t) => t.map((e) => document.createElement(e));

function EffectEvent(e) {
  let x = e.pageX - e.target.offsetLeft;
  let y = e.pageY - e.target.offsetTop;
  e.target.style.setProperty("--x", `${x}px`);
  e.target.style.setProperty("--y", `${y}px`);
}

Selector("button").forEach((btn) => {
  btn.addEventListener("mousemove", EffectEvent);
  btn.addEventListener("mousedown", EffectEvent);
});