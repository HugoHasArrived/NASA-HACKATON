from flask import Flask, render_template_string, jsonify
import os

app = Flask(__name__)

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#07111f">
<title>Junior Astronaut Mission Trainer</title>
<style>
:root {
--bg:#06101d;
--panel:#0d1b2c;
--edge:#29435e;
--text:#eff7ff;
--muted:#9eb4cb;
--cyan:#65e8df;
--blue:#77aaff;
--green:#7ce4a8;
--yellow:#ffd166;
--red:#ff7185}
* {
box-sizing:border-box}
body {
margin:0;
background:radial-gradient(ellipse at 50% -20%,#1a3554 0,#081525 48%,#040912 100%);
color:var(--text);
font:15px/1.5 system-ui,Segoe UI,sans-serif;
min-height:100vh}
button {
font:inherit;
cursor:pointer;
color:var(--text);
border:1px solid #35536f;
background:#152b42;
padding:10px 13px;
border-radius:11px;
font-weight:750;
transition:.14s}
button:hover:not(:disabled) {
transform:translateY(-1px);
border-color:var(--cyan);
background:#1b3a55}
button:focus-visible {
outline:3px solid var(--cyan);
outline-offset:2px}
button:disabled {
opacity:.38;
cursor:not-allowed}
.primary {
color:#061421;
background:linear-gradient(120deg,#67eee2,#76aaff);
border:0}
.wrap {
width:min(1360px,100%);
padding:20px;
margin:auto}
.topbar {
display:flex;
justify-content:space-between;
align-items:center;
gap:15px;
flex-wrap:wrap;
margin-bottom:18px}
.brand {
display:flex;
align-items:center;
gap:12px}
.logo {
width:48px;
height:48px;
display:grid;
place-items:center;
border-radius:15px;
background:linear-gradient(135deg,#4be2d7,#5687ff);
box-shadow:0 0 35px #42dcd733;
font-size:26px}
.eyebrow {
font-size:10px;
letter-spacing:2px;
text-transform:uppercase;
font-weight:900;
color:var(--cyan)}
.title {
font-weight:950;
font-size:clamp(20px,3vw,30px);
letter-spacing:-.7px;
line-height:1.15}
.muted {
color:var(--muted)}
.small {
font-size:12px}
.tag {
display:inline-flex;
align-items:center;
gap:6px;
border:1px solid var(--edge);
border-radius:99px;
padding:6px 10px;
font-size:11px;
color:var(--muted);
white-space:nowrap}
.dot {
width:7px;
height:7px;
border-radius:50%;
background:var(--green)}
.layout {
display:grid;
grid-template-columns:minmax(0,1.5fr) minmax(285px,.8fr);
gap:16px;
align-items:start}
.stack {
display:grid;
gap:16px;
min-width:0}
.panel {
min-width:0;
background:linear-gradient(155deg,#112238f5,#0b1828f5);
border:1px solid var(--edge);
border-radius:18px;
padding:17px;
box-shadow:0 18px 50px #0005}
.panel h2 {
font-size:16px;
margin:0}
.head {
display:flex;
justify-content:space-between;
align-items:center;
gap:10px;
margin-bottom:12px}
.sub {
font-size:12px;
color:var(--muted);
margin-top:3px}
.scene {
height:285px;
border-radius:15px;
position:relative;
overflow:hidden;
border:1px solid #2e4c69;
margin-bottom:14px;
background:linear-gradient(#071327 0%,#172c4c 54%,#51485d 55%,#a17b6a 100%)}
.stars {
position:absolute;
inset:0;
background-image:radial-gradient(#fff 1px,transparent 1.6px),radial-gradient(#9ceaff 1px,transparent 1.6px);
background-size:53px 49px,83px 67px;
background-position:5px 3px,22px 19px;
opacity:.8}
.planet {
position:absolute;
width:112px;
height:112px;
right:12%;
top:22px;
border-radius:50%;
background:linear-gradient(135deg,#e9f4f7,#6f98b6 60%,#344c70);
box-shadow:0 0 40px #8bd8ff55}
.terrain {
position:absolute;
left:-5%;
right:-5%;
bottom:-16px;
height:120px;
background:repeating-radial-gradient(ellipse at 40% 20%,#b08b72 0 2px,#816b67 3px 5px,#665968 6px 9px);
clip-path:polygon(0 24%,13% 9%,28% 23%,45% 4%,63% 25%,80% 10%,100% 20%,100% 100%,0 100%)}
.base {
position:absolute;
bottom:53px;
left:30%;
width:190px;
height:90px;
filter:drop-shadow(0 8px 12px #0007)}
.hab {
position:absolute;
bottom:0;
left:26px;
width:132px;
height:65px;
background:linear-gradient(#dce8ef,#7891a2);
border:3px solid #f0f8ff;
border-radius:40px 40px 8px 8px;
box-shadow:0 0 20px #7eeaff33}
.hab:before {
content:"";
position:absolute;
left:12px;
right:12px;
top:12px;
height:15px;
background:repeating-linear-gradient(90deg,#16364e 0 19px,#9de7ed 20px 23px);
border-radius:4px}
.hab:after {
content:"HABITAT 01";
position:absolute;
bottom:5px;
left:0;
right:0;
text-align:center;
color:#172a3c;
font-size:9px;
font-weight:900;
letter-spacing:1px}
.solar {
position:absolute;
bottom:10px;
left:-52px;
width:66px;
height:45px;
background:repeating-linear-gradient(90deg,#153d79 0 14px,#4d9bd1 15px 16px);
border:2px solid #8bc5ee;
transform:skewY(-12deg)}
.solar:after {
content:"";
position:absolute;
top:20px;
left:0;
right:0;
border-top:2px solid #8bc5ee}
.antenna {
position:absolute;
bottom:65px;
left:90px;
height:35px;
border-left:3px solid #b8cbd9}
.antenna:after {
content:"";
position:absolute;
width:18px;
height:18px;
left:-10px;
top:-7px;
border:2px solid #b8cbd9;
border-radius:50%}
.scene-label,.scene-state {
position:absolute;
background:#07111fd9;
border:1px solid #49617b;
border-radius:8px;
padding:6px 9px;
font-size:10px;
font-weight:900;
letter-spacing:1px}
.scene-label {
left:12px;
top:12px}
.scene-state {
right:12px;
bottom:12px}
.guide-strip {
display:flex;
align-items:center;
gap:12px;
padding:12px;
margin:0 0 13px;
border:1px solid #397b8a;
border-radius:14px;
background:linear-gradient(110deg,#103748,#10243a 70%);
box-shadow:0 8px 30px #00d7ff0b}
.guide-number {
display:grid;
place-items:center;
flex:0 0 34px;
height:34px;
border-radius:11px;
background:linear-gradient(135deg,#7ff5e8,#77aaff);
color:#071522;
font-weight:1000;
font-size:15px}
.guide-strip div {
display:grid;
gap:2px;
flex:1}
.guide-strip strong {
font-size:12px;
color:#7ff5e8}
.guide-strip span:not(.guide-number) {
font-size:11px;
color:#c5d9e9}
.guide-strip button {
padding:7px 10px;
font-size:10px;
white-space:nowrap}
.scene:after {
content:"";
position:absolute;
inset:0;
pointer-events:none;
background:linear-gradient(180deg,#08152622,transparent 42%,#070c1833);
box-shadow:inset 0 0 50px #03081466}
.planet {
animation:planetGlow 5s ease-in-out infinite alternate}
.hab {
box-shadow:0 0 22px #7eeaff33,0 0 55px #7eeaff12}
.solar {
filter:drop-shadow(0 0 5px #5baeff55)}
.action {
position:relative;
overflow:hidden}
.action:before {
content:"";
position:absolute;
inset:0;
background:linear-gradient(125deg,#77f5e90a,transparent 60%);
pointer-events:none}
.action:not(:disabled):hover {
transform:translateY(-3px);
box-shadow:0 12px 24px #0004}
.resource {
transition:border-color .2s,transform .2s}
.resource:hover {
border-color:#527c9b;
transform:translateY(-1px)}
.fill {
box-shadow:0 0 10px currentColor}
.scene-label {
z-index:2}
.scene-state {
z-index:2}
.guide-strip {
position:relative;
z-index:1}
@keyframes planetGlow {
from {
filter:brightness(.95);
box-shadow:0 0 30px #8bd8ff33}
to {
filter:brightness(1.12);
box-shadow:0 0 52px #8bd8ff66}
}
.brief {
padding:12px 13px;
border:1px solid #2a5669;
background:#0c2937;
border-radius:12px;
margin-bottom:13px;
font-size:12px;
color:#c9f7f4}
.brief b {
color:#fff}
.steps {
display:grid;
grid-template-columns:repeat(3,minmax(0,1fr));
gap:8px;
margin-bottom:17px}
.step {
padding:10px;
border-radius:11px;
background:#0a1727;
border:1px solid #243d55;
font-size:11px;
color:var(--muted)}
.step b {
display:block;
color:var(--cyan);
font-size:10px;
letter-spacing:1px;
margin-bottom:3px}
.resources {
display:grid;
grid-template-columns:repeat(3,minmax(0,1fr));
gap:9px}
.resource {
background:#091626;
border:1px solid #243b53;
border-radius:12px;
padding:11px;
min-width:0}
.rhead {
display:flex;
justify-content:space-between;
gap:5px;
color:var(--muted);
font-size:11px}
.rval {
font-size:23px;
font-weight:900;
letter-spacing:-.5px;
margin:5px 0}
.unit {
font-size:10px;
color:var(--muted);
font-weight:600}
.bar {
height:6px;
border-radius:99px;
background:#25384d;
overflow:hidden}
.fill {
height:100%;
border-radius:99px;
background:var(--green);
transition:width .25s}
.fill.warn {
background:var(--yellow)}
.fill.bad {
background:var(--red)}
.rnote {
font-size:10px;
color:var(--muted);
margin-top:6px}
.section-title {
font-size:15px;
font-weight:900;
margin:19px 0 4px}
.section-desc {
font-size:11px;
color:var(--muted);
margin-bottom:10px}
.recommend {
border:1px solid #3a5d75;
background:#10283c;
border-radius:12px;
padding:12px;
font-size:12px;
margin-bottom:10px}
.recommend b {
color:var(--cyan)}
.actions {
display:grid;
grid-template-columns:repeat(2,minmax(0,1fr));
gap:9px}
.action {
min-height:116px;
text-align:left;
padding:12px;
background:#0d1e31;
border-color:#29445e;
display:flex;
flex-direction:column;
gap:4px}
.actiontop {
display:flex;
align-items:center;
gap:8px}
.ico {
font-size:20px}
.aname {
font-size:12px;
font-weight:900}
.adesc {
font-size:11px;
line-height:1.4;
color:var(--muted);
font-weight:500}
.cost {
font-size:10px;
color:#b7d7ed;
margin-top:auto;
padding-top:5px}
.cost.low {
color:var(--red)}
.metric {
display:flex;
justify-content:space-between;
gap:12px;
padding:9px 0;
border-bottom:1px solid #22394f;
font-size:12px}
.metric:last-child {
border-bottom:0}
.metric strong {
font-size:13px}
.good {
color:var(--green)}
.warning {
color:var(--yellow)}
.danger {
color:var(--red)}
.objective {
display:flex;
gap:9px;
align-items:flex-start;
margin:13px 0}
.check {
width:20px;
height:20px;
border-radius:6px;
border:1px solid #4a6a85;
display:grid;
place-items:center;
flex-shrink:0;
font-size:12px;
font-weight:900}
.check.done {
background:var(--green);
border-color:var(--green);
color:#052117}
.objective b {
font-size:12px}
.objective p {
font-size:11px;
color:var(--muted);
margin:2px 0 0}
.log {
max-height:250px;
overflow:auto;
display:grid;
gap:8px}
.entry {
padding:9px 10px;
border-left:3px solid #4b84a8;
border-radius:0 9px 9px 0;
background:#091727;
font-size:11px;
color:#d0dfed}
.entry.good {
border-color:var(--green)}
.entry.warn {
border-color:var(--yellow)}
.entry.bad {
border-color:var(--red)}
.logday {
font-size:9px;
color:#86a8c7;
font-weight:900;
letter-spacing:1px;
margin-bottom:3px}
.lesson {
font-size:12px;
color:#c9d9e8}
.lesson b {
color:var(--cyan)}
.footer {
display:flex;
justify-content:space-between;
gap:12px;
flex-wrap:wrap;
color:var(--muted);
font-size:10px;
padding:18px 3px}
.overlay {
position:fixed;
inset:0;
z-index:10;
display:grid;
place-items:center;
padding:16px;
background:#020712e8;
backdrop-filter:blur(9px);
overflow:auto}
.modal {
width:min(650px,100%);
padding:25px;
background:linear-gradient(150deg,#132942,#0a1728);
border:1px solid #3c5d7a;
border-radius:22px;
box-shadow:0 30px 100px #0009}
.modal h1 {
font-size:clamp(30px,5vw,44px);
line-height:1.05;
letter-spacing:-1px;
margin:10px 0}
.modal h3 {
margin:20px 0 6px}
.modal p {
font-size:13px}
.choices {
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
margin:12px 0}
.choice {
text-align:left;
padding:14px;
background:#0b1a2b}
.choice.selected {
border-color:var(--cyan);
box-shadow:inset 0 0 0 1px var(--cyan);
background:#143247}
.choice .pi {
font-size:27px}
.choice small {
display:block;
color:var(--muted);
font-weight:500;
margin-top:4px}
.note {
border:1px solid #2b5367;
background:#0c2937;
border-radius:11px;
padding:11px;
font-size:12px;
color:#c9f7f4}
.modal-buttons {
display:flex;
gap:8px;
margin-top:15px}
.modal-buttons button {
flex:1}
.hidden {
display:none!important}
.toast {
position:fixed;
z-index:20;
left:50%;
bottom:20px;
transform:translateX(-50%);
width:max-content;
max-width:90vw;
padding:11px 16px;
border-radius:12px;
background:#e8faff;
color:#061421;
font-size:12px;
font-weight:900;
box-shadow:0 12px 40px #0009;
text-align:center}
@media(max-width:900px) {
.layout {
grid-template-columns:1fr}
.sidecol {
grid-template-columns:repeat(2,minmax(0,1fr))}
.sidecol .panel:last-child {
grid-column:1/-1}
}
@media(max-width:560px) {
.wrap {
padding:11px}
.panel {
padding:13px}
.resources {
grid-template-columns:repeat(2,minmax(0,1fr))}
.steps {
grid-template-columns:1fr}
.step {
display:flex;
gap:8px;
align-items:center}
.step b {
min-width:54px;
margin:0}
.sidecol {
grid-template-columns:1fr}
.sidecol .panel:last-child {
grid-column:auto}
.scene {
height:225px}
.guide-strip {
align-items:flex-start;
flex-wrap:wrap}
.guide-strip div {
min-width:150px}
.guide-strip button {
margin-left:46px}
.base {
left:25%;
transform:scale(.85);
transform-origin:bottom left}
.choices {
grid-template-columns:1fr}
.modal {
padding:19px}
.actions {
grid-template-columns:1fr 1fr}
.action {
min-height:135px;
padding:10px}
.title {
font-size:20px}
}

.guide-strip{display:flex;align-items:center;gap:12px;padding:12px;margin:0 0 13px;border:1px solid #397b8a;border-radius:14px;background:linear-gradient(110deg,#103748,#10243a 70%);box-shadow:0 8px 30px #00d7ff0b;position:relative;z-index:1}.guide-number{display:grid;place-items:center;flex:0 0 34px;height:34px;border-radius:11px;background:linear-gradient(135deg,#7ff5e8,#77aaff);color:#071522;font-weight:1000;font-size:15px}.guide-strip div{display:grid;gap:2px;flex:1}.guide-strip strong{font-size:12px;color:#7ff5e8}.guide-strip span:not(.guide-number){font-size:11px;color:#c5d9e9}.guide-strip button{padding:7px 10px;font-size:10px;white-space:nowrap}.planet{animation:planetGlow 5s ease-in-out infinite alternate}.action:not(:disabled):hover{transform:translateY(-3px);box-shadow:0 12px 24px #0004}@keyframes planetGlow{from{filter:brightness(.95);box-shadow:0 0 30px #8bd8ff33}to{filter:brightness(1.12);box-shadow:0 0 52px #8bd8ff66}}

.stars{animation:starDrift 32s linear infinite}
.planet{border:1px solid #d5f5ff66;overflow:hidden}
.planet:after{content:"";position:absolute;inset:0;border-radius:50%;background:linear-gradient(115deg,transparent 28%,#ffffff30 48%,transparent 63%);transform:translateX(-100%);animation:planetShine 9s ease-in-out infinite}
.hab{background:linear-gradient(180deg,#f0fbff,#92aabd 62%,#647f91)}
.hab:before{box-shadow:0 0 12px #80edff77}
.antenna:after{box-shadow:0 0 12px #6ff7e8;animation:beacon 2s ease-in-out infinite alternate}
.scene-state{box-shadow:0 0 16px #0004}
@keyframes starDrift{from{background-position:5px 3px,22px 19px}to{background-position:58px 52px,105px 86px}}
@keyframes planetShine{0%,55%{transform:translateX(-100%)}80%,100%{transform:translateX(100%)}}
@keyframes beacon{from{opacity:.45;box-shadow:0 0 5px #6ff7e8}to{opacity:1;box-shadow:0 0 18px #6ff7e8}}
</style>
</head>
<body>
<div class="wrap">
<header class="topbar">
<div class="brand">
<div class="logo">🚀</div>
<div>
<div class="eyebrow">STEM FIELD SIMULATOR</div>
<div class="title">JUNIOR ASTRONAUT <span style="color:var(--cyan)">MISSION TRAINER</span>
</div>
</div>
</div>
<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
<span class="tag">
<span class="dot">
</span>
<span id="headerStatus">READY FOR TRAINING</span>
</span>
<button id="helpBtn">❔ Help</button>
<button id="restartBtn">↻ Restart</button>
</div>
</header>
<div class="layout">
<main class="stack">
<section class="panel">
<div class="brief">
<b>YOUR MISSION:</b> Keep your crew safe for 12 days. Pick one action, check its cost, then watch how supplies change. You do not need to click every action.</div>
<div class="steps">
<div class="step">
<b>01 / CHOOSE</b>Pick an operation that helps your weakest resource.</div>
<div class="step">
<b>02 / CHECK</b>Each card shows what it costs.</div>
<div class="step">
<b>03 / SURVIVE</b>One action advances a day; supplies are used.</div>
</div>
<div class="head">
<div>
<h2 id="outpostTitle">Outpost overview</h2>
<div class="sub" id="planetSub">Select a destination to begin.</div>
</div>
<span class="tag" id="dayTag">DAY 1 / 12</span>
</div>
<div class="scene">
<div class="stars">
</div>
<div class="planet" id="planetArt">
</div>
<div class="terrain">
</div>
<div class="base">
<div class="solar">
</div>
<div class="antenna">
</div>
<div class="hab">
</div>
</div>
<div class="scene-label" id="sceneLabel">OUTPOST • STANDBY</div>
<div class="scene-state" id="sceneState">SYSTEMS CHECKING</div>
</div>
<div class="guide-strip" id="guideStrip"><span class="guide-number">1</span><div><strong>Beginner guide</strong><span>Read the suggested next step, then choose the matching action card.</span></div><button type="button" id="guideNext">Next tip</button></div>

<div class="head">
<div>
<h2>Resource dashboard</h2>
<div class="sub">Green = okay · Yellow = low · Red = urgent</div>
</div>
<span class="tag">LIVE STATUS</span>
</div>
<div class="resources" id="resources">
</div>
<div class="section-title">What should I do next?</div>
<div class="section-desc">Follow the recommendation, or choose another operation.</div>
<div class="recommend" id="recommendation">
<b>Suggested:</b> Start the mission to receive advice.</div>
<div class="actions" id="actions">
</div>
</section>
<section class="panel">
<div class="head">
<div>
<h2>Learning lab</h2>
<div class="sub">The science behind your choices</div>
</div>
<span class="tag">FIELD NOTES</span>
</div>
<div class="lesson" id="lesson">Your decisions affect the crew and outpost. Choose an operation to learn why it matters.</div>
</section>
</main>
<aside class="stack sidecol">
<section class="panel">
<div class="head">
<div>
<h2>Mission control</h2>
<div class="sub">Crew health and progress</div>
</div>
<span class="tag">CONTROL</span>
</div>
<div class="metric">
<span>Destination</span>
<strong id="worldMetric">Not selected</strong>
</div>
<div class="metric">
<span>Mission day</span>
<strong id="dayMetric">—</strong>
</div>
<div class="metric">
<span>Crew health</span>
<strong id="healthMetric">—</strong>
</div>
<div class="metric">
<span>Crew morale</span>
<strong id="moraleMetric">—</strong>
</div>
<div class="metric">
<span>Science points</span>
<strong id="scienceMetric">0</strong>
</div>
<div class="metric">
<span>Mission score</span>
<strong id="scoreMetric">0</strong>
</div>
<div class="metric">
<span>Current status</span>
<strong id="statusMetric">Awaiting launch</strong>
</div>
</section>
<section class="panel">
<div class="head">
<div>
<h2>Mission checklist</h2>
<div class="sub">Optional goals for a better score</div>
</div>
</div>
<div id="objectives">
</div>
</section>
<section class="panel">
<div class="head">
<div>
<h2>Mission log</h2>
<div class="sub">Latest events first</div>
</div>
<button id="clearLog" style="padding:5px 8px;font-size:10px">Clear</button>
</div>
<div class="log" id="log">
<div class="muted small">Launch your mission to begin.</div>
</div>
</section>
<section class="panel">
<h2 style="font-size:14px;margin-bottom:7px">Cadet tip</h2>
<div class="lesson" id="tip">Never let every supply become low at the same time. Small early adjustments are safer than emergency repairs.</div>
</section>
</aside>
</div>
<footer class="footer">
<span>Educational prototype • Not affiliated with or endorsed by NASA</span>
<span>Made for curiosity, planning, and learning through play</span>
</footer>
</div>
<div class="overlay" id="startOverlay">
<div class="modal">
<div class="eyebrow">MISSION BRIEFING // CADET TRAINING</div>
<h1>Could you keep a crew alive <span style="color:var(--cyan)">on another world?</span>
</h1>
<p class="muted">You are mission commander. Keep your outpost running, make smart trade-offs, and complete a 12-day training mission.</p>
<h3>1. Choose a destination</h3>
<p class="muted small" style="margin-top:0">First time playing? The Moon is a little easier to practice on.</p>
<div class="choices">
<button class="choice selected" data-world="Moon">
<span class="pi">🌕</span>
<br>
<b>The Moon</b>
<small>Long cold nights and no breathable air. Beginner-friendly.</small>
</button>
<button class="choice" data-world="Mars">
<span class="pi">🔴</span>
<br>
<b>Mars</b>
<small>Dust storms and trickier power management.</small>
</button>
</div>
<div class="note">
<b>How to win:</b> keep crew health above zero until day 12. Maintain oxygen, water, food, and power. Checklist goals improve your score.</div>
<div class="modal-buttons">
<button class="primary" id="launchBtn">LAUNCH MISSION →</button>
</div>
</div>
</div>
<div class="overlay hidden" id="helpOverlay">
<div class="modal">
<div class="eyebrow">CADET FIELD GUIDE</div>
<h1>How to play</h1>
<p>
<b>1. Read the resource cards.</b> Their colors show if a supply is healthy, low, or urgent.</p>
<p>
<b>2. Pick an operation.</b> Each card shows its effect and cost. Greyed-out cards need supplies you don't have.</p>
<p>
<b>3. One action = one day.</b> The crew uses oxygen, water, food, and power daily.</p>
<p>
<b>4. Use the recommendation.</b> It suggests an action based on your lowest supply.</p>
<p>
<b>5. Try again.</b> The mission log explains what happened so you can try a new strategy.</p>
<div class="note">This is a simplified educational simulation, not a precise spacecraft engineering model.</div>
<div class="modal-buttons">
<button class="primary" id="closeHelp">BACK TO MISSION</button>
</div>
</div>
</div>
<div class="overlay hidden" id="endOverlay">
<div class="modal">
<div class="eyebrow">MISSION DEBRIEF</div>
<h1 id="endTitle">Mission complete</h1>
<p id="endText" class="muted">
</p>
<div id="debriefStats">
</div>
<div class="modal-buttons">
<button class="primary" id="againBtn">FLY ANOTHER MISSION ↻</button>
</div>
</div>
</div>
<div id="toast" class="toast hidden" role="status" aria-live="polite">
</div>
<script>

const $=id=>document.getElementById(id);const resourceInfo=[{
key:'oxygen',name:'Oxygen',icon:'🫁',unit:'units',max:100,note:'Breathable air reserve'
}
,{
key:'water',name:'Water',icon:'💧',unit:'L',max:120,note:'Drinking and hygiene'
}
,{
key:'food',name:'Food',icon:'🥫',unit:'meals',max:100,note:'Crew food stores'
}
,{
key:'power',name:'Power',icon:'⚡',unit:'%',max:100,note:'Stored electrical energy'
}
,{
key:'shield',name:'Radiation shield',icon:'🛡️',unit:'%',max:100,note:'Shelter protection'
}
,{
key:'parts',name:'Spare parts',icon:'🔩',unit:'parts',max:30,note:'Repair supplies'
}
];const actions=[
{
id:'solar',icon:'☀️',name:'Tune solar array',short:'Recharge batteries and tune panels.',cost:{
parts:1
}
,goal:'solar',lesson:'Solar arrays make electricity, but stored energy helps when sunlight is weak. Tuning panels costs a spare part, so save some for repairs.',run:s=>{
s.power+=27;s.science+=2;s.score+=3;return 'Solar panels tuned. Stored power increased.'
}
}
,
{
id:'repair',icon:'🧰',name:'Repair life support',short:'Restore oxygen and protect crew health.',cost:{
parts:2,power:4
}
,goal:'repair',lesson:'Life-support equipment keeps air safe. Maintenance uses spare parts, so planning ahead is better than waiting for a breakdown.',run:s=>{
s.oxygen+=26;s.health+=4;s.score+=4;return 'Life-support equipment repaired. Oxygen reserves improved.'
}
}
,
{
id:'farm',icon:'🌱',name:'Grow food',short:'Produce meals and improve morale.',cost:{
water:7,power:6
}
,goal:'farm',lesson:'Growing food can reduce resupply needs, but plants need water, electricity, and care.',run:s=>{
s.food+=25;s.morale+=5;s.science+=2;s.score+=4;return 'Greenhouse harvest added food to the stores.'
}
}
,
{
id:'shield',icon:'🛡️',name:'Improve radiation shelter',short:'Increase protection for the crew.',cost:{
parts:3,power:3
}
,goal:'shield',lesson:'Radiation shielding is a design trade-off: stronger protection needs material and construction effort.',run:s=>{
s.shield+=20;s.score+=6;return 'Shelter shielding improved.'
}
}
,
{
id:'research',icon:'🔬',name:'Run science experiment',short:'Earn science points and mission score.',cost:{
power:8
}
,goal:'research',lesson:'Research creates knowledge but uses power and crew time. Balance discovery with survival needs.',run:s=>{
s.science+=9;s.score+=8;s.morale+=2;return 'Experiment completed. Science data recorded.'
}
}
,
{
id:'rest',icon:'🛌',name:'Rest and wellness check',short:'Recover crew health and morale.',cost:{
food:3,water:3
}
,lesson:'Crew health is part of the mission system. Rest, hydration, and morale help people perform under pressure.',run:s=>{
s.health+=12;s.morale+=12;s.score+=1;return 'Crew rested and completed a wellness check.'
}
}
,
{
id:'water',icon:'♻️',name:'Recycle water',short:'Recover water using stored power.',cost:{
power:7
}
,lesson:'Water recycling reduces resupply needs, but recovery systems use energy and need maintenance.',run:s=>{
s.water+=24;s.score+=2;return 'Water recovery system produced a fresh batch.'
}
}
,
{
id:'drill',icon:'🚨',name:'Practice emergency drill',short:'Build readiness and team confidence.',cost:{
power:3,food:2
}
,lesson:'Emergency drills help the crew practice what to do when alarms sound.',run:s=>{
s.morale+=5;s.score+=3;s.science+=1;return 'Emergency drill completed. Crew readiness improved.'
}
}
];let world='Moon',game=null,timer=null;function clamp(n,min=0,max=100){
return Math.max(min,Math.min(max,n))
}
function toast(t){
$('toast').textContent=t;$('toast').classList.remove('hidden');clearTimeout(timer);timer=setTimeout(()=>$('toast').classList.add('hidden'),2500)
}
function log(msg,type=''){
if(!game)return;game.log.unshift({
day:game.day,msg,type
}
);game.log=game.log.slice(0,40)
}
function launch(){
game={
world,day:1,oxygen:86,water:94,food:88,power:82,shield:65,parts:12,health:100,morale:85,science:0,score:0,goals:{
solar:false,repair:false,farm:false,shield:false,research:false
}
,log:[],ended:false
}
;if(world==='Mars')game.shield=58;$('startOverlay').classList.add('hidden');$('endOverlay').classList.add('hidden');log('Mission control: outpost systems online. Welcome, commander.','good');log(world==='Moon'?'Destination: Moon. Watch energy reserves during lunar night.':'Destination: Mars. Dust storms may reduce solar power.');log('Start simple: follow the suggested next step, keep supplies above zero, and complete the checklist.','good');$('lesson').innerHTML='<b>First mission tip:</b> Keep oxygen, water, food, and power above zero. Check your resource cards before every action.';render();toast('Mission launched! Follow the recommendation panel.')
}
function canPay(cost){
return Object.entries(cost).every(([k,v])=>game[k]>=v)
}
function costText(cost){
return Object.entries(cost).map(([k,v])=>`${
v
}
 ${
k
}
`).join(' + ')||'Free'
}
function act(id){
if(!game||game.ended)return;const a=actions.find(x=>x.id===id);if(!canPay(a.cost)){
toast('Not enough supplies. Choose a different operation.');log('Could not complete '+a.name+': not enough supplies.','warn');render();return
}
Object.entries(a.cost).forEach(([k,v])=>game[k]-=v);const msg=a.run(game);if(a.goal)game.goals[a.goal]=true;for(const k of ['oxygen','water','food','power','shield','health','morale'])game[k]=clamp(game[k]);game.parts=clamp(game.parts,0,30);game.log.unshift({
day:game.day,msg,type:'good'
}
);game.log=game.log.slice(0,40);$('lesson').innerHTML='<b>Why it matters:</b> '+a.lesson;advance()
}
function advance(){
game.day++;game.oxygen-=4;game.water-=4;game.food-=4;game.power-=3;if(game.world==='Mars'&&Math.random()<.14){
game.power-=10;log('Dust storm: sunlight was reduced and power fell by 10.','warn')
}
if(game.world==='Moon'&&game.day%4===0){
game.power-=6;log('Lunar night: extra energy was needed for heating.','warn')
}
if(Math.random()<.10){
let e=Math.random();if(e<.4){
game.oxygen-=7;log('Equipment warning: an oxygen valve is leaking. Repair life support soon.','bad')
}
else if(e<.72){
game.parts=Math.max(0,game.parts-1);game.power-=4;log('Small equipment failure: one spare part and some power were used.','warn')
}
else{
game.shield-=6;log('Solar activity increased radiation risk. Shelter protection was tested.','bad')
}
}
if(game.oxygen<20||game.water<18||game.food<18||game.power<12)game.health-=5;if(game.shield<20&&Math.random()<.4)game.health-=3;if(game.oxygen<=0||game.water<=0||game.food<=0||game.power<=0)game.health-=10;if(game.morale<25)game.health-=3;game.health=clamp(game.health);game.morale=clamp(game.morale-(game.food<20?4:1));if(game.health<=0){
end(false,'Crew health reached zero. Review the mission log and resource bars, then try a safer plan.');return
}
if(game.day>12){
let success=game.health>=35&&game.oxygen>0&&game.water>0&&game.food>0&&game.power>0;end(success,success?'Your crew survived the 12-day training mission. Review the score and checklist to see what went well.':'The crew reached the end, but a survival system is critically low. Try a different strategy.');return
}
log('Daily supplies used: oxygen, water, food, and power. Check reserves before acting.');render()
}
function advice(){
if(!game)return{
text:'Start the mission to receive advice.'
}
;const checks=[['oxygen',27,'repair','Oxygen is getting low. Repair life support before breathable air runs out.'],['water',27,'water','Water is getting low. Recycle water before drinking supplies run out.'],['food',27,'farm','Food is getting low. Grow food before the crew begins to suffer.'],['power',27,'solar','Power is getting low. Tune the solar array and avoid power-heavy operations.'],['shield',28,'shield','Radiation protection is low. Improve the shelter if you have spare parts.']];for(const [k,n,id,msg] of checks){
if(game[k]<n){
let a=actions.find(x=>x.id===id);return{
text:msg+(canPay(a.cost)?'':' You lack the supplies for this action, so choose a low-cost operation first.')
}
}
}
if(game.parts<4)return{
text:'Spare parts are running low. Save them for essential repairs.'
}
;if(!game.goals.research)return{
text:'Your basic supplies look stable. Run a science experiment when you can spare the power.'
}
;return{
text:'Your supplies look stable. Finish any checklist goals you want, then check your bars again.'
}
}
function render(){
if(!game)return;$('headerStatus').textContent=game.ended?'MISSION ENDED':'MISSION ACTIVE';$('dayTag').textContent=`DAY ${
Math.min(game.day,12)
}
 / 12`;$('outpostTitle').textContent=game.world==='Moon'?'Lunar Research Outpost':'Martian Research Outpost';$('planetSub').textContent=game.world==='Moon'?'Moon surface • No breathable air • Cold lunar nights':'Mars surface • Thin atmosphere • Dust storm risk';$('sceneLabel').textContent=(game.world==='Moon'?'LUNAR':'MARTIAN')+' OUTPOST • ONLINE';$('sceneState').textContent=game.power<20?'⚠ LOW POWER':game.oxygen<25?'⚠ OXYGEN LOW':game.shield<25?'⚠ RADIATION RISK':'✓ SYSTEMS RUNNING';$('planetArt').style.background=game.world==='Moon'?'linear-gradient(135deg,#e9f4f7,#6f98b6 60%,#344c70)':'linear-gradient(135deg,#f2bc8d,#b95f4c 60%,#6d343a)';$('worldMetric').textContent=game.world;$('dayMetric').textContent=`${
Math.min(game.day,12)
}
 / 12`;$('healthMetric').textContent=game.health+'%';$('moraleMetric').textContent=game.morale+'%';$('scienceMetric').textContent=game.science;$('scoreMetric').textContent=game.score;let status=game.health<35?'CREW AT RISK':game.power<15?'LOW POWER':game.oxygen<20||game.water<20||game.food<20?'SUPPLIES LOW':'OPERATIONAL';$('statusMetric').textContent=status;$('statusMetric').className=game.health<35||game.power<15?'danger':status==='SUPPLIES LOW'?'warning':'good';$('resources').innerHTML=resourceInfo.map(r=>{
let v=Math.round(game[r.key]),pct=clamp(v/r.max*100),level=pct<23?'bad':pct<48?'warn':'';return `<div class="resource"><div class="rhead"><span>${
r.icon
}
 ${
r.name
}
</span><span>${
r.unit
}
</span></div><div class="rval">${
v
}
<span class="unit"> / ${
r.max
}
</span></div><div class="bar"><div class="fill ${
level
}
" style="width:${
pct
}
%"></div></div><div class="rnote">${
pct<23?'<span class="danger">Urgent: act soon</span>':pct<48?'<span class="warning">Running low</span>':r.note
}
</div></div>`
}
).join('');$('recommendation').innerHTML='<b>Suggested next step:</b> '+advice().text;$('actions').innerHTML=actions.map(a=>{
let ok=canPay(a.cost);return `<button class="action" data-action="${
a.id
}
" ${
ok?'':'disabled'
}
><span class="actiontop"><span class="ico">${
a.icon
}
</span><span class="aname">${
a.name
}
</span></span><span class="adesc">${
a.short
}
</span><span class="cost ${
ok?'':'low'
}
">Cost: ${
costText(a.cost)
}
${
ok?'':' • Not enough supplies'
}
</span></button>`
}
).join('');document.querySelectorAll('[data-action]').forEach(b=>b.addEventListener('click',()=>act(b.dataset.action)));const goals=[['solar','Tune the solar array','Improve stored power'],['repair','Repair life support','Keep oxygen working'],['farm','Grow food','Produce meals locally'],['shield','Improve the shelter','Strengthen radiation protection'],['research','Run an experiment','Earn science points']];$('objectives').innerHTML=goals.map(([k,n,d])=>`<div class="objective"><div class="check ${
game.goals[k]?'done':''
}
">${
game.goals[k]?'✓':''
}
</div><div><b>${
n
}
</b><p>${
game.goals[k]?'Completed':d
}
</p></div></div>`).join('');$('log').innerHTML=game.log.map(e=>`<div class="entry ${
e.type
}
"><div class="logday">DAY ${
Math.min(e.day,12)
}
 • MISSION CONTROL</div>${
e.msg
}
</div>`).join('')||'<div class="muted small">No mission events yet.</div>';$('tip').textContent=game.power<25?'Save energy for life support and water recycling. Tune the solar array if you have spare parts.':game.parts<4?'Spare parts are limited. Save them for important repairs.':game.health<60?'Crew health is falling. Stabilize supplies and schedule rest.':'Beginner strategy: keep supplies balanced, follow the suggested action, and do science only when safe.'
}
function end(success,reason){
game.ended=true;log(success?'Mission control: crew survived the training mission. Congratulations!':'Mission control: mission ended. Review the log and try a new strategy.',success?'good':'bad');render();$('endOverlay').classList.remove('hidden');$('endTitle').textContent=success?'MISSION SUCCESS':'MISSION NEEDS WORK';$('endTitle').style.color=success?'var(--green)':'var(--red)';$('endText').textContent=reason;$('debriefStats').innerHTML=`<div class="metric"><span>Destination</span><strong>${
game.world
}
</strong></div><div class="metric"><span>Final crew health</span><strong>${
game.health
}
%</strong></div><div class="metric"><span>Science points</span><strong>${
game.science
}
</strong></div><div class="metric"><span>Checklist completed</span><strong>${
Object.values(game.goals).filter(Boolean).length
}
 / 5</strong></div><div class="metric"><span>Mission score</span><strong>${
game.score
}
</strong></div>`
}
const guideTips = [
  'Step 1: Start with the lowest resource bar. Red means urgent; yellow means plan ahead.',
  'Step 2: Your crew uses oxygen, water, food, and power every day. Do not let any reach zero.',
  'Step 3: Repair life support when oxygen is low. Recycle water when water is low.',
  'Step 4: Grow food before the food supply becomes critical. Rest can improve crew morale.',
  'Step 5: Solar power and radiation protection matter most when the environment gets harsh.',
  'Step 6: Science earns points, but survival comes first. Do science when supplies are stable.'
];let guideIndex = 0;const guideButton = document.getElementById('guideNext');if (guideButton) {
  guideButton.addEventListener('click', () => {
    guideIndex = (guideIndex + 1) % guideTips.length;    const strip = document.getElementById('guideStrip');    strip.querySelector('.guide-number').textContent = String(guideIndex + 1);    strip.querySelector('strong').textContent = 'Easy play tip ' + (guideIndex + 1) + ' of ' + guideTips.length;    strip.querySelector('span:not(.guide-number)').textContent = guideTips[guideIndex];  
}
);}
document.querySelectorAll('[data-world]').forEach(b=>b.addEventListener('click',()=>{
world=b.dataset.world;document.querySelectorAll('[data-world]').forEach(x=>x.classList.toggle('selected',x===b))
}
));$('launchBtn').addEventListener('click',launch);$('restartBtn').addEventListener('click',()=>{
$('startOverlay').classList.remove('hidden');$('endOverlay').classList.add('hidden')
}
);$('againBtn').addEventListener('click',()=>{
$('endOverlay').classList.add('hidden');$('startOverlay').classList.remove('hidden')
}
);$('helpBtn').addEventListener('click',()=>$('helpOverlay').classList.remove('hidden'));$('closeHelp').addEventListener('click',()=>$('helpOverlay').classList.add('hidden'));$('clearLog').addEventListener('click',()=>{
if(game){
game.log=[];render()
}
}
);
</script></body></html>"""

@app.route('/')
def home():
    return render_template_string(PAGE)


@app.route('/health')
def health():
    return jsonify(
        status='ok',
        app='Junior Astronaut Mission Trainer'
    )


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', '5000'))
    )
