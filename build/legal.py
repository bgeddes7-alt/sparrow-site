def LEGAL(EMAIL, UPDATED, APP_URL):
    M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    out = []

    out.append(("privacy", "Privacy Policy", "What Sparrow collects, what it never collects, who processes it, and how to delete it.", f"""
<span class="eyebrow">Privacy</span><h1>Privacy policy</h1><p class="meta">Last updated {UPDATED}</p>
<p class="lede">Sparrow has no sign up. We never ask for your name, email or phone number. There are no ads and no tracking. We keep the small amount of data the app needs to work, and we delete it when you ask.</p>
<p>This policy covers the Sparrow iPhone app and this website, sparrowmahjong.app. Both are run by Geddes Ventures LLC ("we", "us"). Questions go to {M}.</p>

<h2>What the app stores</h2>
<table><tr><th>Data</th><th>Why</th><th>Where it lives</th></tr>
<tr><td>A random anonymous ID created when you first open the app</td><td>So your purchases and uploaded card follow your phone</td><td>Our database (Supabase)</td></tr>
<tr><td>Whether you have Sparrow Plus, which plan, and purchase dates</td><td>To turn on Plus features</td><td>RevenueCat and our database</td></tr>
<tr><td>The list of hands read from a card you upload</td><td>So you can practice with your own card</td><td>Our database</td></tr>
<tr><td>Lesson progress and settings</td><td>So you pick up where you left off</td><td>Only on your phone</td></tr>
<tr><td>Basic server logs (IP address, time, request type)</td><td>Security and fixing bugs</td><td>Our hosting providers, kept for a short period</td></tr>
</table>

<h2>Card photos</h2>
<p>Uploading a card is optional and only available with Sparrow Plus. When you do it, the photos go to our AI provider, Anthropic, which reads the hands and sends back a list. We do not keep the photos. Anthropic does not use this data to train its models, and it deletes it on its own short retention schedule for abuse monitoring. Please photograph only the card itself.</p>

<h2>What we never collect</h2>
<p>Your name, email, phone number, contacts, location, photos you did not choose to upload, or your advertising identifier. We do not sell or share personal information, and we do not track you across other companies' apps or websites.</p>

<h2>Purchases</h2>
<p>Apple handles every payment. We never see your card number or Apple ID. RevenueCat receives purchase receipts from Apple and tells us whether Plus is active.</p>

<h2>Who processes data for us</h2>
<table><tr><th>Company</th><th>What they do</th></tr>
<tr><td>Supabase</td><td>Database, anonymous sign in and server functions</td></tr>
<tr><td>RevenueCat</td><td>Checks subscription status</td></tr>
<tr><td>Anthropic</td><td>Reads uploaded card photos</td></tr>
<tr><td>Apple</td><td>App distribution and payments</td></tr>
<tr><td>Cloudflare</td><td>Hosts this website</td></tr></table>
<p>Each of these companies only gets what it needs to do its job, under its own contract and privacy terms. Data is processed in the United States.</p>

<h2>This website</h2>
<p>sparrowmahjong.app sets no cookies and runs no analytics or advertising scripts. Cloudflare keeps standard request logs to keep the site up and block attacks.</p>

<h2>How long we keep it</h2>
<p>We keep your anonymous ID, Plus status and uploaded card hands while you use Sparrow. Ask us to delete them and we will within 30 days. Deleting the app removes everything stored on your phone right away.</p>

<h2>Your rights</h2>
<p>You can ask what we hold about you, ask us to correct it, or ask us to delete it. See <a href="{{L:delete-data}}">delete my data</a> for the quickest way. We will not treat you differently for asking.</p>
<p><b>California.</b> We do not sell or share personal information as the CCPA defines those terms, and we do not use sensitive personal information.</p>
<p><b>EU and UK.</b> We process data to provide the app you asked for (contract) and to keep it secure (legitimate interests). You can complain to your local data protection authority.</p>

<h2>Children</h2>
<p>Sparrow is made for adults learning a social game. It is not directed at children under 13, and we do not knowingly collect data from them. If you think a child has used Sparrow and you want their data removed, email {M}.</p>

<h2>Security</h2>
<p>Data travels over encrypted connections. Our database uses row level security so each anonymous ID can only reach its own records. No system is perfect, so we collect as little as we can.</p>

<h2>Changes</h2>
<p>If we change this policy we will update the date at the top. If a change affects what we collect, we will post it here before it takes effect.</p>

<h2>Contact</h2>
<p>Geddes Ventures LLC, {M}</p>
"""))

    out.append(("terms", "Terms of Use", "The terms for using the Sparrow app and website, including subscriptions, uploaded cards and the Apple standard license.", f"""
<span class="eyebrow">Terms</span><h1>Terms of use</h1><p class="meta">Last updated {UPDATED}</p>
<p class="lede">Use Sparrow to learn and practice American mahjong. Apple handles payments and refunds. Only upload a card you own. Sparrow is a study tool and is not affiliated with the National Mah Jongg League.</p>

<h2>Who these terms are with</h2>
<p>These terms are between you and Geddes Ventures LLC, which makes Sparrow. By using the app or this website you agree to them. The app is also licensed to you under Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Licensed Application End User License Agreement</a> (the standard EULA). If the two conflict, the EULA wins for the app license.</p>

<h2>Sparrow Plus</h2>
<p>Some features need Sparrow Plus, sold through Apple as a yearly subscription with a free trial, a monthly subscription, or a one time lifetime purchase. Subscriptions renew automatically until you cancel. Prices, trials, cancellation and refunds are covered on the <a href="{{L:subscriptions}}">subscriptions page</a>, which is part of these terms.</p>

<h2>Cards you upload</h2>
<p>If you upload photos of a mahjong card, you confirm you own that copy. The hands read from it are stored for your own private practice and are never shown to other users. You keep whatever rights you have in your photos. You give us permission to process them only to provide the feature. Card reading uses AI and can make mistakes, so check any hand that looks wrong against your card.</p>

<h2>Not affiliated with the League</h2>
<p>Sparrow is not affiliated with, endorsed by or sponsored by the National Mah Jongg League. The built in practice card is made of original hands written for Sparrow. Rules in Sparrow follow common American play. Your table's house rules come first.</p>

<h2>Using Sparrow fairly</h2>
<p>Please do not copy, resell or reverse engineer the app, scrape this site at a volume that disrupts it, or use Sparrow to break any law.</p>

<h2>Our content</h2>
<p>Lessons, art, text, the practice card and software in Sparrow belong to Geddes Ventures LLC or its licensors. You may share links and short quotes from the guides on this website with credit.</p>

<h2>No warranty</h2>
<p>Sparrow is provided as is. We work to keep it accurate and running, but we do not promise it will be error free or always available. Expert advice in the app is a suggestion for practice. It will not win every hand.</p>

<h2>Limits on liability</h2>
<p>To the extent the law allows, Geddes Ventures LLC is not liable for indirect or consequential losses, and our total liability for any claim is limited to the amount you paid for Sparrow in the 12 months before the claim. Some places do not allow these limits, so they may not apply to you.</p>

<h2>Ending use</h2>
<p>You can stop using Sparrow at any time by deleting it and cancelling any subscription. We may suspend access for misuse of these terms.</p>

<h2>Law</h2>
<p>These terms are governed by the laws of the State of California, without regard to conflict of law rules. Nothing here removes rights you have under the consumer laws of where you live.</p>

<h2>Changes and contact</h2>
<p>We may update these terms and will change the date above when we do. Questions: {M}.</p>
"""))

    out.append(("subscriptions", "Subscriptions and Billing", "Sparrow Plus prices, the 7 day free trial, auto renewal, how to cancel, and how refunds work through Apple.", f"""
<span class="eyebrow">Billing</span><h1>Subscriptions and billing</h1><p class="meta">Last updated {UPDATED}</p>
<p class="lede">Sparrow Plus is sold through Apple. The yearly plan starts with 7 free days. You can cancel any time in your iPhone Settings, and refunds go through Apple.</p>

<h2>Plans</h2>
<table><tr><th>Plan</th><th>Price (US)</th><th>Details</th></tr>
<tr><td>Yearly</td><td>$39.99 per year</td><td>7 day free trial for new subscribers, then renews every year</td></tr>
<tr><td>Monthly</td><td>$7.99 per month</td><td>Renews every month</td></tr>
<tr><td>Lifetime</td><td>$79.99 once</td><td>One payment, no renewal</td></tr></table>
<p>Prices in other countries are set in local currency by the App Store and include any taxes Apple applies. The price you see on the purchase screen is the one you pay.</p>

<h2>What Plus includes</h2>
<p>All seven days of the course, the brush up lesson, unlimited practice hands with the expert and full reviews, and uploading your own card. Day one and one practice hand stay free without Plus.</p>

<h2>Auto renewal</h2>
<p>Payment is charged to your Apple ID when you confirm the purchase, or when the free trial ends. Subscriptions renew automatically unless you turn off auto renew at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the period ends. If you cancel during the free trial, you are not charged.</p>

<h2>How to cancel</h2>
<ol><li>Open the Settings app on your iPhone.</li><li>Tap your name at the top.</li><li>Tap Subscriptions, then Sparrow.</li><li>Tap Cancel Subscription.</li></ol>
<p>You keep Plus until the end of the period you already paid for. Deleting the app does not cancel a subscription.</p>

<h2>Refunds</h2>
<p>Apple handles all refunds. Request one at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>. We cannot issue refunds ourselves because we never see your payment.</p>

<h2>Restore purchases</h2>
<p>New phone, or reinstalled the app? Open Sparrow, go to the Plus screen and tap Restore purchases. Make sure you are signed in with the same Apple ID you used to buy.</p>

<h2>Price changes</h2>
<p>If we raise a subscription price, Apple notifies you first and, where required, asks you to agree before you are charged the new price.</p>
<p>Questions about billing: {M}.</p>
"""))

    out.append(("support", "Help and Support", "Get help with Sparrow: restoring purchases, cancelling, uploading your card, and how to reach a real person.", f"""
<span class="eyebrow">Help</span><h1>Help and support</h1>
<p class="lede">Email {M} and a real person will answer, usually within two business days. Tell us what you tapped and what happened. A screenshot helps a lot.</p>

<h2>Common questions</h2>
<div class="faq">
<details open><summary>I paid but Plus is still locked.</summary><p>Go to the Plus screen and tap Restore purchases. Check that your phone is online and signed in to the Apple ID you used. Still stuck? Email us the Order ID from your Apple receipt email.</p></details>
<details><summary>How do I cancel?</summary><p>Settings on your iPhone, tap your name, then Subscriptions, then Sparrow. Full steps are on the <a href="{{L:subscriptions}}">subscriptions page</a>.</p></details>
<details><summary>How do I get a refund?</summary><p>Apple handles refunds at <a href="https://reportaproblem.apple.com" rel="noopener">reportaproblem.apple.com</a>.</p></details>
<details><summary>My card upload missed some hands.</summary><p>Lay the card flat in good light and take one photo for each panel, filling the frame. Glare is the usual problem. You can upload again, up to five times a day.</p></details>
<details><summary>Is the practice card the official card?</summary><p>No. It is a set of original hands written for learning. With Plus you can upload your own official card. Sparrow is not affiliated with the National Mah Jongg League.</p></details>
<details><summary>The expert made a choice I disagree with.</summary><p>Could be right, could be us. Email the hand (a screenshot of the review works) and we will look. Rules questions help us make Sparrow better.</p></details>
<details><summary>I got a new phone and lost my lessons.</summary><p>Lesson progress lives only on your phone, so it does not move to a new one. Plus does move. Restore purchases and you can jump to any day.</p></details>
<details><summary>Is there an Android or iPad version?</summary><p>Not yet. Sparrow is iPhone only for now.</p></details>
</div>

<h2>Privacy and data</h2>
<p>Read the <a href="{{L:privacy}}">privacy policy</a>, or go straight to <a href="{{L:delete-data}}">delete my data</a>.</p>
<h2>Contact</h2>
<p>Geddes Ventures LLC<br>{M}</p>
"""))

    out.append(("delete-data", "Delete My Data", "How to delete everything Sparrow holds about you. No account needed, done within 30 days.", f"""
<span class="eyebrow">Your data</span><h1>Delete my data</h1>
<p class="lede">Sparrow has no accounts, so there is no password to reset or profile to close. Deleting the app clears everything on your phone. To clear what is on our servers too, email us and we will delete it within 30 days.</p>

<h2>Step 1: cancel any subscription</h2>
<p>Deleting data does not stop Apple from billing you. Cancel first in Settings, tap your name, then Subscriptions. Details on the <a href="{{L:subscriptions}}">subscriptions page</a>.</p>

<h2>Step 2: email us</h2>
<p>Send a note to {M} with the subject "Delete my Sparrow data". So we can find your anonymous record, include one of these:</p>
<ul><li>The Order ID from any Apple receipt for Sparrow (in your email, from Apple)</li><li>The rough date you first used Sparrow and the date of any card upload</li></ul>
<p>We will delete your anonymous ID, Plus records and any uploaded card hands, and confirm by email. It takes up to 30 days. Apple keeps its own purchase records under Apple's privacy policy.</p>

<h2>Step 3: delete the app</h2>
<p>Press and hold the Sparrow icon, tap Remove App, then Delete App. Lesson progress and settings are gone from your phone immediately.</p>

<h2>What we cannot delete</h2>
<p>Records we have to keep by law, like tax records for purchases, which hold no lesson or card data. Short lived server logs expire on their own.</p>
"""))

    out.append(("accessibility", "Accessibility", "How Sparrow approaches accessibility, and how to tell us about anything that gets in your way.", f"""
<span class="eyebrow">Accessibility</span><h1>Accessibility</h1><p class="meta">Last updated {UPDATED}</p>
<p class="lede">A lot of people learning mahjong are reading tiles across a table with their glasses pushed up. We want Sparrow to work for everyone at that table, and we fix problems people report.</p>
<h2>What we do</h2>
<ul>
<li>Every tile in the app and on this site has a spoken name for VoiceOver, like "5 Bam" or "Joker".</li>
<li>Tiles show their number and suit, so color is never the only clue.</li>
<li>Animations calm down when Reduce Motion is on in your iPhone settings.</li>
<li>This site follows WCAG 2.1 AA as our target, works with screen readers, and supports dark mode.</li>
</ul>
<h2>Known gaps</h2>
<p>We have not finished testing the practice table with VoiceOver. If it trips you up, tell us where.</p>
<h2>Tell us</h2>
<p>If something in Sparrow or on this site gets in your way, email {M}. We read every note and answer within two business days.</p>
"""))
    return out
