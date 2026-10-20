// Sparrow tiles widget, served as an MCP Apps UI resource (text/html;profile=mcp-app).
// Vanilla JS, tile art drawn inline (same art as the Sparrow app), no external loads.
export const WIDGET_URI = "ui://sparrow/tiles-v1.html";

export const WIDGET_HTML = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--bg:#FFFFFF;--surface:#F7F5FA;--ink:#1E1A36;--muted:#6B6688;--line:#E2DDEC;--accent:#DB3F73;--accent-ink:#fff;--good:#23845A;--bad:#C9343A;
 --display:Georgia,"Times New Roman",serif;--body:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
:root.dark{--bg:#212121;--surface:#2B2840;--ink:#F1EEFA;--muted:#A39EC2;--line:#3B3560;--accent:#F2648F;--accent-ink:#1A0A12;--good:#45B37F;--bad:#EF6167}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 var(--body)}
.wrap{padding:14px;display:flex;flex-direction:column;gap:12px}
h1{font:400 19px var(--display);margin:0;letter-spacing:-.01em}
h3{font:400 16px var(--display);margin:0}
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.code{font:800 20px var(--body);letter-spacing:.05em;margin-top:2px}
.note{font-size:12.5px;color:var(--muted);margin:0}
.box{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:9px}
.row{display:flex;align-items:center;justify-content:space-between;gap:8px}
.pill{font-size:11px;font-weight:700;border-radius:99px;padding:3px 8px;background:var(--bg);border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.pill.go{color:var(--good);border-color:var(--good)}
.groups{display:flex;flex-wrap:wrap;gap:12px 14px}
.grp{display:flex;flex-direction:column;gap:5px}
.grp i{font-style:normal;font-size:11px;color:var(--muted);font-weight:600}
ul{margin:0;padding-left:18px;font-size:13px}ul li{margin:2px 0}
.btn{appearance:none;border:0;border-radius:12px;padding:11px 14px;font:700 14px var(--body);cursor:pointer;background:var(--accent);color:var(--accent-ink);width:100%}
.empty{color:var(--muted);padding:18px 0;text-align:center}
/* tiles: faces stay ivory in any theme, like real tiles */
.tile{--tb:#23845A;--tc:#C9343A;--td:#2B58C9;--tk:#1E1A36;--tg:#B07A0C;position:relative;flex:0 0 auto;width:30px;height:41px;border-radius:5px;background:#FFFDF7;
 border:1px solid #D9D2BE;box-shadow:0 2px 0 #BDB39A,0 3px 6px rgba(20,16,40,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;
 color:var(--tk);line-height:1;font-family:var(--body)}
.tile .art{position:absolute;inset:0;width:100%;height:100%}
.tile .s{font-size:6.5px;font-weight:800;letter-spacing:.05em;margin-top:2px}
.tile .glyph{font-size:18px;font-weight:700}
.tile.R .glyph{color:var(--tc)}.tile.G .glyph{color:var(--tb)}
.tile.O .soap{width:15px;height:22px;border:2.2px solid var(--td);border-radius:3px}
.tile.F .glyph{color:#C2457F;font-size:19px}
.tile.J{background:linear-gradient(160deg,#FFF6D9,#FFFDF7)}.tile.J .glyph{color:var(--tg);font-size:15px}.tile.J .s{color:var(--tg)}
.tile.dim{opacity:.35}
.tile.pass{box-shadow:0 2px 0 var(--bad),0 0 0 2px var(--bad)}
.tiles{display:flex;flex-wrap:wrap;gap:5px 3px}
.gap{width:7px}
.flip{animation:flip .35s ease-out both}
@keyframes flip{from{transform:rotateY(80deg);opacity:0}to{transform:none}}
@media (prefers-reduced-motion:reduce){.flip{animation:none}}
</style></head><body>
<div class="wrap" id="app"><div class="empty">Laying out the tiles...</div></div>
<script>
(function(){
var APP="https://apps.apple.com/app/id6819738312";
var SUITS={B:"Bam",C:"Crak",D:"Dot"};
var HON={N:"North",E:"East",W:"West",S:"South",R:"Red Dragon",G:"Green Dragon",O:"Soap",F:"Flower",J:"Joker"};
var PIPS={1:[[17,25]],2:[[17,15],[17,35]],3:[[10,13],[17,25],[24,37]],4:[[11,15],[23,15],[11,35],[23,35]],
 5:[[11,13],[23,13],[17,25],[11,37],[23,37]],6:[[11,12],[23,12],[11,25],[23,25],[11,38],[23,38]],
 7:[[9,10],[17,14],[25,18],[11,29],[23,29],[11,39],[23,39]],8:[[11,10],[23,10],[11,20],[23,20],[11,30],[23,30],[11,40],[23,40]],
 9:[[9,12],[17,12],[25,12],[9,25],[17,25],[25,25],[9,38],[17,38],[25,38]]};
var CN=["","\\u4e00","\\u4e8c","\\u4e09","\\u56db","\\u4e94","\\u516d","\\u4e03","\\u516b","\\u4e5d"];
function name(c){return SUITS[c[0]]&&c.length===2?c[1]+" "+SUITS[c[0]]:(HON[c]||c)}
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function art(su,n){var g="",P=PIPS[n];
 if(su==="D"){var r=n===1?9:n<=4?5.2:n<=6?4.4:3.7;P.forEach(function(p,i){var col=(n===1||(n===5&&i===2)||(n===9&&i>=3&&i<=5))?"#C9343A":(n>=7&&i<3?"#23845A":"#2B58C9");
   g+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="'+r+'" fill="none" stroke="'+col+'" stroke-width="1.6"/><circle cx="'+p[0]+'" cy="'+p[1]+'" r="'+(r*0.42)+'" fill="'+col+'"/>'})}
 else if(su==="B"){if(n===1){g='<path d="M9 30c2-9 9-13 15-10l3-2-1 4c1 7-5 12-12 11l-4 4 1-5c-1-1-2-1-2-2z" fill="#23845A"/><path d="M14 27c3-2 6-2 9 0" stroke="#C9343A" stroke-width="1.5" fill="none"/><circle cx="22" cy="22" r="1.2" fill="#FFFDF7"/>'}
  else{var h=n<=4?14:n<=6?10:8.5;P.forEach(function(p,i){var col=((n===5&&i===2)||(n===9&&i>=3&&i<=5)||(n===7&&i===0))?"#C9343A":"#23845A";
   g+='<rect x="'+(p[0]-1.8)+'" y="'+(p[1]-h/2)+'" width="3.6" height="'+h+'" rx="1.6" fill="'+col+'"/><rect x="'+(p[0]-2.2)+'" y="'+(p[1]-0.6)+'" width="4.4" height="1.2" fill="#FFFDF7"/>'})}}
 else{g='<text x="17" y="21" text-anchor="middle" font-size="14" font-weight="700" fill="#1E1A36" font-family="serif">'+CN[n]+'</text><text x="17" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="#C9343A" font-family="serif">\\u842c</text>'}
 return '<svg class="art" viewBox="0 0 34 46" aria-hidden="true">'+g+'<text x="3.2" y="8.2" font-size="6.5" font-weight="800" fill="#1E1A36" font-family="system-ui,sans-serif">'+n+'</text></svg>'}
var di=0;
function tile(c,cls){var k,inner;
 if(SUITS[c[0]]&&c.length===2){k=c[0];inner=art(c[0],+c[1])}
 else if("NEWS".indexOf(c)>-1&&c.length===1){k="H";inner='<span class="glyph">'+c+'</span><span class="s">WIND</span>'}
 else if(c==="R"){k="R";inner='<span class="glyph">\\u4e2d</span><span class="s" style="color:var(--tc)">RED</span>'}
 else if(c==="G"){k="G";inner='<span class="glyph">\\u767c</span><span class="s" style="color:var(--tb)">GREEN</span>'}
 else if(c==="O"){k="O";inner='<span class="soap"></span>'}
 else if(c==="F"){k="F";inner='<span class="glyph">\\u273f</span><span class="s" style="color:#C2457F">FLOWER</span>'}
 else{k="J";inner='<span class="glyph">\\u2605</span><span class="s">JOKER</span>'}
 return '<div class="tile flip '+k+' '+(cls||"")+'" style="animation-delay:'+Math.min(0.6,(di++)*0.025).toFixed(2)+'s" role="img" aria-label="'+esc(name(c))+'">'+inner+'</div>'}
function groupTiles(groups){return groups.map(function(g){var s="";for(var i=0;i<g.k;i++)s+=tile(g.t);return s}).join('<span class="gap"></span>')}
var cta='<button class="btn" id="cta">Practice it in Sparrow</button>';

function viewLine(d){
 var h='<div><div class="eyebrow">Card line</div><h1>'+esc(d.title||"Your card line")+'</h1>'+(d.line?'<div class="code">'+esc(d.line)+'</div>':'')+'</div>';
 h+='<div class="box"><div class="groups">'+d.groups.map(function(g){var s="";for(var i=0;i<g.k;i++)s+=tile(g.t);
   return '<div class="grp"><div class="tiles">'+s+'</div><i>'+esc(g.label)+' \\u00b7 '+esc(g.name)+'</i></div>'}).join("")+'</div>'+
   '<div class="row"><span class="note">14 tiles</span><span class="pill">'+(d.concealed?"Concealed":"Exposures OK")+'</span></div></div>';
 h+='<ul>'+(d.notes||[]).map(function(n){return '<li>'+esc(n)+'</li>'}).join("")+'</ul>';
 return h+cta+'<p class="note">Sparrow teaches you to read any card, then lets you practice real hands against bots.</p>'}

function viewRack(d){
 var pl=d.passes.slice();
 var h='<div><div class="eyebrow">Rack check</div><h1>Your best shot</h1></div>';
 h+='<div class="box"><div class="tiles">'+d.rack.map(function(t){var i=pl.indexOf(t);if(i>-1)pl.splice(i,1);return tile(t,i>-1?"pass":"")}).join("")+'</div>'+
   (d.passes.length?'<p class="note">Red outline: pass these first in the Charleston. Never pass a joker.</p>':'<p class="note">Every tile helps your top hand.</p>')+'</div>';
 d.best.forEach(function(b,i){
  h+='<div class="box"><div class="row"><h3>'+(i+1)+'. '+esc(b.name)+'</h3><span class="pill'+(i===0?" go":"")+'">'+b.have+' of 14</span></div>'+
   '<div class="tiles">'+b.tiles.map(function(x){return tile(x.t,x.have?"":"dim")}).join("")+'</div>'+
   '<p class="note">'+esc(b.rule)+(b.need?' Needs '+b.need+' more.':' You have it!')+(b.jokers_used?' Counts '+b.jokers_used+' joker'+(b.jokers_used>1?'s':'')+'.':'')+'</p></div>'});
 return h+cta+'<p class="note">Faded tiles are the ones you still need. Based on Sparrow\\'s practice card. In Sparrow Plus you can load your own card.</p>'}

function viewCard(d){
 var h='<div><div class="eyebrow">Sparrow practice card</div><h1>'+(d.hands.length===1?esc(d.hands[0].name):"Hands to learn on")+'</h1></div>';
 d.hands.forEach(function(x){h+='<div class="box"><div class="row"><h3>'+esc(x.name)+'</h3><span class="pill">'+x.pts+' pts</span></div>'+
   '<div class="tiles">'+groupTiles(x.groups)+'</div><p class="note">'+esc(x.rule)+(x.ways>1?' One of '+x.ways+' ways to make it.':'')+'</p></div>'});
 return h+cta+'<p class="note">Original practice hands for learning how a card works. Not the official League card.</p>'}

var data=null,lastSig=null;
function render(){var app=document.getElementById("app");di=0;
 if(!data){app.innerHTML='<div class="empty">Laying out the tiles...</div>';return}
 app.innerHTML=data.mode==="rack"?viewRack(data):data.mode==="card"?viewCard(data):viewLine(data);
 var b=document.getElementById("cta");if(b)b.onclick=openApp;size()}
function load(sc){if(!sc||!sc.mode)return;var sig=JSON.stringify(sc);if(sig===lastSig)return;lastSig=sig;data=sc;render()}

var pending={},nextId=1;
function rpc(m,p){var id=nextId++;try{window.parent.postMessage({jsonrpc:"2.0",id:id,method:m,params:p},"*")}catch(e){}
 return new Promise(function(res,rej){pending[id]={res:res,rej:rej};setTimeout(function(){if(pending[id]){delete pending[id];rej(new Error("timeout"))}},8000)})}
function notify(m,p){try{window.parent.postMessage({jsonrpc:"2.0",method:m,params:p},"*")}catch(e){}}
function openApp(){var u=(data&&data.app_url)||APP;rpc("ui/open-link",{url:u}).catch(function(){if(window.openai&&window.openai.openExternal){try{window.openai.openExternal({href:u})}catch(e){}}})}
function size(){var b=document.documentElement;notify("ui/notifications/size-changed",{width:b.scrollWidth,height:b.scrollHeight})}
if(window.ResizeObserver)new ResizeObserver(size).observe(document.body);
function theme(t){if(!t)t=(window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches)?"dark":"light";document.documentElement.classList.toggle("dark",t==="dark")}

window.addEventListener("message",function(ev){if(ev.source!==window.parent)return;var m=ev.data;if(!m||m.jsonrpc!=="2.0")return;
 if(m.id!==undefined&&pending[m.id]&&!m.method){var p=pending[m.id];delete pending[m.id];m.error?p.rej(m.error):p.res(m.result);return}
 if(m.method==="ui/notifications/tool-result")load(m.params&&m.params.structuredContent);
 else if(m.method==="ui/notifications/host-context-changed"){if(m.params&&m.params.theme)theme(m.params.theme)}
 else if(m.method==="ui/resource-teardown"&&m.id!==undefined){try{window.parent.postMessage({jsonrpc:"2.0",id:m.id,result:{}},"*")}catch(e){}}
},{passive:true});
theme(window.openai&&window.openai.theme);
rpc("ui/initialize",{protocolVersion:"2026-01-26",appInfo:{name:"Sparrow",version:"1.0.0"},appCapabilities:{availableDisplayModes:["inline"]}})
 .then(function(r){if(r&&r.hostContext&&r.hostContext.theme)theme(r.hostContext.theme);notify("ui/notifications/initialized",{})}).catch(function(){});
var tries=0;(function poll(){if(data)return;var o=window.openai&&window.openai.toolOutput;if(o&&o.mode){load(o);return}if(tries++<40)setTimeout(poll,150)})();
window.addEventListener("openai:set_globals",function(){var o=window.openai&&window.openai.toolOutput;if(o&&o.mode)load(o);if(window.openai&&window.openai.theme)theme(window.openai.theme)});
})();
</script></body></html>`;
