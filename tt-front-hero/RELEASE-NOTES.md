# TT Front Hero – release notes

## 1.5.0 – 26 November 2026

**New**
- The front-page hero now looks like the hero on an article: the article's headline is large (36 px on a computer, 26 px on a phone, one notch smaller than the article heroes had until now), with its categories in capitals just above.
- The categories in the front-page hero are links, as on the article pages. Up to three are shown.
- Every link in the hero is at least 44 px tall, so a thumb can hit it on a phone. A tap anywhere on the picture still opens the article.
- Article heroes get the same headline size (36 px / 26 px), and their category links are also at least 44 px tall.

**What you do differently**
- Nothing in the settings. After updating: LiteSpeed Cache → Toolbox → Purge All, then look at the front page and an article on a phone.

**Good to know**
- The "Rejser med sjæl" line stays hidden on traveltalk.dk, as before (that is set in the site's own Additional CSS, not in the plugin).
- Clicks are still counted in Google Analytics as "hero_click", now also saying whether a headline/picture or a category was tapped.
- The worldsporttalk.com carousel is unchanged.
- Tested on a copy of the hero markup at phone width (390 px) and computer width (1280 px), and the article-hero change was tried on the live Antica Enoteca page in the browser before building. Not tested: a real WordPress install of this version, and traveltalk.travel. Please look at both front pages after updating.
- To go back: reinstall 1.4.0 from the list and purge the cache.

**Older content**
- Applies automatically from installation on, to all articles and the front page. Nothing in posts or settings is changed.

## 1.4.0 – 21 November 2026

**New**
- A new type, **Karrusel** (carousel), made for worldsporttalk.com. The front page's own first section – the stadium picture with the heading, the intro text and the four buttons – stays exactly as it is and becomes slide 1. Slides 2 to 5 are the four newest published articles, each with its featured image and headline, and a click opens the article.
- Articles without a featured image are skipped; the next article fills the place, so there is never an empty slide.
- The carousel changes slide every 6 seconds. It does not stop when the mouse rests on it. Arrows left and right and a row of dots let readers move by hand, also with the keyboard. Readers whose phone or computer asks for less motion see no automatic change, but can still use the arrows and dots.
- A **Release notes** link on the settings screen, and a one-time notice in wp-admin after an update that links to these notes.

**What you do differently**
- On worldsporttalk.com: install the plugin (Plugins → Add New → Upload Plugin), activate it, then go to Appearance → Forsidens hero. Type is already **Karrusel**, slides 4 and seconds 6. Tick **Placér automatisk** and save. Then LiteSpeed Cache → Toolbox → Purge All, and look at the front page on a phone and on a computer.
- To switch the carousel off again: untick **Placér automatisk** and save, then purge the cache. The front page is back to exactly how it was.
- On traveltalk.dk and traveltalk.travel: nothing. The type stays **Hero** and the front page looks and behaves as before. Updating there is optional.

**Good to know**
- Slide 1 is the page's own section, not a copy, so changes made to that section in the page editor show in the carousel straight away. The newest articles follow publishing on their own; pin an article (Stick to the top of the blog) to put it first.
- The news grid under the carousel is not changed, so the newest articles appear both in the carousel and in the grid.
- The carousel is as tall as the first section is today. On a phone that is almost a full screen, so article pictures are cut to a tall shape there; headlines stay readable.
- Tested on a copy of the live worldsporttalk.com front page with the four newest articles, on a computer screen and a phone screen: slide 1 looks identical to today, the page does not jump while loading, slides change every 6 seconds, arrows, dots and keyboard work, nothing moves with reduced motion. Not tested: a real WordPress site (please try it on staging or live and look before you leave it), a real PageSpeed run, older browsers.
- Right now the newest post on worldsporttalk.com has no title and no picture (published 21 November, about Jimmy Connors). The carousel skips it, but it shows in the news grid.

**Older content**
- Not affected. The carousel reads the articles as they are; nothing is changed in posts, pages or settings on sites that already use the hero.

## 1.3.1 – 16 November 2026

**New**
- The front-page hero has its final size from the very first moment the page shows. Until now the pictures stood stacked at full height for a moment and then jumped into place while the page loaded on slow phones. Google PageSpeed counted that jump as a large layout shift (0.41 on traveltalk.travel), which pulls the speed score down.

**What you do differently**
- Nothing. Settings under Udseende → Forsidens hero are unchanged.
- After installing: LiteSpeed Cache → Toolbox → Purge All.

**Good to know**
- Only the front page is affected; the hero looks and rotates exactly as before.
- Tested on a copy of the live front page with slow loading simulated: the hero's jump fell from 0.53 to almost nothing. Not yet tested: a real PageSpeed run after installing (please run one and send it), and traveltalk.dk.
- If the hero ever looks wrong after installing, switch back by reinstalling 1.3.0 and purging the cache.

**Older content**
- Not affected. The change is in how the page loads, not in posts or settings.
