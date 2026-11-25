# LMG Rank Math Keywords – release notes

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
