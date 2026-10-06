import os, json, sys, shutil, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tiles import row, tile
from guides import GUIDES

MODE = sys.argv[1] if len(sys.argv) > 1 else "prod"   # prod = clean URLs, preview = .html links
OUT = os.path.join(ROOT, "site" if MODE == "prod" else "preview")
DOMAIN = "https://sparrowmahjong.app"
APP_URL = "https://apps.apple.com/app/id6819738312"
EMAIL = "brian@geddes.ventures"
UPDATED = "October 6, 2026"
TODAY = "2026-10-06"
INDEXNOW = "9c4e1f7a2b8d4e63a51f0c7d2e9b4a18"

def L(path, depth):
    """path like 'index', 'privacy', 'guides/x', 'guides/index'"""
    if MODE == "prod":
        if path == "index": return "/"
        if path.endswith("/index"): return "/" + path[:-5]
        return "/" + path
    pre = "../" * depth
    return pre + path + ".html"

def canon(path):
    if path == "index": return DOMAIN + "/"
    if path.endswith("/index"): return DOMAIN + "/" + path[:-5]
    return DOMAIN + "/" + path

def asset(p, depth): return ("/" + p) if MODE == "prod" else ("../" * depth + p)

CSS = r"""
@font-face{font-family:"Young Serif";src:url(/fonts/youngserif-400.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:Figtree;src:url(/fonts/figtree-400.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:Figtree;src:url(/fonts/figtree-600.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:Figtree;src:url(/fonts/figtree-800.woff2) format("woff2");font-weight:800;font-display:swap}
:root{--bg:#F2EFF6;--card:#FFFFFF;--ink:#1E1A36;--muted:#5E5873;--line:#E2DCEA;--accent:#DB3F73;--accent-d:#B92D5C;--gold:#C98B12;--cream:#FBF6EA;--bam:#23845A;--crak:#C9343A;--dot:#2B58C9;--night:#1E1A36}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15121F;--card:#1F1B2E;--ink:#F3EFFA;--muted:#B3ACC6;--line:#332D47;--cream:#2A2433;--night:#0E0B16}}
:root[data-theme="dark"]{--bg:#15121F;--card:#1F1B2E;--ink:#F3EFFA;--muted:#B3ACC6;--line:#332D47;--cream:#2A2433;--night:#0E0B16}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 Figtree,system-ui,-apple-system,sans-serif}
a{color:var(--accent)}a:hover{color:var(--accent-d)}
h1,h2,h3{font-family:"Young Serif",Georgia,serif;font-weight:400;line-height:1.15;letter-spacing:-.01em}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}.narrow{max-width:720px}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;background:var(--card);padding:8px 12px;z-index:9}
header.top{position:sticky;top:0;z-index:5;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;gap:16px;height:62px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font:400 22px "Young Serif",serif}
.brand img{width:34px;height:34px;border-radius:9px}
nav.links{margin-left:auto;display:flex;gap:18px;align-items:center}
nav.links a{color:var(--ink);text-decoration:none;font-weight:600;font-size:15px}
nav.links a.btn{color:#fff}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--accent);color:#fff;text-decoration:none;font-weight:800;padding:12px 20px;border-radius:999px;border:0;font-size:16px}
.btn:hover{background:var(--accent-d);color:#fff}
.btn.sm{padding:8px 14px;font-size:14px}
.btn.ghost{background:transparent;color:var(--ink);border:2px solid var(--line)}
.appstore{display:inline-flex;align-items:center;gap:10px;background:#000;color:#fff;text-decoration:none;border-radius:12px;padding:10px 18px 10px 14px}
.appstore:hover{color:#fff;opacity:.9}.appstore svg{width:26px;height:26px}
.appstore small{display:block;font-size:11px;line-height:1}.appstore b{display:block;font-size:20px;line-height:1.1;font-weight:600}
.hero{padding:56px 0 24px;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}
.eyebrow{font-size:13px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.hero h1{font-size:clamp(40px,6vw,68px);margin:.2em 0 .25em}
.hero p.lead{font-size:20px;color:var(--muted);max-width:30em;margin:0 0 26px}
.hero .ctas{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.hero .note{font-size:14px;color:var(--muted);margin-top:14px}
.phones{position:relative;height:560px}
.phones img{position:absolute;width:260px;border-radius:28px;box-shadow:0 30px 60px rgba(30,26,54,.25)}
.phones img:nth-child(1){left:0;top:30px;transform:rotate(-5deg)}
.phones img:nth-child(2){right:0;top:0;transform:rotate(4deg)}
.tilestrip{display:flex;gap:8px;margin:0 0 18px}
section.band{padding:64px 0}
section.band h2{font-size:clamp(30px,4vw,44px);margin:0 0 12px}
section.band p.sub{color:var(--muted);font-size:19px;max-width:36em;margin:0 0 32px}
.days{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;list-style:none;padding:0;margin:0}
.days li{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px}
.days b{display:block;font-family:"Young Serif",serif;font-weight:400;font-size:20px;margin:4px 0}
.days span.d{font-size:12px;font-weight:800;letter-spacing:.1em;color:var(--accent);text-transform:uppercase}
.days li.free{border-color:var(--accent)}
.days p{margin:0;color:var(--muted);font-size:15px}
.dark{background:var(--night);color:#F3EFFA}.dark p.sub{color:#D4CDE6}
.split{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.split img{width:100%;max-width:340px;border-radius:26px;justify-self:center;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.checks{list-style:none;padding:0;margin:0}.checks li{padding:8px 0 8px 32px;position:relative}
.checks li:before{content:"";position:absolute;left:0;top:13px;width:18px;height:18px;border-radius:50%;background:var(--accent);box-shadow:inset 0 0 0 5px color-mix(in srgb,var(--accent) 60%,#fff)}
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.plan{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:24px;position:relative}
.plan.best{border:2px solid var(--accent)}
.plan .tag{position:absolute;top:-12px;left:20px;background:var(--accent);color:#fff;font-size:12px;font-weight:800;padding:3px 10px;border-radius:999px}
.plan h3{margin:0;font-size:22px}.plan .price{font:800 34px Figtree,sans-serif;margin:8px 0 0}.plan .per{color:var(--muted);font-size:15px}
.plan p{color:var(--muted);font-size:15px;margin:10px 0 0}
.free-box{margin-top:18px;background:var(--cream);border-radius:16px;padding:16px 20px;font-size:16px}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:4px 18px;margin:0 0 10px}
.faq summary{cursor:pointer;font-weight:600;padding:12px 0;list-style:none}.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";float:right;color:var(--accent);font-weight:800}.faq details[open] summary:after{content:"–"}
.faq details p{margin:0 0 14px;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.gcard{display:block;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px;text-decoration:none;color:var(--ink)}
.gcard:hover{border-color:var(--accent)}
.gcard h3{margin:0 0 8px;font-size:21px}.gcard p{margin:0;color:var(--muted);font-size:15px}
footer{border-top:1px solid var(--line);padding:40px 0 60px;margin-top:40px;font-size:14px;color:var(--muted)}
footer .cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}
footer a{color:var(--muted);text-decoration:none;display:block;padding:3px 0}footer a:hover{color:var(--accent)}
footer h4{color:var(--ink);margin:0 0 8px;font-size:14px}
article.doc{padding:40px 0 20px}
article.doc h1{font-size:clamp(34px,5vw,50px);margin:.2em 0 .4em}
article.doc h2{font-size:28px;margin:1.6em 0 .4em}
article.doc h3{font-size:21px;margin:1.4em 0 .3em}
article.doc p.lede{font-size:20px;line-height:1.55;background:var(--card);border-left:4px solid var(--accent);padding:16px 20px;border-radius:0 14px 14px 0}
article.doc .meta{color:var(--muted);font-size:14px}
article.doc table{width:100%;border-collapse:collapse;font-size:15px;margin:12px 0}
article.doc td,article.doc th{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
article.doc th{background:var(--card)}
.crumbs{font-size:14px;color:var(--muted);padding-top:22px}.crumbs a{color:var(--muted)}
.appbox{display:flex;gap:16px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px;margin:32px 0}
.appbox img{width:64px;height:64px;border-radius:15px}.appbox p{margin:0;font-size:15px;color:var(--muted)}.appbox b{color:var(--ink)}
/* tiles */
.tilerow{margin:22px 0}.tilerow figcaption{font-size:14px;color:var(--muted);margin-top:8px}
.tiles{display:flex;flex-wrap:wrap;gap:10px}.grp{display:flex;gap:4px}
.tile{--tb:#23845A;--tc:#C9343A;--td:#2B58C9;--tg:#B07A0C;position:relative;display:inline-flex;flex-direction:column;align-items:center;justify-content:center;width:40px;height:54px;background:#FFFDF7;border-radius:7px;box-shadow:0 3px 0 #BDB39A,0 5px 10px rgba(20,16,40,.12);color:#1E1A36;font-family:Figtree,sans-serif;line-height:1}
.tile .art{position:absolute;inset:0;width:100%;height:100%}
.tile .glyph{font-size:21px;font-weight:700}.tile .s{font-size:7px;font-weight:800;letter-spacing:.06em;margin-top:3px}
.tile .red,.tile.R .glyph{color:var(--tc)}.tile .grn,.tile.G .glyph{color:var(--tb)}.tile .flw,.tile.F .glyph{color:#C2457F}
.tile.O .soap{width:18px;height:26px;border:2.5px solid var(--td);border-radius:3px}
.tile.J{background:linear-gradient(160deg,#FFF6D9,#FFFDF7)}.tile.J .glyph{color:var(--tg);font-size:17px}.tile.J .s{color:var(--tg)}
.tile.lg{width:62px;height:84px;border-radius:10px}.tile.lg .glyph{font-size:34px}.tile.lg .s{font-size:10px}.tile.lg.O .soap{width:28px;height:42px;border-width:4px}
@media (max-width:820px){
 .hero .wrap,.split{grid-template-columns:1fr}.phones{height:440px;max-width:420px;margin:0 auto;width:100%}
 .phones img{width:205px}.plans{grid-template-columns:1fr}footer .cols{grid-template-columns:1fr 1fr}
 nav.links a:not(.btn){display:none}.hero{padding-top:32px}
}
@media (max-width:400px){.phones img{width:170px}.phones{height:370px}}
"""

APPLE = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.4 1.2 9.8.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.1-.8 1.5 0 1.9.8 3.2.8 1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.5-1-2.5-3.9zM14 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.1-.6 2.8-1.4z"/></svg>'

def appstore(): return f'<a class="appstore" href="{APP_URL}" rel="noopener">{APPLE}<span><small>Download on the</small><b>App Store</b></span></a>'

def page(path, title, desc, body, depth=0, jsonld=None, og_type="website"):
    lds = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    css_href = asset("style.css", depth)
    t = title if "Sparrow" in title else f"{title} | Sparrow"
    body = re.sub(r"\{L:([^}]+)\}", lambda m: L(m.group(1), depth), body)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{canon(path)}">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon(path)}"><meta property="og:image" content="{DOMAIN}/img/og.png"><meta property="og:site_name" content="Sparrow">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#DB3F73">
<meta name="apple-itunes-app" content="app-id=6819738312">
<link rel="icon" href="{asset('favicon.png', depth)}" type="image/png"><link rel="apple-touch-icon" href="{asset('apple-touch-icon.png', depth)}">
<link rel="stylesheet" href="{css_href}">{lds}
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
<a class="brand" href="{L('index', depth)}"><img src="{asset('img/icon-512.png', depth)}" alt="" width="34" height="34">Sparrow</a>
<nav class="links" aria-label="Main"><a href="{L('index', depth)}#course">The course</a><a href="{L('index', depth)}#pricing">Pricing</a><a href="{L('guides/index', depth)}">Guides</a><a href="{L('support', depth)}">Help</a><a class="btn sm" href="{APP_URL}" rel="noopener">Get the app</a></nav>
</div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><div class="cols">
<div><a class="brand" href="{L('index', depth)}" style="color:var(--ink)"><img src="{asset('img/icon-512.png', depth)}" alt="" width="34" height="34">Sparrow</a>
<p>Learn American mahjong in private, then go play real games. Made by Geddes Ventures LLC.</p>
<p>Sparrow is not affiliated with or endorsed by the National Mah Jongg League. The practice card in the app is made of original hands.</p></div>
<div><h4>Learn</h4><a href="{L('guides/index', depth)}">All guides</a>""" + "".join(f'<a href="{L("guides/"+g["slug"], depth)}">{g["title"].replace("What is the difference between American and Chinese mahjong?","American vs Chinese mahjong")}</a>' for g in GUIDES[:4]) + f"""</div>
<div><h4>Company</h4><a href="{L('support', depth)}">Help and contact</a><a href="{L('subscriptions', depth)}">Subscriptions</a><a href="{L('privacy', depth)}">Privacy</a><a href="{L('terms', depth)}">Terms</a><a href="{L('delete-data', depth)}">Delete my data</a><a href="{L('accessibility', depth)}">Accessibility</a></div>
</div><p style="margin-top:28px">© 2026 Geddes Ventures LLC. Apple and App Store are trademarks of Apple Inc.</p></div></footer>
</body></html>"""
    fn = os.path.join(OUT, path + ".html")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, "w").write(html)

ORG = {"@type": "Organization", "name": "Geddes Ventures LLC", "url": DOMAIN, "email": EMAIL}

# ------------------------------------------------------------------ landing
DAYS = [("Day 1","How mahjong works","The whole game in two minutes, with real tiles moving on screen.",True),
        ("Day 2","Spot the tiles","Bams, craks, dots, winds and dragons. You will name them at a glance.",False),
        ("Day 3","Jokers and the rules","Where jokers can go and where they can't. The rule that loses most beginner games.",False),
        ("Day 4","Read the card","Turn any line on the card into the tiles it means.",False),
        ("Day 5","The Charleston","What to pass, when, and why you keep your pairs.",False),
        ("Day 6","Calling and exposing","How to take a discard without holding up the table.",False),
        ("Day 7","Mahj night ready","Table manners and a full dress rehearsal.",False),
        ("Any time","Brush up","Four quick reminders and a warm up hand before you head out.",False)]

LFAQ = [("Who is Sparrow for?","People who have never played American mahjong, or played once and forgot everything. It skips the frills and gets you ready for a real table."),
        ("Is this the official National Mah Jongg League card?","No. Sparrow comes with a practice card of original hands. If you have Sparrow Plus, you can photograph your own official card and practice with its lines. Sparrow is not affiliated with the League."),
        ("Do I need an account?","No. There is no sign up and no email. Your progress stays tied to your phone."),
        ("What is free?","Day one of the course and one full practice hand. Everything else is Sparrow Plus."),
        ("Can I cancel the free trial?","Yes. Cancel in your iPhone Settings under your name, then Subscriptions, at least a day before the trial ends and you will not be charged."),
        ("Does Sparrow teach Chinese or Riichi mahjong?","No. Sparrow only teaches the American game played with a yearly card.")]

hero_tiles = "".join(tile(c, "lg") for c in ["B5", "C3", "D6", "R", "J"])
landing = f"""
<section class="hero"><div class="wrap">
<div><div class="tilestrip" aria-hidden="true">{hero_tiles}</div>
<span class="eyebrow">American mahjong for total beginners</span>
<h1>Learn mahjong in seven days.</h1>
<p class="lead">Short daily lessons, then a practice table where you play real hands against three players. Make your call, then see what an expert would have done. Learn it in private, then go play real games.</p>
<div class="ctas">{appstore()}<a class="btn ghost" href="#course">See the course</a></div>
<p class="note">Free to start. iPhone only.</p></div>
<div class="phones"><img src="img/01-home.jpg" alt="Sparrow home screen showing day 1 of 7" width="540" height="1170"><img src="img/04-table_expert.jpg" alt="The practice table with expert advice on a discard" width="540" height="1170"></div>
</div></section>

<section class="band" id="course"><div class="wrap">
<span class="eyebrow">The course</span><h2>Five minutes a day. One week.</h2>
<p class="sub">Each day is a short lesson with real tiles and a quick check at the end. Most days finish with a practice hand so it sticks.</p>
<ol class="days">{"".join(f'<li class="{"free" if f else ""}"><span class="d">{d}{" · free" if f else ""}</span><b>{t}</b><p>{p}</p></li>' for d,t,p,f in DAYS)}</ol>
</div></section>

<section class="band dark"><div class="wrap split">
<div><span class="eyebrow">Practice table</span><h2>Play as many hands as you want.</h2>
<p class="sub">Every deal is new. You go through the Charleston, draw, discard and call against three players who play to win.</p>
<ul class="checks"><li>Decide on your own, then review every move after the hand.</li><li>Stuck? Tap the expert for the best discard and the reason behind it.</li><li>Practice with the built in card, or photograph your own card and use real lines.</li><li>Nobody watching. Nobody waiting on you.</li></ul></div>
<img src="img/03-table_review.jpg" alt="A hand review showing each discard next to the expert's choice" width="540" height="1170" loading="lazy">
</div></section>

<section class="band" id="pricing"><div class="wrap">
<span class="eyebrow">Pricing</span><h2>Sparrow Plus</h2>
<p class="sub">All seven days, the brush up lesson, unlimited practice hands, the expert on every move, and your own card.</p>
<div class="plans">
<div class="plan best"><span class="tag">7 days free</span><h3>Yearly</h3><div class="price">$39.99</div><div class="per">per year, about $3.33 a month</div><p>Try everything free for a week. Cancel before the week ends and pay nothing.</p></div>
<div class="plan"><h3>Monthly</h3><div class="price">$7.99</div><div class="per">per month</div><p>Good if mahj night is a short season for you.</p></div>
<div class="plan"><h3>Lifetime</h3><div class="price">$79.99</div><div class="per">one time</div><p>Pay once and keep it.</p></div>
</div>
<div class="free-box"><b>Free forever:</b> day one of the course and one full practice hand. No account needed. Prices are in US dollars and may vary by country. See <a href="{{L:subscriptions}}">subscription details</a>.</div>
</div></section>

<section class="band"><div class="wrap narrow faq">
<span class="eyebrow">Questions</span><h2>Before you download</h2>
{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in LFAQ)}
<p style="margin-top:24px">New to the game? Start with <a href="{{L:guides/how-to-learn-american-mahjong-fast}}">how to learn American mahjong fast</a>.</p>
</div></section>
"""
page("index", "Sparrow: Learn American Mahjong in 7 Days",
     "A seven day American mahjong course for total beginners, with a practice table where an expert reviews every move. For iPhone.",
     landing, 0, [
        {"@context": "https://schema.org", "@type": "MobileApplication", "name": "Sparrow: Learn Mahjong", "operatingSystem": "iOS",
         "applicationCategory": "EducationalApplication", "url": DOMAIN, "installUrl": APP_URL,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "publisher": ORG},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in LFAQ]}])

# ------------------------------------------------------------------ guides
def appbox(depth):
    return f'<div class="appbox"><img src="{asset("img/icon-512.png", depth)}" alt="" width="64" height="64"><p><b>Sparrow</b> teaches American mahjong to total beginners in seven short days, with unlimited practice hands. <a href="{L("index", depth)}">See how it works</a>.</p></div>'

for gd in GUIDES:
    faq_html = "<h2>Quick answers</h2><div class=\"faq\">" + "".join(f"<details open><summary>{q}</summary><p>{a}</p></details>" for q, a in gd["faq"]) + "</div>"
    body = f"""<div class="wrap narrow"><div class="crumbs"><a href="{{L:index}}">Sparrow</a> / <a href="{{L:guides/index}}">Guides</a></div>
<article class="doc"><h1>{gd['title']}</h1><p class="meta">Updated {gd['date']} · by Brian Geddes, maker of Sparrow</p>
<p class="lede">{gd['lede']}</p>{gd['body']}{faq_html}{appbox(1)}
<h2>More guides</h2><div class="cards">""" + "".join(f'<a class="gcard" href="{{L:guides/{o["slug"]}}}"><h3>{o["title"]}</h3></a>' for o in GUIDES if o is not gd)[:100000] + "</div></article></div>"
    page("guides/" + gd["slug"], gd["title"], gd["desc"], body, 1, [
        {"@context": "https://schema.org", "@type": "Article", "headline": gd["title"], "description": gd["desc"],
         "datePublished": gd["date"], "dateModified": gd.get("modified", gd["date"]),
         "author": {"@type": "Person", "name": "Brian Geddes"}, "publisher": ORG,
         "mainEntityOfPage": canon("guides/" + gd["slug"]), "image": DOMAIN + "/img/og.png"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in gd["faq"]]}], "article")

gi = """<div class="wrap"><article class="doc"><span class="eyebrow">Guides</span><h1>American mahjong, answered</h1>
<p class="sub" style="color:var(--muted);font-size:19px;max-width:36em">Plain answers to the questions new players ask before their first game. A new one goes up most weeks.</p><div class="cards">""" + \
     "".join(f'<a class="gcard" href="{{L:guides/{g["slug"]}}}"><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES) + "</div></article></div>"
page("guides/index", "American Mahjong Guides for Beginners", "Plain answers to the questions new American mahjong players ask, from reading the card to the Charleston and jokers.", gi, 1)

# ------------------------------------------------------------------ legal
from legal import LEGAL
for path, title, desc, html in LEGAL(EMAIL, UPDATED, APP_URL):
    page(path, title, desc, f'<div class="wrap narrow"><article class="doc">{html}</article></div>', 0)

page("404", "Page not found", "This page does not exist.",
     '<div class="wrap narrow"><article class="doc"><h1>That tile is not in the set.</h1><p>The page you wanted is gone or never existed. Try the <a href="{L:index}">home page</a> or the <a href="{L:guides/index}">guides</a>.</p></article></div>', 0)

# ------------------------------------------------------------------ static files
css = CSS if MODE == "prod" else CSS.replace("url(/fonts/", "url(fonts/")
open(os.path.join(OUT, "style.css"), "w").write(css)
for d in ["img", "fonts"]:
    src = os.path.join(ROOT, "build", "assets") + "/" + d
    shutil.copytree(src, os.path.join(OUT, d), dirs_exist_ok=True)
for f in ["favicon.png", "apple-touch-icon.png"]:
    shutil.copy(os.path.join(ROOT, "build", "assets") + "/" + f, OUT)

if MODE == "prod":
    urls = ["index", "guides/index"] + ["guides/" + g["slug"] for g in GUIDES] + ["support", "subscriptions", "privacy", "terms", "delete-data", "accessibility"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{canon(u)}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "Googlebot"]
    open(os.path.join(OUT, "robots.txt"), "w").write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    llms = f"# Sparrow\n\n> Sparrow is an iPhone app that teaches American mahjong (the National Mah Jongg League style, with a yearly card, jokers and the Charleston) to total beginners in seven short daily lessons, plus an unlimited practice table with an expert who reviews every move. Made by Geddes Ventures LLC. Not affiliated with the National Mah Jongg League.\n\n- Free: day one and one practice hand. Sparrow Plus: $39.99 per year with a 7 day free trial, $7.99 per month, or $79.99 once.\n- No account, no ads, no tracking.\n- App Store: {APP_URL}\n\n## Guides\n\n" + \
           "".join(f"- [{g['title']}]({canon('guides/'+g['slug'])}): {g['desc']}\n" for g in GUIDES) + \
           f"\n## Policies\n\n- [Privacy]({canon('privacy')})\n- [Terms]({canon('terms')})\n- [Subscriptions]({canon('subscriptions')})\n- [Support]({canon('support')})\n"
    open(os.path.join(OUT, "llms.txt"), "w").write(llms)
    open(os.path.join(OUT, f"{INDEXNOW}.txt"), "w").write(INDEXNOW)
    open(os.path.join(OUT, "_headers"), "w").write("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  X-Frame-Options: SAMEORIGIN
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; script-src 'none'; frame-ancestors 'self'; base-uri 'self'; form-action 'none'
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/img/*
  Cache-Control: public, max-age=604800
""")
    open(os.path.join(OUT, "_redirects"), "w").write("/help /support 301\n/privacy-policy /privacy 301\n/delete /delete-data 301\n")
print("built", MODE, OUT)
