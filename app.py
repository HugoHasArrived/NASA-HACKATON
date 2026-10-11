from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Junior Astronaut Mission Trainer</title>
<style>
:root{--bg:#07111f;--panel:#101f33;--panel2:#142943;--line:#29435f;--text:#eef6ff;--muted:#9db2ca;--cyan:#55e6e0;--gold:#ffd166;--red:#ff6878;--green:#70e1a1}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at top,#172d49 0,#07111f 55%,#030812 100%);color:var(--text);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}button,select{font:inherit}button{cursor:pointer;border:1px solid #3c6386;background:#193653;color:var(--text);padding:10px 13px;border-radius:10px;font-weight:700;transition:.15s}button:hover{transform:translateY(-1px);border-color:var(--cyan);background:#214867}button:disabled{opacity:.35;cursor:not-allowed;transform:none}.primary{background:linear-gradient(135deg,#27b8c4,#357be0);border:0;color:#061421}.wrap{max-width:1250px;margin:auto;padding:22px}.top{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:18px}.brand{display:flex;align-items:center;gap:12px}.logo{width:48px;height:48px;border-radius:15px;background:linear-gradient(135deg,#3ddbd3,#477ce8);display:grid;place-items:center;font-size:26px;box-shadow:0 0 32px #36d4cf33}.eyebrow{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--cyan);font-weight:800}.title{font-size:clamp(22px,3vw,32px);font-weight:900;letter-spacing:-.8px}.muted{color:var(--muted)}.pill{border:1px solid var(--line);padding:7px 11px;border-radius:99px;color:var(--muted);font-size:12px}.layout{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(290px,.9fr);gap:16px}.panel{background:linear-gradient(160deg,#13263bfa,#0c1a2bfa);border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:0 12px 35px #0003;min-width:0}.panel h2{font-size:17px;margin:0 0 4px}.sub{font-size:12px;color:var(--muted);margin-bottom:14px}.scene{height:240px;border-radius:14px;overflow:hidden;position:relative;border:1px solid #304d69;background:linear-gradient(#081226 0%,#182a4b 58%,#6b5367 59%,#b08b73 100%);margin:14px 0}.stars{position:absolute;inset:0;background-image:radial-gradient(#fff 1px,transparent 1.5px),radial-gradient(#a8e8ff 1px,transparent 1.5px);background-size:53px 47px,79px 61px;background-position:8px 4px,27px 15px;opacity:.75}.planet{position:absolute;width:92px;height:92px;top:25px;right:12%;border-radius:50%;background:linear-gradient(130deg,#e5f4f7,#6796b9 60%,#365579);box-shadow:0 0 36px #8cd6ff44}.ground{position:absolute;left:-5%;right:-5%;height:105px;bottom:-20px;background:repeating-radial-gradient(ellipse at 40% 20%,#ad8b70 0 2px,#826c66 3px 5px,#695967 6px 9px);clip-path:polygon(0 25%,15% 8%,29% 22%,45% 4%,63% 26%,80% 10%,100% 20%,100% 100%,0 100%)}.base{position:absolute;bottom:49px;left:28%;width:190px;height:82px}.hab{position:absolute;bottom:0;left:25px;width:132px;height:65px;background:linear-gradient(#d7e1e7,#6e899c);border:3px solid #e5f4ff;border-radius:40px 40px 8px 8px;box-shadow:0 0 20px #72eaff33}.hab:before{content:"";position:absolute;left:12px;right:12px;top:12px;height:15px;background:repeating-linear-gradient(90deg,#16364e 0 19px,#9de7ed 20px 23px);border-radius:4px}.hab:after{content:"HABITAT 01";position:absolute;bottom:5px;left:0;right:0;text-align:center;color:#172a3c;font-size:9px;font-weight:900;letter-spacing:1px}.solar{position:absolute;bottom:10px;left:-52px;width:66px;height:45px;background:repeating-linear-gradient(90deg,#153d79 0 14px,#4d9bd1 15px 16px);border:2px solid #8bc5ee;transform:skewY(-12deg)}.solar:after{content:"";position:absolute;top:20px;left:0;right:0;border-top:2px solid #8bc5ee}.antenna{position:absolute;bottom:65px;left:90px;height:35px;border-left:3px solid #b8cbd9}.antenna:after{content:"";position:absolute;width:18px;height:18px;left:-10px;top:-7px;border:2px solid #b8cbd9;border-radius:50%}.scene-label{position:absolute;left:12px;top:12px;background:#07111fc9;border:1px solid #49617b;border-radius:8px;padding:5px 9px;font-size:11px;font-weight:800;letter-spacing:1px}.scene-status{position:absolute;right:12px;bottom:12px;background:#07111fc9;border-radius:8px;padding:6px 9px;font-size:11px}.resource-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}.resource{background:#0a1727;border:1px solid #263f59;border-radius:12px;padding:11px}.r-top{display:flex;justify-content:space-between;gap:5px;font-size:12px;color:var(--muted)}.r-value{font-size:22px;font-weight:850;margin:4px 0}.bar{height:5px;background:#24374b;border-radius:8px;overflow:hidden}.fill{height:100%;border-radius:8px;background:var(--cyan);transition:width .3s}.fill.warn{background:var(--gold)}.fill.danger{background:var(--red)}.section-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin:18px 0 10px}.actions{display:grid;grid-template-columns:1fr 1fr;gap:9px}.action{background:#10243a;border:1px solid #29445f;border-radius:12px;padding:12px;text-align:left;min-height:99px}.action strong{display:block;margin:5px 0;font-size:13px}.action small{display:block;color:var(--muted);font-size:11px;line-height:1.4}.action .ico{font-size:20px}.action:disabled{filter:grayscale(.6)}.side-stack{display:grid;gap:16px;align-content:start}.metric-row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #263b52;font-size:13px}.metric-row:last-child{border:0}.objective{display:flex;gap:9px;align-items:flex-start;font-size:13px;margin:12px 0}.check{width:19px;height:19px;border:1px solid #4a6a85;border-radius:6px;display:grid;place-items:center;flex-shrink:0;color:#061421;font-weight:900}.check.done{background:var(--green);border-color:var(--green)}.log{max-height:230px;overflow:auto;display:flex;flex-direction:column;gap:8px}.log-entry{border-left:2px solid #3c7599;background:#0b1929;padding:9px 11px;border-radius:0 8px 8px 0;font-size:12px;color:#c7d7e7}.log-entry.alert{border-color:var(--gold)}.log-entry.bad{border-color:var(--red)}.log-entry.good{border-color:var(--green)}.bottom{margin-top:16px;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:11px}.overlay{position:fixed;inset:0;background:#020713df;backdrop-filter:blur(8px);display:grid;place-items:center;padding:18px;z-index:5}.modal{width:min(650px,100%);background:#102139;border:1px solid #41607e;border-radius:22px;padding:26px;box-shadow:0 30px 90px #0008}.modal h1{font-size:clamp(28px,5vw,43px);line-height:1.06;margin:10px 0}.choices{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:18px 0}.choice{padding:14px;text-align:left}.choice.selected{border-color:var(--cyan);box-shadow:inset 0 0 0 1px var(--cyan);background:#1c3c51}.notice{padding:11px 13px;background:#112d3a;border:1px solid #245569;border-radius:11px;font-size:12px;color:#c9f8f5}.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#e8f9ff;color:#061421;padding:11px 16px;border-radius:11px;font-weight:800;box-shadow:0 8px 40px #0008;z-index:8;max-width:90vw;text-align:center}.danger-text{color:var(--red)}.green-text{color:var(--green)}.hidden{display:none!important}
@media(max-width:850px){.layout{grid-template-columns:1fr}.scene{height:220px}.resource-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.wrap{padding:13px}.panel{padding:14px}}@media(max-width:420px){.actions{grid-template-columns:1fr 1fr}.action{padding:10px}.choices{grid-template-columns:1fr}.title{font-size:21px}}
</style>
</head>
<body>
<div class="wrap">
 <header class="top">
  <div class="brand"><div class="logo">🚀</div><div><div class="eyebrow">STEM • SPACE EXPLORATION</div><div class="title">JUNIOR ASTRONAUT <span style="color:var(--cyan)">MISSION TRAINER</span></div></div></div>
  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><span class="pill" id="missionPill">MISSION NOT STARTED</span><button id="helpBtn">How to play ?</button><button id="resetBtn">↻ Restart</button></div>
 </header>
 <div class="layout">
  <main>
   <section class="panel">
    <div style="display:flex;justify-content:space-between;align-items:start;gap:10px"><div><h2 id="outpostTitle">Outpost overview</h2><div class="sub" id="planetSub">Your mission starts here.</div></div><span class="pill" id="dayPill">SOL 1 / 12</span></div>
    <div class="scene" aria-label="Illustrated space outpost"><div class="stars"></div><div class="planet" id="planet"></div><div class="ground"></div><div class="base"><div class="solar"></div><div class="antenna"></div><div class="hab"></div></div><div class="scene-label" id="sceneLabel">OUTPOST • ONLINE</div><div class="scene-status" id="sceneStatus">SYSTEMS NOMINAL</div></div>
    <div class="section-head"><h2>Life-support dashboard</h2><span class="muted" style="font-size:11px">Live mission telemetry</span></div>
    <div class="resource-grid" id="resources"></div>
    <div class="section-head"><h2>Engineering & operations</h2><span class="muted" style="font-size:11px">Choose wisely</span></div>
    <div class="actions" id="actions"></div>
   </section>
  </main>
  <aside class="side-stack">
   <section class="panel"><h2>Mission control</h2><div class="sub">Crew status and mission performance</div>
    <div class="metric-row"><span>Mission day</span><strong id="dayMetric">1 of 12</strong></div>
    <div class="metric-row"><span>Crew health</span><strong id="healthMetric">100%</strong></div>
    <div class="metric-row"><span>Morale</span><strong id="moraleMetric">85%</strong></div>
    <div class="metric-row"><span>Science points</span><strong id="scienceMetric">0</strong></div>
    <div class="metric-row"><span>Mission score</span><strong id="scoreMetric">0</strong></div>
    <div class="metric-row"><span>Mission status</span><strong id="statusMetric" class="green-text">OPERATIONAL</strong></div>
   </section>
   <section class="panel"><h2>Mission objectives</h2><div class="sub">Complete all goals to earn mission success</div><div id="objectives"></div></section>
   <section class="panel"><div class="section-head" style="margin-top:0"><h2>Mission log</h2><button id="clearLog" style="padding:5px 8px;font-size:11px">Clear</button></div><div class="log" id="log"></div></section>
   <section class="panel"><h2>Learning lab</h2><div class="sub">Why your choices matter</div><p style="font-size:13px;margin:0 0 10px">A real outpost must balance limited supplies, reliable power, crew health, and protection from radiation. Improving one system often uses resources needed by another.</p><div class="notice" id="lesson">Mission tip: Solar panels provide power, but storms can reduce their output. Keep a reserve.</div></section>
  </aside>
 </div>
 <footer class="bottom"><span>Independent educational prototype • Not an official NASA product</span><span>Designed for learning through decisions, experimentation, and teamwork</span></footer>
</div>
<div class="overlay" id="startOverlay">
 <div class="modal">
  <div class="eyebrow">MISSION BRIEFING // CADET TRAINING</div><h1>Could you keep a crew alive <span style="color:var(--cyan)">on another world?</span></h1>
  <p class="muted">Lead a junior exploration team. Make real trade-offs, protect your crew, and complete a 12-day outpost mission. Resources are limited, and every decision matters.</p>
  <h3>Choose your destination</h3>
  <div class="choices"><button class="choice selected" data-world="Moon"><span style="font-size:26px">🌕</span><br><strong>The Moon</strong><br><small class="muted">Short supply routes, long cold nights, no breathable air.</small></button><button class="choice" data-world="Mars"><span style="font-size:26px">🔴</span><br><strong>Mars</strong><br><small class="muted">Dust storms, remote resupply, challenging conditions.</small></button></div>
  <div class="notice">Training objective: survive 12 mission days, keep crew health above zero, and complete your outpost goals. This is a simplified educational simulation.</div>
  <button class="primary" id="startBtn" style="width:100%;margin-top:16px;padding:14px">LAUNCH TRAINING MISSION →</button>
 </div>
</div>
<div class="overlay hidden" id="endOverlay"><div class="modal"><div class="eyebrow">MISSION DEBRIEF</div><h1 id="endTitle">Mission complete</h1><p id="endText" class="muted"></p><div id="debriefStats"></div><button class="primary" id="againBtn" style="width:100%;margin-top:18px;padding:13px">FLY ANOTHER MISSION ↻</button></div></div>
<div class="overlay hidden" id="helpOverlay"><div class="modal"><div class="eyebrow">CADET FIELD GUIDE</div><h1>How to play</h1><p><b>1. Watch your resources.</b> Oxygen, water, food, power, shielding, and spare parts are limited.</p><p><b>2. Choose an operation.</b> Repair systems, grow food, reinforce radiation shielding, research, or rest. Actions use resources and advance time.</p><p><b>3. Prepare for emergencies.</b> A solar event or equipment failure may happen. Save spare parts and power for emergencies.</p><p><b>4. Learn from trade-offs.</b> A successful mission requires planning—not simply upgrading everything.</p><p class="muted">This is a fictional learning game, not a precise engineering simulator or NASA software.</p><button class="primary" id="closeHelp" style="width:100%">BACK TO MISSION</button></div></div>
<div id="toast" class="toast hidden"></div>
<script>
const $=id=>document.getElementById(id);
const defs=[
 {key:'oxygen',name:'Oxygen',icon:'🫁',unit:'units',max:100,desc:'Breathable air reserve'},
 {key:'water',name:'Water',icon:'💧',unit:'L',max:120,desc:'Drinking and hygiene'},
 {key:'food',name:'Food',icon:'🥫',unit:'meals',max:100,desc:'Crew food stores'},
 {key:'power',name:'Power',icon:'⚡',unit:'%',max:100,desc:'Stored electrical energy'},
 {key:'shield',name:'Radiation shield',icon:'🛡️',unit:'%',max:100,desc:'Protection from radiation'},
 {key:'parts',name:'Spare parts',icon:'🔩',unit:'parts',max:30,desc:'Repair supplies'}
];
const actionDefs=[
 {id:'solar',icon:'☀️',name:'Tune solar array',desc:'Gain power and science. Storms may still interfere.',cost:{parts:1},effect:s=>{s.power+=23;s.science+=2;return 'Solar array tuned: stored power increased.'},lesson:'Solar arrays generate electricity, but batteries help bridge periods when sunlight is weak or unavailable.'},
 {id:'repair',icon:'🧰',name:'Repair life support',desc:'Restore oxygen reliability and use spare parts.',cost:{parts:3,power:5},effect:s=>{s.oxygen+=23;s.health+=4;return 'Life-support maintenance completed.'},lesson:'Preventive maintenance can be more valuable than waiting for a failure. Repairs consume parts that may be needed later.'},
 {id:'farm',icon:'🌱',name:'Tend food greenhouse',desc:'Produce food and improve crew morale.',cost:{water:8,power:8},effect:s=>{s.food+=23;s.morale+=5;s.science+=3;return 'Greenhouse produced fresh food and new experiment data.'},lesson:'Growing food in space can reduce resupply needs, but plants require water, energy, nutrients, and careful monitoring.'},
 {id:'shield',icon:'🛡️',name:'Reinforce shelter',desc:'Improve radiation protection with spare parts.',cost:{parts:4,power:4},effect:s=>{s.shield+=17;s.score+=5;return 'Radiation shielding improved.'},lesson:'Shielding mass and material matter. Water and other hydrogen-rich materials can help reduce some radiation exposure, but no simple shield removes all risk.'},
 {id:'research',icon:'🔬',name:'Run science experiment',desc:'Earn science points and mission score.',cost:{power:10},effect:s=>{s.science+=10;s.score+=8;s.morale+=2;return 'Experiment completed. Data transmitted to mission control.'},lesson:'Science competes with life support for power and crew time. Good mission planning balances discovery with safety.'},
 {id:'rest',icon:'🛌',name:'Crew rest period',desc:'Recover health and morale; time still passes.',cost:{food:3,water:3},effect:s=>{s.health+=10;s.morale+=12;return 'Crew completed a rest period and wellness check.'},lesson:'Crew wellbeing is a mission system too. Sleep, food, hydration, and morale can affect performance.'},
 {id:'water',icon:'♻️',name:'Recycle water',desc:'Use power to recover water from the habitat.',cost:{power:9},effect:s=>{s.water+=20;s.score+=2;return 'Water recovery system processed a new batch.'},lesson:'Water recovery reduces the amount that must be launched from Earth, but recycling equipment needs energy and maintenance.'},
 {id:'drill',icon:'🚨',name:'Emergency systems drill',desc:'Train the crew and improve readiness.',cost:{power:5,food:2},effect:s=>{s.morale+=4;s.score+=4;s.science+=1;return 'Crew completed emergency response training.'},lesson:'Practice helps teams respond quickly when alarms sound. Drills take time and supplies but can reduce mistakes during real emergencies.'}
];
let state=null, world='Moon', toastTimer;
function clamp(n,min=0,max=100){return Math.max(min,Math.min(max,n))}
function startMission(){
 state={world,day:1,oxygen:84,water:88,food:82,power:78,shield:world==='Moon'?60:52,parts:12,health:100,morale:85,science:0,score:0,done:{solar:false,repair:false,farm:false,shield:false,research:false},log:[],ended:false};
 $('startOverlay').classList.add('hidden');$('endOverlay').classList.add('hidden');
 addLog('Mission control: outpost systems are online. Your 12-day training mission begins.','good');
 addLog(world==='Moon'?'Destination: lunar outpost. Watch power reserves through the long night.':'Destination: Mars outpost. Dust storms may reduce solar generation.','');
 render();toast('Mission launched. Good luck, commander!');
}
function addLog(msg,type=''){if(!state)return;state.log.unshift({msg,type,day:state.day});state.log=state.log.slice(0,24)}
function toast(msg){$('toast').textContent=msg;$('toast').classList.remove('hidden');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').classList.add('hidden'),2400)}
function costText(cost){return Object.entries(cost).map(([k,v])=>`${v} ${k}`).join(' · ')}
function canAfford(cost){return Object.entries(cost).every(([k,v])=>state[k]>=v)}
function doAction(id){
 if(!state||state.ended)return;
 const a=actionDefs.find(x=>x.id===id);if(!canAfford(a.cost)){toast('Not enough resources. Try another operation.');addLog('Operation blocked: insufficient resources for '+a.name+'.','alert');render();return}
 for(const [k,v] of Object.entries(a.cost))state[k]-=v;
 a.effect(state);
 for(const k of ['oxygen','water','food','power','shield','health','morale'])state[k]=clamp(state[k]);
 state.parts=clamp(state.parts,0,30);state.science=Math.max(0,state.science);state.score=Math.max(0,state.score);
 addLog(a.effect?state.log.length>=0?'Operation: '+a.name+' — '+a.lesson:'':'', 'good');
 // Replace the generic entry with the operation outcome.
 state.log[0].msg='Operation: '+a.name+' completed. '+a.lesson;
 $('lesson').textContent='Learning point: '+a.lesson;
 advanceDay();
}
function advanceDay(){
 if(state.ended)return;
 state.day++;
 // Daily consumption makes conservation and production important.
 state.oxygen-=7;state.water-=8;state.food-=7;state.power-=6;
 if(state.world==='Mars'&&Math.random()<.26){state.power-=12;addLog('MARS DUST STORM: solar output fell. Stored power dropped.','alert');}
 if(state.world==='Moon'&&state.day%4===0){state.power-=8;addLog('LUNAR NIGHT CONDITIONS: energy demand is high. Conserve power.','alert');}
 if(Math.random()<.22){
  const event=Math.random();
  if(event<.34){state.oxygen-=9;addLog('ALERT: oxygen valve fault detected. Repair life support soon.','bad');}
  else if(event<.67){state.parts=Math.max(0,state.parts-2);state.power-=5;addLog('ALERT: equipment fault consumed spare parts and power.','alert');}
  else{state.shield-=7;addLog('SOLAR PARTICLE EVENT: shelter protection is being tested.','bad');}
 }
 if(state.oxygen<25||state.water<20||state.food<20||state.power<12)state.health-=10;
 if(state.shield<30&&Math.random()<.65)state.health-=6;
 if(state.oxygen<=0||state.water<=0||state.food<=0||state.power<=0)state.health-=15;
 state.health=clamp(state.health);state.morale=clamp(state.morale- (state.food<25?7:2));
 if(state.day>1)addLog('Daily check: supplies consumed; review reserves before the next operation.','');
 if(state.health<=0){endMission(false,'The crew could not maintain safe living conditions. Review your reserves, repairs, and emergency planning.');return}
 if(state.day>12){const completed=Object.values(state.done).filter(Boolean).length;const success=state.health>=45&&state.oxygen>0&&state.water>0&&state.food>0&&completed>=3;endMission(success,success?'Your crew completed the 12-day mission with functioning life support and key objectives achieved.':'The crew reached the end of the training window, but several systems or objectives need improvement.');return}
 render();
}
function render(){
 if(!state)return;
 $('missionPill').textContent=state.ended?'MISSION ENDED':'MISSION ACTIVE';$('dayPill').textContent=`SOL ${Math.min(state.day,12)} / 12`;
 $('outpostTitle').textContent=state.world==='Moon'?'Lunar Research Outpost':'Martian Research Outpost';
 $('planetSub').textContent=state.world==='Moon'?'Lunar surface • Low gravity • No breathable atmosphere':'Mars surface • Thin atmosphere • Dust storm risk';
 $('sceneLabel').textContent=(state.world==='Moon'?'LUNAR':'MARTIAN')+' OUTPOST • ONLINE';
 $('sceneStatus').textContent=state.power<20?'LOW POWER WARNING':state.oxygen<25?'OXYGEN RESERVE LOW':state.shield<30?'RADIATION ALERT':'SYSTEMS NOMINAL';
 $('planet').style.background=state.world==='Moon'?'linear-gradient(130deg,#e5f4f7,#6796b9 60%,#365579)':'linear-gradient(130deg,#f2bc8d,#b95f4c 60%,#6d343a)';
 $('dayMetric').textContent=`${Math.min(state.day,12)} of 12`;$('healthMetric').textContent=state.health+'%';$('moraleMetric').textContent=state.morale+'%';$('scienceMetric').textContent=state.science;$('scoreMetric').textContent=state.score;
 $('statusMetric').textContent=state.health<35?'CRITICAL':state.power<15?'LOW POWER':'OPERATIONAL';$('statusMetric').className=state.health<35||state.power<15?'danger-text':'green-text';
 $('resources').innerHTML=defs.map(d=>{let v=Math.round(state[d.key]);let pct=clamp(v/d.max*100);return `<div class="resource"><div class="r-top"><span>${d.icon} ${d.name}</span><span>${d.unit}</span></div><div class="r-value">${v}</div><div class="bar"><div class="fill ${pct<25?'danger':pct<48?'warn':''}" style="width:${pct}%"></div></div><div style="font-size:10px;color:var(--muted);margin-top:6px">${d.desc}</div></div>`}).join('');
 $('actions').innerHTML=actionDefs.map(a=>{let ok=canAfford(a.cost);return `<button class="action" data-action="${a.id}" ${ok?'':'disabled'}><span class="ico">${a.icon}</span><strong>${a.name}</strong><small>${a.desc}</small><small style="margin-top:7px;color:${ok?'#80dcd9':'#ff9aa5'}">Cost: ${costText(a.cost)||'none'}</small></button>`}).join('');
 document.querySelectorAll('[data-action]').forEach(b=>b.addEventListener('click',()=>doAction(b.dataset.action)));
 const goals=[['solar','Stabilize electrical power'],['repair','Maintain life support'],['farm','Produce food locally'],['shield','Improve radiation protection'],['research','Complete a science experiment']];
 $('objectives').innerHTML=goals.map(([k,t])=>`<div class="objective"><div class="check ${state.done[k]?'done':''}">${state.done[k]?'✓':''}</div><div><strong>${t}</strong><div class="muted" style="font-size:11px">${state.done[k]?'Completed':'Use the matching operation to complete'}</div></div></div>`).join('');
 // Objective completion is based on having used the operation, tracked below by operation log.
 for(const k of Object.keys(state.done))if(state.log.some(e=>e.msg.startsWith('Operation: '+({solar:'Tune solar array',repair:'Repair life support',farm:'Tend food greenhouse',shield:'Reinforce shelter',research:'Run science experiment'}[k])+' completed')))state.done[k]=true;
 $('objectives').innerHTML=goals.map(([k,t])=>`<div class="objective"><div class="check ${state.done[k]?'done':''}">${state.done[k]?'✓':''}</div><div><strong>${t}</strong><div class="muted" style="font-size:11px">${state.done[k]?'Completed':'Use the matching operation to complete'}</div></div></div>`).join('');
 $('log').innerHTML=state.log.map(e=>`<div class="log-entry ${e.type}"><div style="font-size:10px;color:#86a8c7;margin-bottom:3px">DAY ${Math.min(e.day,12)} • MISSION CONTROL</div>${e.msg}</div>`).join('')||'<div class="muted">No messages yet.</div>';
}
function endMission(success,reason){
 state.ended=true;render();$('endOverlay').classList.remove('hidden');
 $('endTitle').textContent=success?'MISSION SUCCESS':'MISSION FAILED';$('endTitle').style.color=success?'var(--green)':'var(--red)';
 $('endText').textContent=reason;
 $('debriefStats').innerHTML=`<div class="metric-row"><span>Destination</span><strong>${state.world}</strong></div><div class="metric-row"><span>Crew health remaining</span><strong>${state.health}%</strong></div><div class="metric-row"><span>Science points</span><strong>${state.science}</strong></div><div class="metric-row"><span>Objectives completed</span><strong>${Object.values(state.done).filter(Boolean).length} / 5</strong></div><div class="metric-row"><span>Final score</span><strong>${state.score}</strong></div>`;
 addLog(success?'MISSION CONTROL: mission objectives achieved. Well done, commander.':'MISSION CONTROL: mission ended. Study the log and try a new strategy. ',success?'good':'bad');
}
document.querySelectorAll('[data-world]').forEach(b=>b.addEventListener('click',()=>{world=b.dataset.world;document.querySelectorAll('[data-world]').forEach(x=>x.classList.toggle('selected',x===b))}));
$('startBtn').addEventListener('click',startMission);$('resetBtn').addEventListener('click',()=>{$('startOverlay').classList.remove('hidden');$('endOverlay').classList.add('hidden')});$('againBtn').addEventListener('click',()=>{$('endOverlay').classList.add('hidden');$('startOverlay').classList.remove('hidden')});
$('helpBtn').addEventListener('click',()=>$('helpOverlay').classList.remove('hidden'));$('closeHelp').addEventListener('click',()=>$('helpOverlay').classList.add('hidden'));$('clearLog').addEventListener('click',()=>{if(state){state.log=[];render()}});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/health")
def health():
    return {"status": "ok", "app": "Junior Astronaut Mission Trainer"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)))
