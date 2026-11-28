# LMG Rank Math Keywords – release notes

## 1.1.0 – 28 November 2026

### New
- A new **LMG SEO** menu in the left column collects the SEO tools. **Fokusnøgleord** (the old Tools → Rank Math nøgleord) has moved here, and Link repair, Positioner and Rank Math get shortcuts when they run on the site.
- **LMG SEO → Svage sider** finds published posts with real substance (800+ words) but a Rank Math score under 80. For each it shows what is missing: a link to its country or hub page, internal links, an external link, enough images (about one per 400 words), and a focus keyword that is only a country name.
- Posts with Search Console impressions at positions 10-50 come first, since they are closest to page one. Then the posts with the most gaps.
- **Dagens 5** shows five posts at a time. Press **Ret** on a post to see the suggestions and fix that one post:
  - **Gem nøgleord** puts a longer keyword first (for example "cuzco i peru" instead of "Peru") and keeps the old one as an extra keyword.
  - **Tilføj valgte links** adds one "Læs mere om [hub], se også [external site]" line at the end of the text. **Fortryd linkene** takes it out again.
  - **Markér som klaret** moves the post to the Klaret list.
- New focus keywords for posts (from Fokusnøgleord and on publishing) now lead with a longer phrase that contains the country, with the country second. Pages keep the country as their main keyword.

### What you do differently
- After installing, open **LMG SEO → Svage sider** and press **Scan nu** (it reads 40 posts at a time and takes a minute or two).
- Work through Dagens 5. After a fix, open the post in the editor and press **Opdater**, so Rank Math works out the new score.
- Fill in **Eksterne forslag** under Indstillinger with official sites per place (one per line, "Tanzania = https://..."). Those become the suggested external link. Otherwise use the link that searches the sister site.

### Good to know
- Nothing changes on its own. Every change is one button for one post.
- Adding links saves the text directly, without triggering Translator or other save actions, and keeps a backup for Fortryd.
- Search Console figures come from Rank Math Analytics (last 90 days). Without them, the list is sorted by gaps and length.
- The score shown is the one Rank Math saved last. It changes when the post is saved in the editor, and when you press Scan igen.
- Tested outside WordPress against 122 real traveltalk.dk posts. Not yet tested on a live site.

## 1.0.0 – 7 November 2026

### New
- A new page under **Tools → Rank Math nøgleord** shows how many posts, pages and other content types (airline pages, deals and so on) have no focus keyword in Rank Math.
- The page lists every one of them with a suggested keyword set: the country or destination first as the main keyword, then up to two more taken from the title and the categories (for example "italien, vinrejse til italien, vinrejser italien").
- You can edit any suggestion in the list, untick the ones you don't want, and press **Gem valgte**.
- **Udfyld alle automatisk** fills every missing keyword in one go, with a running count on screen.
- New posts that are published or updated without a focus keyword get one automatically. This can be switched off under Settings on the same page.

### What you do differently
- Install the plugin, open **Tools → Rank Math nøgleord**, look through the first page of suggestions, then press **Udfyld alle automatisk**, or save page by page if you want to check each one.
- Add regions, islands and cities that should count as destinations (Bali, Toscana, Mallorca) under **Ekstra destinationer**. Countries in Danish, English and German are already known.

### Good to know
- Keywords that are already set are never changed.
- If the title has no country, the plugin looks in the categories and tags, then the web address, then the text. Denmark is ignored outside the title, so "fly fra Danmark" does not become the main keyword.
- Pages with no destination (such as "Om os") get a keyword from the title. Untick them in the list if you don't want that.
- Rank Math's SEO score for a post is updated the next time the post is opened in the editor.
- Tested against example titles outside WordPress. Not yet tested on a live site with Rank Math; try it on traveltalk.dk first and check a few posts in Rank Math afterwards.

### Older content
- Needs a catch-up: older posts without a keyword are filled when you press **Udfyld alle automatisk** (or save them from the list). From installation on, new posts are filled when they are published.
