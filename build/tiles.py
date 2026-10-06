PIPS={1:[[17,25]],2:[[17,15],[17,35]],3:[[10,13],[17,25],[24,37]],4:[[11,15],[23,15],[11,35],[23,35]],
 5:[[11,13],[23,13],[17,25],[11,37],[23,37]],6:[[11,12],[23,12],[11,25],[23,25],[11,38],[23,38]],
 7:[[9,10],[17,14],[25,18],[11,29],[23,29],[11,39],[23,39]],8:[[11,10],[23,10],[11,20],[23,20],[11,30],[23,30],[11,40],[23,40]],
 9:[[9,12],[17,12],[25,12],[9,25],[17,25],[25,25],[9,38],[17,38],[25,38]]}
CN=["","一","二","三","四","五","六","七","八","九"]
SUITS={"B":"Bam","C":"Crak","D":"Dot"}
HON={"N":"North Wind","E":"East Wind","W":"West Wind","S":"South Wind","R":"Red Dragon","G":"Green Dragon","O":"White Dragon (Soap)","F":"Flower","J":"Joker"}

def art(su,n):
    g="";P=PIPS[n]
    if su=="D":
        r=9 if n==1 else 5.2 if n<=4 else 4.4 if n<=6 else 3.7
        for i,(x,y) in enumerate(P):
            col="#C9343A" if (n==1 or (n==5 and i==2) or (n==9 and 3<=i<=5)) else ("#23845A" if n>=7 and i<3 else "#2B58C9")
            g+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{col}" stroke-width="1.6"/><circle cx="{x}" cy="{y}" r="{r*0.42:.2f}" fill="{col}"/>'
    elif su=="B":
        if n==1:
            g='<path d="M9 30c2-9 9-13 15-10l3-2-1 4c1 7-5 12-12 11l-4 4 1-5c-1-1-2-1-2-2z" fill="#23845A"/><path d="M14 27c3-2 6-2 9 0" stroke="#C9343A" stroke-width="1.5" fill="none"/><circle cx="22" cy="22" r="1.2" fill="#FFFDF7"/>'
        else:
            h=14 if n<=4 else 10 if n<=6 else 8.5
            for i,(x,y) in enumerate(P):
                col="#C9343A" if ((n==5 and i==2) or (n==9 and 3<=i<=5) or (n==7 and i==0)) else "#23845A"
                g+=f'<rect x="{x-1.8:.1f}" y="{y-h/2:.1f}" width="3.6" height="{h}" rx="1.6" fill="{col}"/><rect x="{x-2.2:.1f}" y="{y-0.6:.1f}" width="4.4" height="1.2" fill="#FFFDF7"/>'
    else:
        g=f'<text x="17" y="21" text-anchor="middle" font-size="14" font-weight="700" fill="#1E1A36" font-family="serif">{CN[n]}</text><text x="17" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="#C9343A" font-family="serif">萬</text>'
    return f'<svg class="art" viewBox="0 0 34 46" aria-hidden="true">{g}<text x="3.2" y="8.2" font-size="6.5" font-weight="800" fill="#1E1A36" font-family="system-ui,sans-serif">{n}</text></svg>'

def name(c):
    if c[0] in SUITS and len(c)==2: return f"{c[1]} {SUITS[c[0]]}"
    return HON[c]

def tile(c,cls=""):
    if c[0] in SUITS and len(c)==2: k=c[0]; inner=art(c[0],int(c[1]))
    elif c in "NEWS": k="H"; inner=f'<span class="glyph">{c}</span><span class="s">WIND</span>'
    elif c=="R": k="R"; inner='<span class="glyph">中</span><span class="s red">RED</span>'
    elif c=="G": k="G"; inner='<span class="glyph">發</span><span class="s grn">GREEN</span>'
    elif c=="O": k="O"; inner='<span class="soap"></span>'
    elif c=="F": k="F"; inner='<span class="glyph">✿</span><span class="s flw">FLOWER</span>'
    else: k="J"; inner='<span class="glyph">★</span><span class="s">JOKER</span>'
    return f'<span class="tile {k} {cls}" role="img" aria-label="{name(c)}">{inner}</span>'

def row(codes,cap=None,cls=""):
    """codes: space separated; '|' starts a new group"""
    groups=[g.split() for g in codes.split("|")]
    html="".join('<span class="grp">'+"".join(tile(c) for c in g)+'</span>' for g in groups)
    c=f'<figcaption>{cap}</figcaption>' if cap else ""
    return f'<figure class="tilerow {cls}"><div class="tiles">{html}</div>{c}</figure>'
