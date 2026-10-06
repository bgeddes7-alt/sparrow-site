from tiles import row

GUIDES = []

def g(**k): GUIDES.append(k)

# ---------------------------------------------------------------- 1
g(slug="how-to-learn-american-mahjong-fast",
  title="How do you learn American mahjong fast?",
  desc="Learn the tiles, then the card, then the Charleston, and play real hands early. A short plan for total beginners with a mahj night coming up.",
  date="2026-10-04",
  lede="Learn the tiles first, then how to read the card, then the Charleston. After that, play real hands as soon as you can, even sloppy ones. Ten or fifteen minutes a day for a week will get a total beginner through a friendly game without holding everyone up.",
  body=f"""
<p>Your friend texts on a Monday. The group needs a fourth on Thursday. You have never touched a tile. This is the plan I would follow.</p>

<h2>Day one: what the game is</h2>
<p>American mahjong is a four player game played with 152 tiles. Everyone tries to build one exact hand printed on a card. You hold 13 tiles and win on the 14th. On each turn you pick a tile and throw one away. That is the whole loop.</p>
<p>The part that trips people up is the card. Players in other styles build sets freely. Here, your hand has to match a line on the card, tile for tile.</p>
{row("B3 B3 B3 | C5 C5 C5 | D7 D7 | J J J","A made-up hand: two sets of three, a pair, and three jokers filling a set.")}

<h2>Days two and three: tiles and jokers</h2>
<p>Learn to name tiles at a glance. There are three suits (bams, craks and dots), numbered 1 to 9. Then come the winds, the dragons, flowers and jokers. The white dragon is called Soap, and it doubles as a zero.</p>
<p>Jokers are where beginners lose games. A joker can fill any group of three or more. It can never stand in for a single tile or one tile of a pair. If you remember one rule from this page, make it that one.</p>

<h2>Day four: read the card</h2>
<p>Each line on the card is one possible hand. Colors tell you about suits inside that line. Same color means same suit. Different colors mean different suits. An X next to the hand means you can call discards to build it. A C means it has to stay hidden until you win. There is a full walkthrough in <a href="{{L:guides/how-to-read-the-mahjong-card}}">how to read the mahjong card</a>.</p>

<h2>Day five: the Charleston</h2>
<p>Before play starts, everyone passes tiles in a set pattern: right, across, left. A second round can follow. This is where you shape your hand, and where new players freeze. Pass what clearly does not fit. Keep pairs. Never pass a joker. More in <a href="{{L:guides/what-is-the-charleston-in-mahjong}}">what is the Charleston</a>.</p>

<h2>Days six and seven: play real hands</h2>
<p>Reading about mahjong only gets you so far. You need to see a rack of 13 random tiles and decide which hand to chase. The first dozen hands feel slow. Then you start to notice patterns, like how a rack full of 2s, 4s and 6s points you toward one section of the card.</p>
<p>Play against people who will wait for you, or practice alone where nobody is waiting. Either works. Doing nothing until Thursday does not.</p>

<h2>What you can skip for now</h2>
<p>Scoring details, betting, and the fine points of when you can call a tile for a pair. Your group will walk you through payment the first night. Every table has its own house rules anyway, so ask before you start.</p>

<p>I built <a href="{{L:index}}">Sparrow</a> for this exact week. It is a seven day course for people who have never played, with short lessons and a practice table where you can make a call and then see what an expert would have done. Day one and one practice hand are free.</p>
""",
  faq=[
   ("How long does it take to learn American mahjong?","Most beginners can play a slow, friendly game after a week of short daily practice. Feeling quick and confident takes a few months of regular games."),
   ("Do I need my own card to learn?","You need a current card to play with a group. For learning, any practice card works, since the reading skills carry over to the official one."),
   ("Is American mahjong harder than Chinese mahjong?","It has more rules up front because of the card and the Charleston. Many players find it easier once those click, because the card tells you exactly what to build."),
   ("What should I learn first?","The tiles and the joker rule. Jokers fill groups of three or more and never fill a single or a pair."),
  ])

# ---------------------------------------------------------------- 2
g(slug="what-is-the-charleston-in-mahjong",
  title="What is the Charleston in mahjong?",
  desc="The Charleston is the tile passing before American mahjong starts. Here is the order, the blind pass, and what to give away as a beginner.",
  date="2026-10-04",
  lede="The Charleston is a round of tile passing that happens before play starts in American mahjong. Everyone passes three tiles right, then across, then left. A second, optional round goes the other way, and it ends with a small courtesy pass across the table.",
  body=f"""
<p>Picture four people who each just got 13 random tiles. Most of those racks are a mess. The Charleston gives everyone a chance to clean theirs up before the first discard.</p>

<h2>The order of passes</h2>
<p>The first Charleston is required. You pass three tiles to the player on your right. Then three to the player across. Then three to your left.</p>
<p>The second Charleston is optional. If any one player wants to stop, it stops. If everyone agrees, you pass left, then across, then right.</p>
<p>Last comes the courtesy pass. You and the player across from you agree on a number from zero to three and swap that many tiles. If you each ask for a different number, the lower one wins.</p>

<h2>The blind pass</h2>
<p>On the last pass of each Charleston (the first left and the second right), you are allowed to pass tiles you just received without looking at them. It is called a blind pass or stealing. Beginners use it when they are holding a good rack and do not want to break it up.</p>

<h2>What to pass as a beginner</h2>
<p>Start by looking for two or three hands on the card that your rack could become. Then pass tiles that help none of them.</p>
{row("B1 | C9 | N","Lonely tiles like these are usually easy passes.")}
<p>Keep pairs. A pair is hard to rebuild once it is gone. Keep flowers if any of your target hands use them. Do not hang on to a tile just because it looks nice.</p>
<p>You can never pass a joker. If a joker lands in your rack, it stays there, which is good news for you.</p>

<h2>Reading what other people pass</h2>
<p>This is the part that takes longer. If the player on your left keeps sending you dragons, they probably are not building a dragon hand. If someone asks for zero on the courtesy pass, their rack is likely in good shape. You do not need any of this your first night. It is just nice to know that the passing gives information away in both directions.</p>

<h2>Common beginner mistakes</h2>
<ul>
<li>Passing a tile from a pair because you panicked on the clock.</li>
<li>Committing to one hand on the first pass and throwing away everything else.</li>
<li>Forgetting which direction you are on. Say it out loud. Everyone does.</li>
</ul>

<p>The Charleston is day five of the course in <a href="{{L:index}}">Sparrow</a>, and the practice table runs a full Charleston every hand. You can pick your passes and review them after, or ask the expert first.</p>
""",
  faq=[
   ("Is the second Charleston required?","No. Any player can stop the second Charleston. The first one always happens."),
   ("Can you pass a joker in the Charleston?","No. Jokers can never be passed during the Charleston."),
   ("What is a blind pass?","On the last pass of each Charleston, you may pass tiles you just received without looking at them."),
   ("How many tiles are in the courtesy pass?","Zero to three, agreed with the player across from you. If you ask for different numbers, you use the lower one."),
  ])

# ---------------------------------------------------------------- 3
g(slug="how-do-jokers-work-in-american-mahjong",
  title="How do jokers work in American mahjong?",
  desc="Jokers fill any group of three or more tiles, never a single or a pair. Here is how the joker swap works and why a discarded joker is dead.",
  date="2026-10-04",
  lede="A joker can stand in for any tile in a group of three or more matching tiles. It can never be used as a single tile or as part of a pair. There are eight jokers in an American set, and they are the most valuable tiles in the game.",
  body=f"""
<p>New players see a joker and think wild card. That is close, with one big catch. Jokers only work in groups.</p>

<h2>Where a joker can go</h2>
<p>Any pung (three of a kind), kong (four of a kind), quint (five) or sextet (six). If your hand needs four 7 dots, you can hold two real 7 dots and two jokers.</p>
{row("D7 D7 J J","A kong of 7 dots built with two jokers. Legal.")}

<h2>Where a joker cannot go</h2>
<p>Singles and pairs. Lots of hands on the card include a lone tile or a pair, like a single flower or a pair of 2s. Those have to be the real tiles.</p>
{row("C2 J","A pair of 2 craks with a joker. Not allowed.")}
<p>Hands from the Singles and Pairs section of the card can never use jokers at all, because every group in them is a single or a pair.</p>

<h2>The joker swap</h2>
<p>Say another player has exposed three 5 bams and one of them is a joker. On your turn, if you hold a real 5 bam, you can trade it for that joker. You can do this with anyone's exposed groups, including your own. The one exception is a player whose hand has been called dead.</p>
{row("B5 B5 J","Someone exposed this. Hold a real 5 bam and the joker can be yours.")}
<p>You can only swap on your own turn, after you draw or after you take a discard. Then you discard as usual.</p>

<h2>A discarded joker is dead</h2>
<p>If someone throws a joker, nobody can call it. That is why experienced players almost never discard one. Throwing a joker hands nothing to anyone, but it also gives up your best tile.</p>

<h2>A couple of habits that help</h2>
<ul>
<li>Before you expose a group with jokers in it, check whether anyone at the table might be holding the real tile. They can take your joker.</li>
<li>When choosing between two hands, favor the one with more groups of three or more. More of those means more places your jokers can work.</li>
</ul>

<p>Jokers get a full lesson on day three in <a href="{{L:index}}">Sparrow</a>, and the practice table flags it when you try to use one where it does not belong.</p>
""",
  faq=[
   ("Can a joker be used in a pair in American mahjong?","No. Jokers can only be used in groups of three or more identical tiles."),
   ("How many jokers are in an American mahjong set?","Eight."),
   ("Can you call a discarded joker?","No. A discarded joker cannot be called by anyone."),
   ("When can I swap for an exposed joker?","On your own turn, if you hold the real tile the joker is standing in for."),
  ])

# ---------------------------------------------------------------- 4
g(slug="how-to-read-the-mahjong-card",
  title="How do you read the American mahjong card?",
  desc="Each line on the card is one winning hand. Here is what the colors, the X and C, the zeros and the numbers mean, explained for first timers.",
  date="2026-10-04",
  lede="Every line on the American mahjong card is one complete winning hand of 14 tiles. Colors show which groups share a suit. The letter at the end tells you whether you can call discards (X) or must keep it concealed (C), and the number is what the hand pays.",
  body=f"""
<p>The first time you see the card it looks like a lottery ticket printed in three inks. It is more readable than it looks. Take one line at a time.</p>

<h2>One line, one hand</h2>
<p>Each line spells out 14 tiles. Numbers are tile values. Letters are honors: N, E, W and S for winds, D for a dragon, F for a flower. A zero is the white dragon, which everyone calls Soap. That is how a line can say 2026 and mean a hand built from a 2, a Soap, another 2 and a 6.</p>
{row("F F | C2 O C2 C6","FF 2026 written as tiles, with craks as the suit.")}

<h2>What the colors mean</h2>
<p>The card prints groups in green, red or blue. The colors do not stand for a specific suit. They tell you which groups match each other inside one hand.</p>
<p>If every group in a line is the same color, the whole hand is one suit. You pick which. If a line uses two colors, you use two different suits, again your choice. Three colors means all three suits.</p>
{row("B2 B2 B2 | B4 B4 B4 B4 | D6 D6 D6 D6","Two colors on the card can become bams and dots here. Craks and dots would also work.")}

<h2>X or C</h2>
<p>At the right end of each line is a letter and a number. X means exposed. You may call other people's discards to complete groups, laying them face up. C means concealed. You build it from your own draws and only show it when you win, though you can still take the final tile you need for mahjong.</p>

<h2>Dragons follow suits</h2>
<p>When a hand pairs a dragon with a number group, the dragon usually has to match the suit. Green dragon goes with bams, red with craks, and Soap with dots. Watch for this, it catches a lot of new players.</p>

<h2>Sections</h2>
<p>Hands are grouped by theme: year hands, even numbers (2468), odd numbers, like numbers, consecutive runs, winds and dragons, and a few more. Learning the sections helps more than memorizing lines. When your starting rack has lots of even tiles, you know which part of the card to look at first.</p>

<h2>The card changes every year</h2>
<p>The National Mah Jongg League prints a new card each spring, and groups switch over once it arrives. The hands change. The way you read them stays the same, so learning on any card is time well spent.</p>

<p><a href="{{L:index}}">Sparrow</a> teaches card reading on day four with a practice card of original hands, and Plus members can photograph their own official card so practice hands use real lines. Sparrow is not affiliated with the League.</p>
""",
  faq=[
   ("What does the zero mean on the mahjong card?","A zero is the white dragon, also called Soap."),
   ("What do the colors mean on the mahjong card?","Groups in the same color share a suit. Different colors mean different suits. The colors do not name a specific suit."),
   ("What do X and C mean on the mahjong card?","X means you can expose the hand by calling discards. C means the hand stays concealed until you win."),
   ("How often does the mahjong card change?","The National Mah Jongg League publishes a new card every year, usually in the spring."),
  ])

# ---------------------------------------------------------------- 5
g(slug="american-vs-chinese-mahjong",
  title="What is the difference between American and Chinese mahjong?",
  desc="American mahjong uses jokers, a yearly card of set hands, and the Charleston. Chinese mahjong has none of those. Here is what changes at the table.",
  date="2026-10-04",
  lede="American mahjong uses eight jokers, a card of required winning hands that changes every year, and a tile passing round called the Charleston. Chinese styles skip all of those, and players build any hand of sets and a pair. American also drops runs, so you cannot win with a sequence like 3, 4, 5 of a suit.",
  body=f"""
<p>If you learned mahjong from a grandparent in Hong Kong and then sat down at an American table, you would recognize the tiles and almost nothing else.</p>

<h2>The tiles</h2>
<p>An American set has 152 tiles. That includes eight flowers and eight jokers. Chinese sets usually have 136 or 144 tiles and no jokers. Some American sets print the year or extra markings on tiles, which makes no difference to play.</p>
{row("J | F | O","Jokers and flowers do real work in American play. Soap does double duty as a zero.")}

<h2>The card</h2>
<p>This is the big one. In American play you can only win with a hand printed on the current card from the National Mah Jongg League. Chinese mahjong lets you build any combination that meets the basic shape of four sets and a pair.</p>

<h2>No runs</h2>
<p>Chinese mahjong uses chows, which are runs like 3, 4, 5 of bams. American mahjong does not let you call or build a chow. Some card hands ask for consecutive numbers, but they are made of groups like a pung of 3s, a pung of 4s and a pung of 5s.</p>

<h2>The Charleston</h2>
<p>American games begin with a tile passing ritual. Chinese games start right away. If you want the details, see <a href="{{L:guides/what-is-the-charleston-in-mahjong}}">what is the Charleston</a>.</p>

<h2>Calling discards</h2>
<p>In both styles you can take another player's discard to finish a group. American rules are tighter. You can only call for a group of three or more, or for the tile that finishes your hand. Calling for a pair is only allowed when it wins.</p>

<h2>Which one should you learn?</h2>
<p>Learn the one your friends play. In the United States, the weekly game at the community center or someone's kitchen table is almost always American, with a fresh card each spring.</p>

<p>I made <a href="{{L:index}}">Sparrow</a> for the American game only, for people getting ready to join a group. It does not teach Chinese or Riichi styles.</p>
""",
  faq=[
   ("Does Chinese mahjong use jokers?","Traditional Chinese mahjong does not use jokers. American mahjong uses eight."),
   ("How many tiles are in an American mahjong set?","152, including eight flowers and eight jokers."),
   ("Can you make runs in American mahjong?","No. American mahjong does not allow chows or runs. Consecutive number hands are built from groups like pungs and kongs."),
   ("Do you need a card to play Chinese mahjong?","No. Only American mahjong uses a yearly card of required hands."),
  ])

# ---------------------------------------------------------------- 6
g(slug="first-mahjong-night-what-to-know",
  title="What should I know before my first mahjong night?",
  desc="Bring a current card, learn the joker rule, ask about house rules and money, and tell the table you are new. A short checklist for first timers.",
  date="2026-10-04",
  lede="Bring the current card if you have one, know the joker rule cold, and tell the table you are new before the first Charleston. Ask about house rules and money up front. Groups are used to beginners, and most players remember being one.",
  body=f"""
<p>You are holding a bottle of wine in a stranger's driveway, running through tile names in your head. Here is what will help once you get inside.</p>

<h2>Bring a card</h2>
<p>Each player uses their own copy of the current National Mah Jongg League card. If you do not have one yet, ask the host. Somebody usually has a spare from a friend who quit. Large print versions exist and nobody will judge.</p>

<h2>Know these cold</h2>
<ul>
<li>You win with 14 tiles that match one line on the card.</li>
<li>Jokers fill groups of three or more. Never a single, never a pair.</li>
<li>Charleston order: right, across, left. Then, if everyone agrees, left, across, right.</li>
<li>Say the name of every tile you discard, out loud.</li>
</ul>
{row("D4","Discard this and say four dot. Every time.")}

<h2>Ask before you play</h2>
<p>Tables differ. Ask how much each game costs (often a small amount, sometimes nothing), whether they play with a time limit, and what happens if someone calls mahjong by mistake. That last one comes with a penalty at many tables. Better to hear it before it happens to you.</p>

<h2>Table manners</h2>
<p>Keep your rack tidy and your tiles facing you. Do not touch other people's discards except when calling one. When you call a tile, say "call" clearly before the next player draws. If you are unsure, it is fine to say so. Slowing down is normal for the first few weeks.</p>

<h2>Expect to lose</h2>
<p>You will lose most games for a while. That is how everyone starts. Watch which hands the winners chose from their starting racks. The game is mostly that decision, made again every hand.</p>

<h2>A quick warm up the day of</h2>
<p>Play two or three practice hands that afternoon. It wakes up the tile names in your head and you will walk in less nervous.</p>

<p><a href="{{L:index}}">Sparrow</a> has a short brush up lesson for exactly this, plus a day seven rehearsal that walks you through a whole night at the table. It takes about five minutes, so the parking lot counts.</p>
""",
  faq=[
   ("Do I need my own mahjong card?","Yes. Each player normally uses their own copy of the current card."),
   ("Do you play for money at mahjong night?","Many groups play for small stakes. Ask the host before the first game."),
   ("What happens if I call mahjong by mistake?","Many tables have a penalty for a false mahjong. Ask about house rules before you start."),
   ("Should I tell the group I am a beginner?","Yes. Most tables slow down for new players and will help you through the first few games."),
  ])
