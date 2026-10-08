from flask import Flask

app = Flask(__name__)

PAGE = r'''<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Metroidvania: Ruinas del Alba</title>
    <style>
        :root { color-scheme: dark; --ink:#f5edda; --gold:#f2c66d; --panel:#171b27; }
        * { box-sizing:border-box }
        body { margin:0; min-height:100vh; display:grid; place-items:center; padding:20px;
            background:radial-gradient(ellipse at top,#29334a,#10131c 65%); color:var(--ink);
            font:16px/1.45 system-ui,sans-serif }
        main { width:min(900px,100%); text-align:center }
        h1 { margin:0; color:var(--gold); letter-spacing:.08em; font-size:clamp(1.7rem,5vw,2.6rem) }
        .sub { margin:4px 0 16px; color:#b5bdcd }
        .layout { display:grid; grid-template-columns:minmax(0,640px) 210px; gap:14px; align-items:start; justify-content:center }
        canvas { width:100%; height:auto; display:block; border:2px solid #596078; border-radius:10px;
            background:#111522; box-shadow:0 12px 36px #0008; image-rendering:pixelated }
        aside { background:var(--panel); border:1px solid #3c4356; border-radius:10px; padding:14px; text-align:left }
        .stat { display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid #303647 }
        .stat strong { color:var(--gold) }
        #message { min-height:66px; margin:12px 0; color:#d8d3c7 }
        button { width:100%; border:0; border-radius:7px; padding:10px; margin:4px 0; cursor:pointer;
            color:#211a10; background:var(--gold); font-weight:800 }
        button:hover { filter:brightness(1.12) }
        .help { color:#aeb5c4; font-size:.87rem; margin-top:12px }
        .mobile { display:none; grid-template-columns:repeat(3,1fr); gap:5px; margin-top:10px }
        .mobile button { margin:0; min-height:42px }
        @media(max-width:720px) { .layout { grid-template-columns:1fr } aside { display:grid; grid-template-columns:1fr 1fr; gap:0 12px }
            aside h2,.help,#message { grid-column:1/-1 } .mobile { display:grid } }
    </style>
</head>
<body>
<main>
    <h1>RUINAS DEL ALBA</h1>
    <p class="sub">Un metroidvania: explora, salta, combate y consigue cristales para abrir la salida.</p>
    <div class="layout">
        <section>
            <canvas id="game" width="640" height="512" aria-label="Mundo de plataformas"></canvas>
            <div class="mobile" aria-label="Controles táctiles">
                <span></span><button onpointerdown="press('jump')">▲</button><span></span>
                <button onpointerdown="press('left')" onpointerup="release('left')" onpointerleave="release('left')">◀</button>
                <button onclick="attack()">⚔</button>
                <button onpointerdown="press('right')" onpointerup="release('right')" onpointerleave="release('right')">▶</button>
                <span></span><button onpointerdown="press('jump')" onpointerup="release('jump')" onpointerleave="release('jump')">▼</button><span></span>
            </div>
        </section>
        <aside>
            <h2 style="margin:0 0 6px;color:var(--gold)">Exploradora</h2>
            <div class="stat"><span>Vida</span><strong id="hp">♥♥♥♥♥</strong></div>
            <div class="stat"><span>Zona</span><strong id="floor">1</strong></div>
            <div class="stat"><span>Cristales</span><strong id="gold">0/3</strong></div>
            <div class="stat"><span>Enemigos</span><strong id="foes">0</strong></div>
            <p id="message">Explora las ruinas, recoge los 3 cristales y encuentra el portal.</p>
            <button onclick="attack()">Atacar (X)</button>
            <button onclick="newGame()">Nueva partida</button>
            <p class="help">Mover: A/D o flechas · Saltar: W, ↑ o espacio<br>Atacar: X · Explora plataformas y recoge cristales.</p>
        </aside>
    </div>
</main>
<script>
const canvas=document.getElementById('game'),ctx=canvas.getContext('2d');
const tile=32, worldW=100, worldH=16, keys={};
let map,player,enemies,crystals,zone,shards,ended,camera=0,lastTime=0;
const solid=(x,y)=>y>=worldH||x<0||x>=worldW||y<0||map[y][x]===1;
function say(text){document.getElementById('message').textContent=text;}
function newGame(){zone=1;shards=0;ended=false;player={x:48,y:400,w:20,h:28,vx:0,vy:0,hp:5,max:5,face:1,onGround:false,invuln:0,attack:0};makeZone();say('Explora las ruinas, recoge los 3 cristales y encuentra el portal.');}
function makeZone(){
    map=Array.from({length:worldH},()=>Array(worldW).fill(0));
    for(let x=0;x<worldW;x++){map[15][x]=1;if(x%19===0&&x>0)map[14][x]=1;}
    for(const [x,y,len] of [[8,12,6],[18,10,7],[29,12,8],[39,9,7],[51,12,7],[62,10,8],[73,12,8],[84,9,8]])
        for(let i=0;i<len;i++)map[y][x+i]=1;
    // Cada zona ofrece varias alturas para explorar y rutas de salto.
    crystals=[[12,11],[43,8],[77,11]].map(([x,y],i)=>({x:x+((zone-1)%3)*2,y:y,taken:false}));
    enemies=[{x:23*tile,y:14*tile-24,min:20*tile,max:28*tile,vx:45,hp:2},{x:56*tile,y:14*tile-24,min:52*tile,max:61*tile,vx:-55,hp:2},{x:82*tile,y:14*tile-24,min:78*tile,max:87*tile,vx:50,hp:2}];
    player.x=48;player.y=400;player.vx=0;player.vy=0;camera=0;updateUI();
}
function press(key){keys[key]=true;if(key==='jump'&&player.onGround&&!ended){player.vy=-430;player.onGround=false;}}
function release(key){keys[key]=false;}
function attack(){if(!ended)player.attack=.22;}
function updateUI(){document.getElementById('hp').textContent='♥'.repeat(Math.max(0,player.hp))+'♡'.repeat(player.max-player.hp);document.getElementById('floor').textContent=zone;document.getElementById('gold').textContent=shards+'/3';document.getElementById('foes').textContent=enemies.length;}
function hitWall(x,y,w,h){return solid(Math.floor(x/tile),Math.floor(y/tile))||solid(Math.floor((x+w-1)/tile),Math.floor(y/tile))||solid(Math.floor(x/tile),Math.floor((y+h-1)/tile))||solid(Math.floor((x+w-1)/tile),Math.floor((y+h-1)/tile));}
function tick(dt){
    if(ended)return;
    player.vx=(keys.left?-1:0)+(keys.right?1:0);player.vx*=190;if(player.vx)player.face=Math.sign(player.vx);
    player.vy=Math.min(560,player.vy+1000*dt);
    player.x+=player.vx*dt;if(hitWall(player.x,player.y,player.w,player.h))player.x-=player.vx*dt;
    player.y+=player.vy*dt;player.onGround=false;
    if(hitWall(player.x,player.y,player.w,player.h)){player.y-=player.vy*dt;if(player.vy>0)player.onGround=true;player.vy=0;}
    player.x=Math.max(0,Math.min(worldW*tile-player.w,player.x));
    if(player.y>canvas.height+80){player.hp--;player.x=48;player.y=350;player.vy=0;say('¡Cuidado con las caídas!');}
    if(player.invuln>0)player.invuln-=dt;if(player.attack>0)player.attack-=dt;
    for(const e of enemies){e.x+=e.vx*dt;if(e.x<e.min||e.x>e.max)e.vx*=-1;
        if(overlap(player.x,player.y,player.w,player.h,e.x,e.y,24,24)&&player.invuln<=0){player.hp--;player.invuln=1;say('Un guardián te ha golpeado.');}}
    if(player.attack>0){const ax=player.face>0?player.x+player.w:player.x-26;
        for(const e of enemies)if(overlap(ax,player.y+4,26,player.h-8,e.x,e.y,24,24))e.hp-=dt*8;}
    enemies=enemies.filter(e=>e.hp>0);
    for(const c of crystals)if(!c.taken&&overlap(player.x,player.y,player.w,player.h,c.x*tile,c.y*tile,20,20)){c.taken=true;shards++;say('¡Cristal antiguo recogido! '+shards+'/3');}
    if(player.hp<=0){player.hp=0;ended=true;say('Has caído en las ruinas. Pulsa Nueva partida para volver a intentarlo.');}
    const portalX=(worldW-3)*tile;
    if(player.x>portalX-12){if(shards>=3){zone++;shards=0;player.hp=Math.min(player.max,player.hp+1);makeZone();say('¡Portal abierto! Has llegado a la zona '+zone+'.');}else{player.x=portalX-20;say('El portal está sellado: necesitas los 3 cristales.');}}
    camera=Math.max(0,Math.min(worldW*tile-canvas.width,player.x-canvas.width*.42));updateUI();
}
function overlap(ax,ay,aw,ah,bx,by,bw,bh){return ax<bx+bw&&ax+aw>bx&&ay<by+bh&&ay+ah>by;}
function draw(){
    const bg=ctx.createLinearGradient(0,0,0,canvas.height);bg.addColorStop(0,'#18263a');bg.addColorStop(1,'#493653');ctx.fillStyle=bg;ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.save();ctx.translate(-camera,0);
    for(let y=0;y<worldH;y++)for(let x=Math.floor(camera/tile);x<Math.ceil((camera+canvas.width)/tile);x++)if(map[y][x]){ctx.fillStyle='#354457';ctx.fillRect(x*tile,y*tile,tile-2,tile-2);ctx.fillStyle='#526579';ctx.fillRect(x*tile,y*tile,tile-2,5);}
    for(const c of crystals)if(!c.taken){ctx.fillStyle='#77f2e1';ctx.beginPath();ctx.moveTo(c.x*tile+10,c.y*tile);ctx.lineTo(c.x*tile+21,c.y*tile+10);ctx.lineTo(c.x*tile+10,c.y*tile+22);ctx.lineTo(c.x*tile,c.y*tile+10);ctx.closePath();ctx.fill();}
    const px=(worldW-3)*tile;ctx.fillStyle=shards>=3?'#f2c66d':'#935a94';ctx.fillRect(px,14*tile,28,32);ctx.fillStyle='#fff0b0';ctx.fillRect(px+10,14*tile+8,8,16);
    for(const e of enemies){ctx.fillStyle='#da6474';ctx.fillRect(e.x,e.y,24,24);ctx.fillStyle='#fff';ctx.fillRect(e.x+5,e.y+6,4,4);ctx.fillRect(e.x+15,e.y+6,4,4);}
    if(!(player.invuln>0&&Math.floor(performance.now()/90)%2)){ctx.fillStyle='#f2c66d';ctx.fillRect(player.x,player.y,player.w,player.h);ctx.fillStyle='#31465c';ctx.fillRect(player.x+4,player.y+6,12,9);}
    if(player.attack>0){ctx.strokeStyle='#fff0a6';ctx.lineWidth=4;ctx.beginPath();ctx.arc(player.x+player.w/2+player.face*17,player.y+14,20,-1,1);ctx.stroke();}
    ctx.restore();ctx.fillStyle='#ffffffcc';ctx.font='14px system-ui';ctx.fillText('ZONA '+zone+'  •  CRISTALES '+shards+'/3',14,24);
}
function frame(time){const dt=Math.min((time-lastTime)/1000||0,.033);lastTime=time;tick(dt);draw();requestAnimationFrame(frame);}
document.addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(['arrowleft','arrowright','arrowup',' ','w','a','d','x'].includes(k))e.preventDefault();if(k==='arrowleft'||k==='a')press('left');if(k==='arrowright'||k==='d')press('right');if(k==='arrowup'||k==='w'||k===' ')press('jump');if(k==='x'&&!e.repeat)attack();if(k==='r')newGame();});
document.addEventListener('keyup',e=>{const k=e.key.toLowerCase();if(k==='arrowleft'||k==='a')release('left');if(k==='arrowright'||k==='d')release('right');if(k==='arrowup'||k==='w'||k===' ')release('jump');});
newGame();requestAnimationFrame(frame);
</script>
</body>
</html>'''


@app.route('/')
def hello_world():
        return PAGE


if __name__ == '__main__':
        app.run(debug=True)