# LMG Concierge – release notes

For editors on traveltalk.dk, traveltalk.travel, winetalk.dk and worldsporttalk.com. Newest first.

## 0.9.2 – 14 Nov 2026

### New
- **The Aianna box in the text has moved to the end of the article**, just above the Leisure Family block. It used to sit after the first paragraph, where it competed with the Aianna widget at the top of the page. The top widget is unchanged.

### What you do differently
- Nothing. Install it with "Update all now" (Tools → LMG Updates), then purge the cache.

### Good to know
- Applies on traveltalk.dk and traveltalk.travel, where Aianna sits in the text. On winetalk.dk and worldsporttalk.com she sits in the corner, as before.
- This version also brings 0.9.0 and 0.9.1 (Aianna for partners, test mode, master codes) to every site. Nothing of that shows until you set it up under Tools → Aianna for partners.
- Tested on a test WordPress: article text, then Aianna, then the Family block. Not yet seen on the live sites.
- If a site has never had LMG Concierge installed in its normal folder, it will not show in the update list there. Upload the zip by hand (Plugins → Add New → Upload → Replace current).

### Older content
- Applies automatically to all posts and pages from installation on. Nothing in the posts is changed; the box is placed when the page is shown. Posts where Aianna was hidden stay hidden.

## 0.9.1 – 12 Nov 2026

### New
- **What Mio and you do no longer counts in a partner's statistics.** While you are logged in to wp-admin (editor or administrator), opening a partner's link, asking questions and clicking the buttons are not counted. A yellow line at the top of the page says so.
- **A Preview link for each partner** in Tools → Aianna for partners. It shows the page exactly as that partner sees it.
- **Master codes for Mio and you.** Tick "Master code" when you create a code, with a made-up company (e.g. "Demo Travel Co") and a real destination page. A master code:
  - opens the page on any device, without logging in, so it works for a demo on a call
  - is never counted, and is left out of the totals at the top
  - sends requests marked DEMO, so you can see the mail arrive
  - adds no one to the newsletter
- In tests and demos, the two buttons send mails marked TEST or DEMO to Mio and contact@, so you can check that mail from the site arrives. The newsletter box adds no one to Brevo.

### What you do differently
- Install over 0.9.0 (Plugins → Add New → Upload → Replace current).
- Make one master code each: Tools → Aianna for partners → New codes → your name, a made-up company, a destination page → tick "Master code" → Create codes. Use that link for demos and tests.
- Check partners' pages with the Preview link while logged in.

### Good to know
- Tested on a test WordPress with stand-ins for Claude, Brevo and e-mail: a partner's visit is counted, a logged-in preview and a master code are not, and only the partner reaches Brevo. Not tested against the real services.
- "Not counted while logged in" works because the page knows you are logged in. Opened in a private window or on a phone where you are not logged in, a partner's link counts as the partner. Use your master code there.
- A master code is not secret in any special way: anyone with the link can use it for a demo. Close it in the list when it is no longer needed.

### Older content
- Not affected. Codes, statistics and settings from 0.9.0 stay as they are. Visits you already made in 0.9.0 stay counted; close and recreate a code if its numbers should start from zero.

## 0.9.0 – 12 Nov 2026

### New
- **Aianna for partners**: a chat for travel companies we want as partners, on a hidden page of traveltalk.travel. It opens only with a personal link.
  - She greets the person by name, knows their company and our page about their destination, and answers questions about the partner offer: what they get, what it costs, how it works.
  - She names only the prices agreed: USD 200 for 3 months or USD 500 for a year, and the free first month for partners whose link carries it. She never negotiates; for that she hands over to Mio.
  - Above the chat, a preview card shows their company as a Traveltalk partner on our page about their destination. It is a mock-up, not live.
  - Below the chat: "Send me a real offer" and "Book a call". A click sends an e-mail to Mio and contact@ with the person, the company and the whole conversation; reply to it to write to them.
  - An unticked box, "Send me the partner newsletter", puts them on the partner list in Brevo.
- **Tools → Aianna for partners** in wp-admin: create personal links one at a time or many at once, copy the link for each partner, and see for each: opened, questions asked (and what), offer or call requested, newsletter taken. A line at the top gives the totals.
- **The readers' concierge does not change.** It does not appear on the partner page.

### What you do differently
- Install over 0.8.3 on traveltalk.travel (Plugins → Add New → Upload → Replace current). On the other sites it can be installed too; the partner part stays unused there.
- On traveltalk.travel, once:
  1. Pages → Add New. Title "Partners" (or what you like), content only `[aianna_partners]`. Publish.
  2. In Rank Math's box on that page: set it to No Index, so it stays out of the sitemap as well. The plugin already keeps it out of Google and the cache.
  3. Tools → Aianna for partners → Settings: choose the page; check that requests go to mio@traveltalk.media and contact@traveltalk.media; write the partner newsletter's list number from Brevo (or leave it empty if it is set in Newsletter → Overview).
- For each partner: Tools → Aianna for partners → New codes. Name, job title, company, e-mail, the link to our page about their destination, and the offer. For many at once, one per line: `Name; Job title; Company; E-mail; Link; profile` (or `free_month`). Copy the personal link into Mio's mail.
- Test it yourself first: make a code with your own e-mail, open the link, ask a question, click both buttons.

### Good to know
- Tested on a test WordPress with a stand-in for Claude, Brevo and e-mail: the page, the chat, both buttons, the newsletter box, the statistics, a wrong link, and that the readers' concierge is unchanged. Not tested against the real Claude, Brevo or the site's e-mail.
- **E-mail from the site:** the requests are sent by traveltalk.travel's own mail set-up. Check that the first test request arrives (also in spam). If it does not, nothing is lost: the request still shows in Tools → Aianna for partners.
- What Aianna says comes from the Google Doc "Aianna for partners – what she knows". Gaps marked there (how fast a profile goes live, payment, refunds, monthly numbers, traveltalk.dk) she answers with "Mio will answer that one" until they are filled in. Send Claude the corrections, and they go into the next version.
- Opens are counted when the page actually runs in a browser, so mail scanners that only check the link do not count.
- She has her own spending limit (USD 1.50 a day, USD 10 a month) and at most 40 questions per partner per day.
- The personal links hold the partner's name, company and e-mail in wp-admin only; the page shows only their first name and company. Close a link (Close in the list) when it should stop working.

### Older content
- Not affected. The readers' concierge, its settings, conversations and log stay as they are. The partner chat starts empty.

## 0.8.3 – 12 Nov 2026

### New
- **The concierge now leads the conversation on.** Every answer ends with one short question that offers the next step, with the options named, for example "Vil du vide mere om Grenache eller Zinfandel?" This applies to Aianna, Bottiglia and Kai.
- **Bottiglia may mention the newsletter once**, at a natural end of the conversation (when the reader thanks her, says goodbye, or after about three questions). She promises exactly what the sign-up promises, and nothing else.
- **Bottiglia names the shop as ours:** a bottle from bottiglia.wine is presented as coming "fra Winetalks egen vinbutik". She suggests a bottle with its price only when the shop has a fitting one; otherwise she recommends the style.
- **New sign-up text in Bottiglia's panel:** "Producenthistorier, smagsnoter og udvalgte vintilbud fra vores egen vinbutik."

### What you do differently
- Install over 0.8.2 (Plugins → Add New → Upload → Replace current), then purge LiteSpeed.
- **On winetalk.dk, change the popup's text to the same words**, so the two sign-ups promise the same: Settings → LMG Signups → "Sub (popup)" → "Producenthistorier, smagsnoter og udvalgte vintilbud fra vores egen vinbutik." → Save.

### Good to know
- Not tested against the real Claude: how well she follows the new instructions shows only on the site. Try a few conversations on winetalk.dk and tell Claude what reads wrong.
- Prices: bottiglia.wine must show prices with decimals (e.g. €19,00) for Bottiglia to name them. Where it does not, she names the bottle without a price.
- Subscribers who signed up before today agreed to a newsletter without offers. Check the legal question (the §10 note of 10 Nov) before they receive offers.
- Aianna and Kai do not mention the newsletter; only the follow-up question is new for them.

### Older content
- Not affected. Settings, conversations, the portrait and the log stay as they are. The new behaviour applies to answers from installation on.

## 0.8.2 – 12 Nov 2026

### New
- **Bottiglia answers faster on winetalk.dk.** She now answers without first "thinking it through", and her answers have a lower length ceiling. Her answers were already meant to be two to six sentences, so the content should read the same.
- **No reader waits for bottiglia.wine any more.** The wine list from bottiglia.wine is now refreshed in the background twice a day. Before, the first reader after the list expired had to wait while up to 60 wine pages were fetched one by one. That was the likely cause of the slowest answers.
- **Links to the site's own articles are checked without a round trip.** A published article is accepted straight away; only other links are checked over the net.
- **The header reads "Bottiglia, din vinguide" on one line again.** The site's own heading size made the name very large and pushed "din vinguide" onto a line of its own. The panel now keeps its own sizes.

### What you do differently
- Nothing. Install it over 0.8.1 (Plugins → Add New → Upload → Replace current), then purge LiteSpeed.
- Check: ask Bottiglia a question, then look at the answer time in the log under Værktøjer → Bottiglia (the latency column, in milliseconds). Send Claude a few figures.

### Good to know
- Tested on a test WordPress with a fake Claude and a fake bottiglia.wine: thinking is switched off in the request, an expired wine list is answered at once from the last copy and refreshed in the background, and the header shows on one line with a theme that forces large headings. Not tested against the real Claude or on winetalk.dk itself.
- The background refresh runs on WordPress' own schedule, which fires when someone visits the site. On a quiet site the first refresh may come a little late; the reader still gets the last copy straight away.
- Only the very first wine-list fetch on a site, before any copy exists, still happens while a reader waits. On winetalk.dk a copy already exists.
- If the answers feel thinner, thinking can be switched back on in the plugin's winetalk settings file; tell Claude.
- Aianna, Kai and the English traveltalk are not changed in speed; only the header fix applies to them too.

### Older content
- Not affected. Settings, conversations, the portrait and the log stay as they are. The background refresh starts by itself from installation on.

## 0.8.1 – 12 Nov 2026

### New
- **"Vælg billede" under Portræt (Værktøjer → Aianna / Bottiglia / Kai) now opens the media library** in more set-ups. On winetalk.dk the button did nothing. The button now looks for the media library when you click it, not when the page loads.
- **If the media library still cannot open, you get a message** saying so, instead of a button that does nothing. Then the image address can be pasted in the field below it.

### What you do differently
- Nothing. Install it over 0.8.0 (Plugins → Add New → Upload → Replace current).
- To set Bottiglia's portrait on winetalk.dk: Værktøjer → Bottiglia → Portræt → Vælg billede → choose the picture → Brug billedet → Gem. Then purge LiteSpeed.

### Good to know
- Tested on a test WordPress: the button opens the media library, with no errors. The fault could not be reproduced there with 0.8.0 either, so something on winetalk.dk itself stops the media library from loading on that page. If the new message appears, tell Claude: that names the cause.
- Bottiglia's own picture files (bottiglia-face/turn) are not in this zip: they were never in the repository. Choose the portrait in wp-admin as above; the files are then not needed.

### Older content
- Not affected. Settings, conversations and the chosen portrait stay as they are.
