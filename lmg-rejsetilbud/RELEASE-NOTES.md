# LMG Rejsetilbud – release notes

## 1.0.0 – 6 November 2026

### New
- **Rejsetilbud** is a new menu in wp-admin (under Posts). Each deal is its own page with our own text: who the trip suits, what is good, what to watch in the small print. Above the text the reader sees the price, the agency, what is included, departure, travel dates, "Gælder til" and a "Se tilbuddet" button. The button is repeated under the text.
- **Deals box on country pages.** Tick one or more country pages on a deal, and it shows in a "Rejsetilbud til [land]" box on those pages, newest first (3 by default). When LMG Faktabokse shows "Sådan kommer du til …", the box sits right under it, otherwise at the end of the text.
- **Expiry.** On the day after "Valid until" the deal leaves every box by itself. Its page stays up, says "Tilbuddet er udløbet" and points to the country page and its current deals, and Google is asked not to index it.
- **Click counting.** Every click on "Se tilbuddet" is counted before the reader goes on to the agency. Rejsetilbud → Settings and clicks → Clicks shows clicks per agency and per deal, this month and in all, and downloads them as a spreadsheet (CSV). These are the numbers to show an agency.
- **Facebook text.** On each deal, a Facebook box (right-hand column) has a ready post to copy: headline, price, what is included, dates, "Gælder til", the excerpt and the link to our deal page.
- **Translation.** Deals can be translated with LMG Translator like any article. They are translated exactly as written, with no length warnings. On traveltalk.travel the deal shows in the boxes of the translated country pages, but only in the languages ticked on the deal.
- **Affiliate notice.** "Annoncelink: Vi kan få provision …" is shown under every box and deal, in the reader's language.

### What you do differently
- Add a deal under Rejsetilbud → Nyt tilbud. Write the headline place-first and price-first, for example "Phuket: 10 dage med fly og hotel fra 6.999 kr.". Write the excerpt as the one line that sells it; it is used in the Facebook text.
- Paste the affiliate link from Partner-ads, Adtraction, Awin or the agency in "Link to the deal". Fill in the price, agency, "Valid until" and "Price checked".
- Pick the country page(s). A deal with no country page shows in no box (the list says so in red).
- Languages: Danish is always on. Tick other languages only when readers there can actually book the deal. Packages from Copenhagen are usually Danish only.
- To show deals somewhere else, put [lmg_rejsetilbud] in a text. [lmg_rejsetilbud land="alle" antal="9"] shows the newest deals for all countries, for example on a "Rejsetilbud" page or the front page.
- Settings are under Rejsetilbud → Settings and clicks → Settings: deals per box, where the box goes, the affiliate notice, which languages new deals get, and the address of deal pages (/rejsetilbud/ on .dk, /travel-deals/ on .travel).

### Good to know
- Not tested on a live WordPress site yet: the code was checked for errors and the price and date formats were tested, but it has not run on traveltalk.dk or .travel. Test with one deal first.
- traveltalk.travel needs this plugin installed too. Deal facts travel there through the Translator's bridge each time a deal is saved on .dk; after installing it on .travel, press "Send all deals to traveltalk.travel again" once on .dk. A deal shows on .travel only once its translation is published there.
- The deal list at /rejsetilbud/ uses your theme's normal archive layout and shows live deals only.
- Clicks from Google's crawler, Facebook's link preview and similar robots are not counted. Clicks are counted per site, so .dk and .travel each have their own numbers.
- If the page cache (LiteSpeed) is on, country pages are cleared when a deal is saved and once a day when a deal expires. If an expired deal still shows, clear the cache for that page.
- Prices are entered by hand. Check them before the deal goes out, and update "Price checked" when you do.

### Older content
- Not affected. No existing posts or pages change. Country pages only get a box once a deal points to them.
