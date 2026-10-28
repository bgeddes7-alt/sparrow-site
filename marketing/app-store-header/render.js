const {chromium}=require('playwright');
(async()=>{
 const [,,mode,out]=process.argv;
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:(process.argv[4]==='search.html'?1280:823)},deviceScaleFactor:2});
 await p.goto('file://'+__dirname+'/'+(process.argv[4]||'header.html'));await p.evaluate(()=>document.fonts.ready);
 const times=mode==='test'?[0.2,1.6,5,10.4]:[...Array(360).keys()].map(i=>i/30);
 for(let k=0;k<times.length;k++){await p.evaluate(t=>render(t),times[k]);
  await p.screenshot({path:`${out}/f${String(k).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
 await b.close();
})();
