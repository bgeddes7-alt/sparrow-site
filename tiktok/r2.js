// node r2.js 10  -> renders every <section> in 10.html to out/sparrow-10-slide-N.png
const {chromium}=require('playwright');const n=process.argv[2];(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.cwd()+'/'+n+'.html');await p.waitForTimeout(600);
const s=await p.$$('section');for(let i=0;i<s.length;i++){await s[i].screenshot({path:'out/sparrow-'+n+'-slide-'+(i+1)+'.png'})}console.log(n,s.length);await b.close()})()
