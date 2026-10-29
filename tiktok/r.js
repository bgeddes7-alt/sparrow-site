const {chromium}=require('playwright');const n=process.argv[2];(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.cwd()+'/'+n+'.html');await p.waitForTimeout(500);
for(let i=1;i<=7;i++){await (await p.$('#s'+i)).screenshot({path:'/mnt/user-data/outputs/sparrow-'+n+'-slide-'+i+'.png'})}await b.close()})()
