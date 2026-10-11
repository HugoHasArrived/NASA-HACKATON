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

#spaceCanvas{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:1}
.scene .stars,.scene .planet,.scene .terrain,.scene .base{display:none}
.scene-label,.scene-state{z-index:3;backdrop-filter:blur(8px);box-shadow:0 8px 24px #0005}
.scene{height:340px;border-radius:18px;background:#070d20;box-shadow:inset 0 0 70px #0008,0 12px 34px #0003}
.panel{background:linear-gradient(145deg,#142b43f5,#091523f7);border-color:#2c4a68;box-shadow:0 18px 55px #0004,inset 0 1px #ffffff08}
.resource{background:linear-gradient(145deg,#0d2033,#081321);border-color:#29445f}
.rval{font-variant-numeric:tabular-nums}
.action{background:linear-gradient(145deg,#10263b,#0a1727);border-radius:14px;transition:transform .18s,border-color .18s,box-shadow .18s}
.action:focus-visible{outline:3px solid var(--cyan);outline-offset:3px}
.action .ico{display:grid;place-items:center;width:38px;height:38px;border:1px solid #4b7c9970;border-radius:12px;background:linear-gradient(145deg,#1b4059,#112338);font-size:22px}
.action .aname{font-size:13px}
.action .adesc{font-size:11px}
.action .cost{border-top:1px solid #ffffff0c}
.fill{position:relative;overflow:hidden}
.fill:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,#ffffff45,transparent);transform:translateX(-120%);animation:resourceShine 4s ease-in-out infinite}
@keyframes resourceShine{0%,60%{transform:translateX(-120%)}90%,100%{transform:translateX(120%)}}
.logo{position:relative;isolation:isolate;box-shadow:0 0 0 5px #63e8df0a,0 0 34px #42dcd744}
.logo:after{content:"";position:absolute;inset:-5px;border:1px solid #73f5ed55;border-radius:19px;animation:logoPulse 3s ease-out infinite;z-index:-1}
@keyframes logoPulse{0%{transform:scale(.9);opacity:.8}100%{transform:scale(1.3);opacity:0}}
.tag{background:#081727b8}
.guide-strip{border-color:#3c8195;background:linear-gradient(110deg,#10394a,#10233a 75%);box-shadow:0 0 25px #36ddeb0c}
.guide-strip button{border-color:#4d8398;background:#123348}
.objective{padding:8px;border-radius:10px;transition:background .2s}
.objective:has(.check.done){background:#66e9a80b}
.check.done{box-shadow:0 0 16px #7ce4a844}
.entry{border:1px solid #1a344b;border-left:3px solid #4b84a8}
.entry.good{border-left-color:var(--green)}
.entry.warn{border-left-color:var(--yellow)}
.entry.bad{border-left-color:var(--red)}
.brief{box-shadow:inset 3px 0 #5ce8df}
.modal{background:radial-gradient(ellipse at 100% 0,#1e4760 0,transparent 44%),linear-gradient(150deg,#132942,#091524);box-shadow:0 35px 120px #000b;border-color:#456984}
.choice{min-height:112px;border-radius:14px;transition:transform .18s,background .18s,border-color .18s}
.choice:hover{transform:translateY(-2px)}
.primary{box-shadow:0 8px 24px #5ce8df20}
button{transition:transform .16s,border-color .16s,background .16s,box-shadow .16s}
.footer{border-top:1px solid #ffffff0a;margin-top:8px}
.scene:before{content:"";position:absolute;inset:0;z-index:2;pointer-events:none;background:linear-gradient(180deg,#07101d1c,transparent 40%,#07101d18);box-shadow:inset 0 0 50px #0207117d}
@media(max-width:560px){.scene{height:250px}.scene-label,.scene-state{font-size:9px;padding:5px 7px}.scene-label{max-width:62%}.scene-state{max-width:48%}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}


.expedition{overflow:hidden;position:relative;background:linear-gradient(145deg,#101f35,#08121f)}
.expedition-head{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.rover-wrap{position:relative;border:1px solid #36516d;border-radius:16px;overflow:hidden;background:#090f1d;margin-top:14px}
#roverCanvas{display:block;width:100%;height:310px;touch-action:none}
.rover-hud{display:flex;gap:8px;flex-wrap:wrap;padding:10px;background:#091421;border-top:1px solid #253d55}
.hud-pill{border:1px solid #2d4b67;border-radius:999px;padding:5px 10px;font-size:11px;color:#cce8f8;background:#10243a}
.rover-controls{display:grid;grid-template-columns:repeat(3,48px);gap:6px;justify-content:center;align-items:center;margin:12px auto 2px}
.rover-controls button{height:42px;padding:0;font-size:17px;touch-action:manipulation}
.rover-controls .empty{visibility:hidden}
.rover-actions{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:space-between;margin-top:10px}
.mission-banner{display:flex;gap:10px;align-items:flex-start;padding:12px;border:1px solid #326078;background:linear-gradient(110deg,#103449,#102036);border-radius:13px;margin-top:12px}
.mission-banner .emoji{font-size:24px}
#roverMessage{font-size:12px;color:#b7cce0;margin-top:8px;min-height:18px}
@media(max-width:560px){#roverCanvas{height:240px}.rover-controls{grid-template-columns:repeat(3,54px)}.rover-controls button{height:48px}}

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
<button id="saveBtn">💾 Save</button><button id="loadBtn">📂 Load</button><button id="helpBtn">❔ Help</button>
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
<div class="scene" id="scene">
<canvas id="spaceCanvas" aria-label="Animated illustration of the selected planetary outpost"></canvas>
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

<section class="panel expedition">
<div class="expedition-head"><div><div class="eyebrow">OPTIONAL FIELD ACTIVITY</div><h2 style="margin:5px 0">Rover exploration</h2><div class="sub">Drive around the surface, collect science samples, and return safely to base.</div></div><span class="tag">NO DAY COST</span></div>
<div class="mission-banner"><div class="emoji">🛰️</div><div><b>Field objective</b><div class="small muted">Collect 5 glowing samples, avoid the rocks, then drive back to the blue landing pad. Successful trips earn science points, spare parts, and crew morale.</div></div></div>
<div class="rover-wrap"><canvas id="roverCanvas" aria-label="Interactive rover exploration field"></canvas><div class="rover-hud"><span class="hud-pill" id="roverSamples">Samples: 0 / 5</span><span class="hud-pill" id="roverDistance">Distance: 0 m</span><span class="hud-pill" id="roverBattery">Battery: 100%</span><span class="hud-pill" id="roverStatus">Rover parked</span></div></div>
<div class="rover-actions"><div class="small muted">Keyboard: WASD or arrow keys. On phones, use the controls below.</div><div style="display:flex;gap:8px;flex-wrap:wrap"><button id="roverStart" class="primary">🚙 Start expedition</button><button id="roverReset">Reset field</button></div></div>
<div class="rover-controls" aria-label="Rover direction controls"><span class="empty"></span><button data-rover-dir="up" aria-label="Drive forward">▲</button><span class="empty"></span><button data-rover-dir="left" aria-label="Drive left">◀</button><button data-rover-dir="down" aria-label="Drive backward">▼</button><button data-rover-dir="right" aria-label="Drive right">▶</button></div>
<div id="roverMessage" aria-live="polite">Start an expedition when your mission is active. You can practice driving before launch, too.</div>
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

const sceneCanvas=document.getElementById('spaceCanvas');
const sceneCtx=sceneCanvas.getContext('2d');
let sceneWidth=0;
let sceneHeight=0;
let sceneFrame=0;
let sceneStars=[];
let sceneDust=[];
let sceneLastTime=0;
function resizeSpaceScene(){
const box=sceneCanvas.getBoundingClientRect();
const ratio=Math.min(window.devicePixelRatio||1,2);
sceneWidth=Math.max(1,box.width);
sceneHeight=Math.max(1,box.height);
sceneCanvas.width=Math.round(sceneWidth*ratio);
sceneCanvas.height=Math.round(sceneHeight*ratio);
sceneCtx.setTransform(ratio,0,0,ratio,0,0);
sceneStars=Array.from({length:Math.max(45,Math.floor(sceneWidth*.28))},()=>({x:Math.random()*sceneWidth,y:Math.random()*sceneHeight*.67,r:Math.random()*1.25+.25,a:Math.random()*.65+.2,p:Math.random()*6.28}));
sceneDust=Array.from({length:45},()=>({x:Math.random()*sceneWidth,y:Math.random()*sceneHeight,v:Math.random()*.22+.04,r:Math.random()*1.8+.3,a:Math.random()*.24+.06}));
}
function pathShape(ctx,points,fill,stroke,width=1){
ctx.beginPath();
points.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));
ctx.closePath();
if(fill){ctx.fillStyle=fill;ctx.fill()}
if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=width;ctx.stroke()}
}
function roundedRect(ctx,x,y,w,h,r,fill,stroke){
ctx.beginPath();ctx.roundRect(x,y,w,h,r);
if(fill){ctx.fillStyle=fill;ctx.fill()}
if(stroke){ctx.strokeStyle=stroke;ctx.stroke()}
}
function glowCircle(ctx,x,y,r,color,blur){
ctx.save();ctx.shadowColor=color;ctx.shadowBlur=blur;ctx.fillStyle=color;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();ctx.restore();
}
function drawPlanet(ctx,w,h,t){
const isMars=world==='Mars';
const px=w*(isMars?.78:.79);
const py=h*(isMars?.27:.29);
const radius=Math.min(w,h)*(isMars?.17:.2);
const halo=ctx.createRadialGradient(px,py,radius*.5,px,py,radius*1.9);
halo.addColorStop(0,isMars?'#f07d4b24':'#8bd8ff22');halo.addColorStop(1,'#8bd8ff00');
ctx.fillStyle=halo;ctx.beginPath();ctx.arc(px,py,radius*1.9,0,Math.PI*2);ctx.fill();
const sphere=ctx.createRadialGradient(px-radius*.42,py-radius*.4,radius*.08,px,py,radius*1.25);
if(isMars){sphere.addColorStop(0,'#ffcf9b');sphere.addColorStop(.38,'#dc7758');sphere.addColorStop(.78,'#8d3c3c');sphere.addColorStop(1,'#321c32')}else{sphere.addColorStop(0,'#f1ffff');sphere.addColorStop(.32,'#9fc8df');sphere.addColorStop(.72,'#426a8e');sphere.addColorStop(1,'#172d4e')}
ctx.fillStyle=sphere;ctx.beginPath();ctx.arc(px,py,radius,0,Math.PI*2);ctx.fill();
ctx.save();ctx.beginPath();ctx.arc(px,py,radius*.97,0,Math.PI*2);ctx.clip();
for(let i=0;i<8;i++){
const bx=px+Math.sin(i*8.1+(isMars?1:0))*radius*.65;
const by=py+Math.cos(i*5.4)*radius*.6;
ctx.fillStyle=isMars?'#6d343b30':'#d8f4ff26';ctx.beginPath();ctx.ellipse(bx,by,radius*(.1+(i%3)*.04),radius*(.04+(i%2)*.035),i*.4,0,Math.PI*2);ctx.fill();
}
const shade=ctx.createLinearGradient(px-radius,py-radius,px+radius,py+radius);
shade.addColorStop(0,'#ffffff20');shade.addColorStop(.5,'#ffffff00');shade.addColorStop(1,'#020718a8');ctx.fillStyle=shade;ctx.fillRect(px-radius,py-radius,radius*2,radius*2);
ctx.restore();
}
function drawStars(ctx,w,h,t){
for(const star of sceneStars){
const flicker=.55+.45*Math.sin(t*.0018+star.p);
ctx.globalAlpha=star.a*flicker;
ctx.fillStyle=star.r>1.1?'#d8f5ff':'#ffffff';
ctx.beginPath();ctx.arc(star.x,star.y,star.r,0,Math.PI*2);ctx.fill();
if(star.r>1.15){ctx.globalAlpha=star.a*flicker*.35;ctx.fillRect(star.x-3,star.y-.4,6,.8);ctx.fillRect(star.x-.4,star.y-3,.8,6)}
}
ctx.globalAlpha=1;
}
function drawTerrain(ctx,w,h,t){
const isMars=world==='Mars';
const horizon=h*.62;
const sky=ctx.createLinearGradient(0,0,0,h);
sky.addColorStop(0,isMars?'#160e25':'#07152c');sky.addColorStop(.52,isMars?'#4b293c':'#1a3b5b');sky.addColorStop(1,isMars?'#a6574b':'#6b7890');ctx.fillStyle=sky;ctx.fillRect(0,0,w,h);
drawStars(ctx,w,h,t);drawPlanet(ctx,w,h,t);
const glow=ctx.createRadialGradient(w*.48,h*.63,2,w*.48,h*.63,w*.66);
glow.addColorStop(0,isMars?'#f59a6436':'#78d5ff24');glow.addColorStop(1,'#00000000');ctx.fillStyle=glow;ctx.fillRect(0,h*.34,w,h*.66);
pathShape(ctx,[[0,horizon+9],[w*.09,h*.53],[w*.2,h*.6],[w*.34,h*.48],[w*.46,h*.59],[w*.59,h*.5],[w*.74,h*.59],[w*.89,h*.51],[w,h*.57],[w,h],[0,h]],isMars?'#5c3946':'#273e5b');
pathShape(ctx,[[0,h*.75],[w*.13,h*.67],[w*.25,h*.73],[w*.42,h*.64],[w*.58,h*.72],[w*.74,h*.65],[w*.9,h*.72],[w,h*.66],[w,h],[0,h]],isMars?'#9a5a4e':'#647087');
const ground=ctx.createLinearGradient(0,h*.72,0,h);ground.addColorStop(0,isMars?'#bb7056':'#8b8995');ground.addColorStop(1,isMars?'#3b2636':'#202b43');ctx.fillStyle=ground;ctx.fillRect(0,h*.74,w,h*.26);
for(let i=0;i<22;i++){
const x=(i*97+17)%Math.max(1,w);const y=h*(.78+((i*23)%20)/100);const rw=2+(i%4)*2;
ctx.fillStyle=isMars?'#efb08b35':'#d5e3f544';ctx.beginPath();ctx.ellipse(x,y,rw,rw*.45,(i%5)*.2,0,Math.PI*2);ctx.fill();
}
for(let i=0;i<5;i++){
const x=(i*137+53)%w;const y=h*(.87+(i%3)*.035);ctx.strokeStyle='#1a203c55';ctx.lineWidth=1.5;ctx.beginPath();ctx.ellipse(x,y,8+i%4*3,2+i%2,0,0,Math.PI*2);ctx.stroke();
}
}
function drawSolarPanel(ctx,x,y,w,h,t){
ctx.save();ctx.translate(x,y);ctx.transform(1,-.12,.08,1,0,0);
ctx.fillStyle='#101e43';ctx.fillRect(0,0,w,h);ctx.strokeStyle='#9de8ff';ctx.lineWidth=1.4;ctx.strokeRect(0,0,w,h);
for(let i=1;i<4;i++){ctx.strokeStyle='#4a9bd2';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(w*i/4,0);ctx.lineTo(w*i/4,h);ctx.stroke()}
for(let i=1;i<3;i++){ctx.beginPath();ctx.moveTo(0,h*i/3);ctx.lineTo(w,h*i/3);ctx.stroke()}
ctx.strokeStyle='#d2f7ff';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(w*.5,h);ctx.lineTo(w*.5,h+19);ctx.stroke();ctx.restore();
}
function drawHabitat(ctx,w,h,t){
const scale=Math.min(1.12,w/620);const cx=w*.47;const ground=h*.79;const bw=110*scale;const bh=63*scale;const bx=cx-bw/2;const by=ground-bh;
ctx.save();ctx.translate(0,Math.sin(t*.0009)*.6);
ctx.strokeStyle='#c7efff';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(cx,by+6);ctx.lineTo(cx,by-25);ctx.stroke();
glowCircle(ctx,cx,by-26,3,'#7df8f0',12);
ctx.fillStyle='#263c57';ctx.beginPath();ctx.ellipse(cx,ground+2,bw*.82,7*scale,0,0,Math.PI*2);ctx.fill();
ctx.shadowColor='#6feaff';ctx.shadowBlur=19;roundedRect(ctx,bx,by,bw,bh,14*scale,'#b8d1de','#f0fbff');ctx.shadowBlur=0;
const body=ctx.createLinearGradient(0,by,0,by+bh);body.addColorStop(0,'#effaff');body.addColorStop(.56,'#8faebd');body.addColorStop(1,'#506d83');roundedRect(ctx,bx+3,by+3,bw-6,bh-6,12*scale,body,'#d8f8ff');
for(let i=0;i<4;i++){const wx=bx+13*scale+i*22*scale;roundedRect(ctx,wx,by+13*scale,15*scale,15*scale,3*scale,'#0b2945','#9deeff');ctx.fillStyle='#4bcfe7';ctx.fillRect(wx+2*scale,by+15*scale,2*scale,10*scale)}
roundedRect(ctx,cx-25*scale,by+38*scale,50*scale,12*scale,3*scale,'#254157','#7898aa');ctx.fillStyle='#e2f7ff';ctx.font=`900 ${6.8*scale}px system-ui`;ctx.textAlign='center';ctx.fillText('HABITAT 01',cx,by+46*scale);
ctx.strokeStyle='#cce8f5';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(bx+bw*.82,by+bh*.7);ctx.lineTo(bx+bw*.92,ground);ctx.stroke();
drawSolarPanel(ctx,bx-56*scale,ground-34*scale,48*scale,31*scale,t);drawSolarPanel(ctx,bx+bw+9*scale,ground-31*scale,43*scale,28*scale,t);
ctx.restore();
}
function drawRover(ctx,w,h,t){
const x=w*(.73+Math.sin(t*.00025)*.025);const y=h*.79;const scale=Math.min(1,w/520);
ctx.save();ctx.translate(x,y);
ctx.fillStyle='#151c2e';ctx.beginPath();ctx.ellipse(0,5*scale,31*scale,4*scale,0,0,Math.PI*2);ctx.fill();
ctx.strokeStyle='#c8eaff';ctx.lineWidth=2*scale;ctx.beginPath();ctx.moveTo(-20*scale,-2*scale);ctx.lineTo(-17*scale,-14*scale);ctx.lineTo(16*scale,-14*scale);ctx.lineTo(22*scale,-2*scale);ctx.stroke();
roundedRect(ctx,-25*scale,-17*scale,48*scale,17*scale,4*scale,'#d4e7ef','#f4ffff');roundedRect(ctx,-14*scale,-29*scale,24*scale,13*scale,4*scale,'#7096aa','#e4faff');
ctx.fillStyle='#13344e';ctx.fillRect(-10*scale,-26*scale,15*scale,6*scale);
for(const wx of [-16,14]){ctx.fillStyle='#0a1324';ctx.beginPath();ctx.arc(wx*scale,1*scale,7*scale,0,Math.PI*2);ctx.fill();ctx.strokeStyle='#83b8d1';ctx.lineWidth=2*scale;ctx.beginPath();ctx.arc(wx*scale,1*scale,4*scale,0,Math.PI*2);ctx.stroke()}
ctx.strokeStyle='#d8f5ff';ctx.lineWidth=1.5*scale;ctx.beginPath();ctx.moveTo(0,-29*scale);ctx.lineTo(5*scale,-37*scale);ctx.stroke();glowCircle(ctx,5*scale,-38*scale,2*scale,'#70f4e9',9);
ctx.restore();
}
function drawAstronaut(ctx,w,h,t){
const x=w*.29+Math.sin(t*.0008)*1.8;const y=h*.79;const s=Math.min(1,w/600);
ctx.save();ctx.translate(x,y);
ctx.fillStyle='#19253a';ctx.beginPath();ctx.ellipse(0,2*s,13*s,3*s,0,0,Math.PI*2);ctx.fill();
ctx.strokeStyle='#edf8ff';ctx.lineWidth=6*s;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(-4*s,-13*s);ctx.lineTo(-7*s,-2*s);ctx.moveTo(4*s,-13*s);ctx.lineTo(8*s,-2*s);ctx.stroke();
roundedRect(ctx,-10*s,-35*s,20*s,25*s,6*s,'#dceaf0','#ffffff');
ctx.strokeStyle='#eaf8ff';ctx.lineWidth=4*s;ctx.beginPath();ctx.moveTo(-8*s,-29*s);ctx.lineTo(-15*s,-19*s);ctx.moveTo(8*s,-29*s);ctx.lineTo(15*s,-23*s);ctx.stroke();
ctx.fillStyle='#b7d3e3';ctx.beginPath();ctx.arc(0,-41*s,9*s,0,Math.PI*2);ctx.fill();ctx.fillStyle='#15364e';ctx.beginPath();ctx.ellipse(1*s,-42*s,6*s,5*s,-.1,0,Math.PI*2);ctx.fill();ctx.strokeStyle='#76f3ee';ctx.lineWidth=1*s;ctx.beginPath();ctx.arc(0,-41*s,9*s,0,Math.PI*2);ctx.stroke();
roundedRect(ctx,-6*s,-25*s,12*s,6*s,2*s,'#eea05f','#ffe4b5');
ctx.restore();
}
function drawWeather(ctx,w,h,t){
if(world==='Mars'){
const wind=(t*.022)% (w+120)-60;
ctx.strokeStyle='#ffb58b25';ctx.lineWidth=1.2;
for(let i=0;i<16;i++){const x=(wind+i*57+w)%(w+40)-20;const y=h*(.56+(i%8)*.045);ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+14+(i%4)*5,y-2);ctx.stroke()}
}else{
ctx.strokeStyle='#b8d8ff18';ctx.lineWidth=1;
for(let i=0;i<7;i++){const x=(i*83+(t*.006)%w)%w;ctx.beginPath();ctx.moveTo(x,h*.74);ctx.lineTo(x+14,h*.79);ctx.stroke()}
}
for(const d of sceneDust){d.x-=d.v*(world==='Mars'?1.8:1);if(d.x<0)d.x=w;d.y+=Math.sin(t*.0004+d.x)*.03;if(d.y>h)d.y=0;ctx.globalAlpha=d.a;ctx.fillStyle=world==='Mars'?'#ffc19b':'#d6f6ff';ctx.beginPath();ctx.arc(d.x,d.y,d.r,0,Math.PI*2);ctx.fill()}
ctx.globalAlpha=1;
}
function drawScene(t){
if(!sceneCtx||!sceneWidth||!sceneHeight){requestAnimationFrame(drawScene);return}
sceneFrame++;
const ctx=sceneCtx;const w=sceneWidth;const h=sceneHeight;
ctx.clearRect(0,0,w,h);drawTerrain(ctx,w,h,t);drawWeather(ctx,w,h,t);drawHabitat(ctx,w,h,t);drawRover(ctx,w,h,t);drawAstronaut(ctx,w,h,t);
if(game){
const low=game.power<25||game.oxygen<25||game.water<25;
if(low){ctx.save();ctx.strokeStyle='#ff718544';ctx.lineWidth=2;ctx.setLineDash([6,5]);ctx.strokeRect(8,8,w-16,h-16);ctx.restore()}
}
requestAnimationFrame(drawScene);
}
function updateSceneLabels(){
const label=$('sceneLabel');const state=$('sceneState');
if(!game){label.textContent='OUTPOST • STANDBY';state.textContent='SYSTEMS CHECKING';return}
label.textContent=(game.world==='Mars'?'MARS':'LUNAR')+' OUTPOST • DAY '+Math.min(game.day,12);
if(game.oxygen<25||game.water<20||game.food<20)state.textContent='SUPPLY ALERT';else if(game.power<25)state.textContent='LOW POWER';else state.textContent='SYSTEMS NOMINAL';
}
const originalRender=render;
render=function(){originalRender();updateSceneLabels()};
window.addEventListener('resize',resizeSpaceScene,{passive:true});
resizeSpaceScene();
requestAnimationFrame(drawScene);



const roverCanvas=document.getElementById('roverCanvas');
const roverCtx=roverCanvas.getContext('2d');
const roverState={x:0,y:0,baseX:0,baseY:0,samples:[],rocks:[],collected:0,battery:100,distance:0,active:false,complete:false,paid:false,keys:{},last:0};
function roverResize(){const r=roverCanvas.getBoundingClientRect();const d=Math.min(window.devicePixelRatio||1,2);roverCanvas.width=Math.max(1,Math.floor(r.width*d));roverCanvas.height=Math.max(1,Math.floor(r.height*d));roverCtx.setTransform(d,0,0,d,0,0);if(!roverState.active)roverReset(false);roverDraw()}
function roverW(){return roverCanvas.getBoundingClientRect().width}
function roverH(){return roverCanvas.getBoundingClientRect().height}
function roverReset(show=true){const w=roverW()||600,h=roverH()||300;roverState.baseX=w*.13;roverState.baseY=h*.75;roverState.x=roverState.baseX;roverState.y=roverState.baseY;roverState.collected=0;roverState.battery=100;roverState.distance=0;roverState.active=false;roverState.complete=false;roverState.paid=false;roverState.keys={};roverState.samples=[];roverState.rocks=[];for(let i=0;i<5;i++)roverState.samples.push({x:w*(.3+i*.125),y:h*(.27+((i*37)%47)/100),got:false,p:i*1.7});for(let i=0;i<8;i++)roverState.rocks.push({x:w*(.24+((i*19)%70)/100),y:h*(.2+((i*31)%61)/100),r:7+(i%4)*2});roverHud();roverDraw();if(show)document.getElementById('roverMessage').textContent='Field reset. Start an expedition and collect all five samples.'}
function roverHud(){document.getElementById('roverSamples').textContent='Samples: '+roverState.collected+' / 5';document.getElementById('roverDistance').textContent='Distance: '+Math.round(roverState.distance)+' m';document.getElementById('roverBattery').textContent='Battery: '+Math.max(0,Math.round(roverState.battery))+'%';document.getElementById('roverStatus').textContent=roverState.complete?'Mission complete':roverState.active?'Exploring':roverState.battery<=0?'Battery empty':'Rover parked'}
function roverDraw(){if(!roverCanvas||!roverCtx)return;const w=roverW(),h=roverH();if(!w||!h)return;const c=roverCtx;const mars=world==='Mars';const sky=c.createLinearGradient(0,0,0,h);sky.addColorStop(0,mars?'#3c1e37':'#091b36');sky.addColorStop(.65,mars?'#c06b55':'#607b9b');sky.addColorStop(1,mars?'#55303b':'#242e48');c.fillStyle=sky;c.fillRect(0,0,w,h);for(let i=0;i<55;i++){const x=(i*97+13)%w,y=(i*47+9)%(h*.52);c.fillStyle='rgba(255,255,255,'+(0.25+(i%4)*.13)+')';c.fillRect(x,y,1.5,1.5)}const planetX=w*.8,planetY=h*.22,pr=Math.min(w,h)*.13;c.beginPath();c.arc(planetX,planetY,pr,0,Math.PI*2);const pg=c.createRadialGradient(planetX-pr*.4,planetY-pr*.4,1,planetX,planetY,pr);pg.addColorStop(0,mars?'#ffd2a0':'#f1fbff');pg.addColorStop(1,mars?'#9e4a46':'#45688c');c.fillStyle=pg;c.fill();c.fillStyle=mars?'#a45c50':'#747e91';c.beginPath();c.moveTo(0,h*.64);for(let x=0;x<=w;x+=20)c.lineTo(x,h*.62+Math.sin(x*.027)*9+Math.cos(x*.055)*5);c.lineTo(w,h);c.lineTo(0,h);c.closePath();c.fill();c.fillStyle=mars?'#6b3940':'#343b50';c.fillRect(0,h*.76,w,h*.24);for(let i=0;i<35;i++){let x=(i*71+23)%w,y=h*(.79+(i%8)*.025);c.fillStyle=i%2?'#1a2537':'#9b8790';c.beginPath();c.ellipse(x,y,2+i%5,1+i%2,0,0,Math.PI*2);c.fill()}c.strokeStyle='#9bd8f7';c.lineWidth=2;c.setLineDash([5,6]);c.beginPath();c.moveTo(roverState.baseX,roverState.baseY);c.lineTo(w*.88,h*.28);c.stroke();c.setLineDash([]);c.fillStyle='#37d9ff22';c.beginPath();c.arc(roverState.baseX,roverState.baseY,23,0,Math.PI*2);c.fill();c.strokeStyle='#75e8ff';c.lineWidth=2;c.strokeRect(roverState.baseX-12,roverState.baseY-8,24,16);c.fillStyle='#b5f6ff';c.fillRect(roverState.baseX-5,roverState.baseY-4,10,8);for(const s of roverState.samples){if(s.got)continue;c.save();c.translate(s.x,s.y);c.rotate(Math.sin(performance.now()*.002+s.p)*.12);c.shadowColor='#6af9dc';c.shadowBlur=18;c.fillStyle='#70f5d8';c.beginPath();c.moveTo(0,-8);c.lineTo(6,0);c.lineTo(0,8);c.lineTo(-6,0);c.closePath();c.fill();c.restore()}for(const r of roverState.rocks){c.fillStyle='#4d566a';c.strokeStyle='#a5b2c4';c.lineWidth=1;c.beginPath();c.moveTo(r.x-r.r,r.y+r.r*.5);c.lineTo(r.x-r.r*.6,r.y-r.r);c.lineTo(r.x+r.r*.5,r.y-r.r*.8);c.lineTo(r.x+r.r,r.y+r.r*.6);c.closePath();c.fill();c.stroke()}c.save();c.translate(roverState.x,roverState.y);c.shadowColor='#f9c66a';c.shadowBlur=13;c.fillStyle='#e4b65f';c.fillRect(-12,-7,24,12);c.fillStyle='#b7e7f6';c.fillRect(-4,-12,10,7);c.shadowBlur=0;c.fillStyle='#111a28';for(const wx of [-8,7]){c.beginPath();c.arc(wx,6,4,0,Math.PI*2);c.fill();c.strokeStyle='#94a9b9';c.stroke()}c.strokeStyle='#e6f7ff';c.beginPath();c.moveTo(0,-12);c.lineTo(0,-17);c.stroke();c.restore();c.fillStyle='#eff8ff';c.font='bold 11px system-ui';c.fillText('BASE',roverState.baseX-15,roverState.baseY+28);c.fillStyle='#d8e8f5';c.font='11px system-ui';c.fillText(mars?'MARS FIELD ZONE':'LUNAR FIELD ZONE',12,20);if(!roverState.active&&!roverState.complete){c.fillStyle='#06111dcc';c.fillRect(w*.28,h*.42,w*.44,36);c.fillStyle='#fff';c.textAlign='center';c.font='bold 12px system-ui';c.fillText('START EXPEDITION TO DEPLOY ROVER',w*.5,h*.42+23);c.textAlign='left'}if(roverState.complete){c.fillStyle='#06111ddd';c.fillRect(w*.22,h*.4,w*.56,44);c.fillStyle='#8fffe0';c.textAlign='center';c.font='bold 14px system-ui';c.fillText('SAMPLES SECURED • RETURN COMPLETE',w*.5,h*.4+27);c.textAlign='left'}}
function roverMove(dir){if(!roverState.active||roverState.complete||roverState.battery<=0)return;const speed=11;let dx=0,dy=0;if(dir==='up')dy=-speed;if(dir==='down')dy=speed;if(dir==='left')dx=-speed;if(dir==='right')dx=speed;const w=roverW(),h=roverH();const nx=Math.max(14,Math.min(w-14,roverState.x+dx)),ny=Math.max(22,Math.min(h-16,roverState.y+dy));let hit=false;for(const r of roverState.rocks){if(Math.hypot(nx-r.x,ny-r.y)<r.r+13){hit=true;break}}if(hit){roverState.battery=Math.max(0,roverState.battery-3);document.getElementById('roverMessage').textContent='Rock collision! Steer around obstacles; battery -3%.';roverHud();roverDraw();return}roverState.distance+=Math.hypot(dx,dy)*.35;roverState.x=nx;roverState.y=ny;roverState.battery=Math.max(0,roverState.battery-.18);for(const s of roverState.samples){if(!s.got&&Math.hypot(s.x-roverState.x,s.y-roverState.y)<18){s.got=true;roverState.collected++;document.getElementById('roverMessage').textContent='Sample secured! '+roverState.collected+' of 5 collected.'}}if(roverState.collected===5&&Math.hypot(roverState.x-roverState.baseX,roverState.y-roverState.baseY)<28){roverState.complete=true;roverState.active=false;if(!roverState.paid){roverState.paid=true;if(game&&!game.ended){game.science+=15;game.parts=clamp(game.parts+2,0,30);game.morale=clamp(game.morale+8);game.score+=100;log('Rover expedition complete: five samples returned. +15 science, +2 spare parts, +8 morale.','good');render()}document.getElementById('roverMessage').textContent='Excellent driving! All samples returned safely. Rewards added to your active mission.'}else document.getElementById('roverMessage').textContent='All samples returned safely.'}else if(roverState.battery<=0){roverState.active=false;document.getElementById('roverMessage').textContent='Battery depleted. Reset the field and plan a shorter route.'}roverHud();roverDraw()}
document.getElementById('roverStart').addEventListener('click',()=>{if(roverState.complete)roverReset(false);roverState.active=true;roverState.battery=Math.max(roverState.battery,30);document.getElementById('roverMessage').textContent='Rover deployed. Collect all glowing samples and return to the base pad.';roverHud();roverDraw()});document.getElementById('roverReset').addEventListener('click',()=>roverReset(true));document.querySelectorAll('[data-rover-dir]').forEach(b=>{b.addEventListener('click',()=>roverMove(b.dataset.roverDir));});window.addEventListener('keydown',e=>{if(['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','w','a','s','d','W','A','S','D'].includes(e.key)&&roverState.active){e.preventDefault();const k=e.key.toLowerCase();roverMove(k==='arrowup'||k==='w'?'up':k==='arrowdown'||k==='s'?'down':k==='arrowleft'||k==='a'?'left':'right')}});window.addEventListener('resize',roverResize,{passive:true});setTimeout(roverResize,80);
document.getElementById('saveBtn').addEventListener('click',()=>{if(!game){toast('Launch a mission before saving.');return}try{localStorage.setItem('juniorAstronautMissionSave',JSON.stringify({game,world}));toast('Mission saved on this device.')}catch(e){toast('Save failed in this browser.')}});
document.getElementById('loadBtn').addEventListener('click',()=>{try{const raw=localStorage.getItem('juniorAstronautMissionSave');if(!raw){toast('No saved mission found on this device.');return}const data=JSON.parse(raw);if(!data.game||!data.game.world)throw new Error('invalid save');game=data.game;world=data.world||game.world;document.querySelectorAll('[data-world]').forEach(b=>b.classList.toggle('selected',b.dataset.world===world));$('startOverlay').classList.add('hidden');$('endOverlay').classList.add('hidden');render();roverDraw();toast('Saved mission loaded.')}catch(e){toast('Could not load that save. Start a new mission.')}});

</script></body></html>"""

@app.route('/')
def home():
    return app.response_class(PAGE, mimetype='text/html')


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
