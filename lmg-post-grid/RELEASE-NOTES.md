# LMG Post Grid – release notes

## 1.0.2 – 2 Nov 2026

**New**
- **Previews on the traveltalk.travel front page show the article's own opening again.** Articles without a hand-written summary showed "Travel with soul" and the titles of the big picture slides at the top of the front page instead. Their preview is now taken from the article's own paragraphs. Articles with a summary (written in the post's Excerpt field, or Rank Math's description where the grid uses it) are not touched.
- Contains 1.0.1 (no right-hand column on the Travel News page) and 1.0.0 (3-line previews).

**What you do differently**
- Install over the version you have on both sites (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded), then purge the cache. You can skip 1.0.1 if it is not installed yet.

**Good to know**
- The cause is another plugin on traveltalk.travel that adds the front-page slides to each article's text while the front page is drawn; this works around it rather than changing that plugin. Which plugin it is was not checked (it is not one from our repository).
- Not tested on the sites: the preview code was checked for errors only; the slide text problem was seen on the live front page.

**Older content**
- Applies to every article without a summary from installation on. Nothing is saved in the articles.

## 1.0.1 – 2 Nov 2026

**New**
- The Travel News page on traveltalk.travel no longer shows the right-hand column (the sign-up and wine boxes). The grid of posts takes the full width, as Rejsenyt does on traveltalk.dk. Articles and other pages, Europe among them, keep their right-hand column.

**What you do differently**
- Install over 1.0.0 on traveltalk.travel (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded), then purge the cache. On traveltalk.dk it changes nothing; installing it there too keeps both sites on the same version.

**Good to know**
- The Travel News page's own layout setting did not take effect; this does it from the plugin. Turning the setting back has no effect while the plugin is active.
- Tested by applying the same rule to the live page in a browser. Not tested installed.

**Older content**
- Not affected; applies to the Travel News page from installation on.

## 1.0.0 – 2 Nov 2026

**New**
- In the post grids (Travel News on traveltalk.travel, Rejsenyt on traveltalk.dk, and every other grid of posts made with the same block), each preview under the picture now stops after 3 lines, whatever the column width. Before, previews ran to 55 words, up to 15 lines in narrow columns.

**What you do differently**
- Nothing. Install and activate on both sites, then LiteSpeed Cache → Toolbox → Purge All.

**Good to know**
- Only the display is cut: the full preview text stays in the page, so search engines still read it.
- To undo: deactivate the plugin under Plugins.
- Tested by applying the same rule to the live pages in a browser (3 lines at wide, medium and phone width). Not tested installed on the sites.

**Older content**
- Applies automatically to every grid from installation on. No catch-up needed.
