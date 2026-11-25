# LMG Match – release notes

For editors and reviewers on traveltalk.dk. Newest first.

## 0.3.1 – 1 Nov 2026

**New**
- **The questions now come as a pop-up after 10 seconds, not as a thin bar.** A green card in the middle of the page says "Svar på 5 spørgsmål på 10 sek. og du er klar til afgang." (the number is the real number of questions in the set, 5 or 6) with the button "Find din rejse". The button opens the questions in the same window; the reader stays on the article. A × or a click outside closes it.
- **The questions can always be found again.** A small green button "Find din rejse" stays at the bottom right of the page, also after the pop-up is closed, so a reader can come back and answer with another set of interests. Any menu item or button that links to the address #find-din-rejse opens the questions too (Appearance → Menus → Custom Links, address #find-din-rejse).
- Settings → LMG Match pop-up has the seconds (10 to begin with), the text, the button text and the text of the small button.

**What you do differently**
- After installing: LiteSpeed Cache → Toolbox → Purge → Purge All, then open traveltalk.dk with ?lmgbar=1 at the end of the address to see the pop-up at once.
- Choose the question set for the front page in Settings → LMG Match pop-up.
- Optional: add a menu item "Find din rejse" with the address #find-din-rejse.

**Good to know**
- A visitor who has seen the pop-up does not get it again for 14 days (remembered in their own browser); the small button is always there.
- Neither the pop-up nor the small button shows on a page that already has the questions built in. The #find-din-rejse link still works there.
- Not tested on the live site and not run inside WordPress before; tried in a browser against a test page only.

**Older content**
- Not affected. This replaces the bar from 0.3.0, which was never installed.

## 0.3.0 – 1 Nov 2026

**New**
- **A slim bar at the bottom of the page offers the questions.** After 25 seconds a thin green bar slides up: "Tag få spørgsmål på 10 sekunder – og du er klar til afgang." with the button "Find din rejse". The button opens the questions in a window on top of the page; the reader stays on the article. A × closes the bar.
- **The bar picks the question set that fits the article.** An article about Italy gets the Italy questions, a wine article the wine questions. The front page and articles without a matching set get the set chosen in Settings → LMG Match bar (to begin with: Eventyrrejser).
- **Settings → LMG Match bar:** on/off, seconds before it appears, days before the same visitor sees it again (14), where it shows (articles and front page; articles only; every page), which set the front page uses, and the two texts.

**What you do differently**
- After installing: open traveltalk.dk with `?lmgbar=1` at the end of the address (for example traveltalk.dk/?lmgbar=1) to see the bar at once, whatever the cooldown. Press the button and answer the questions.
- Then LiteSpeed Cache → Toolbox → Purge → Purge All.
- Choose the question set for the front page in Settings → LMG Match bar.

**Good to know**
- A visitor who closes the bar or opens the questions does not see it again for 14 days (remembered in the visitor's own browser).
- The bar does not show on a page that already has the questions built in.
- The five or six questions come from the set; the bar text says "få spørgsmål" because the sets have five or six.
- Not tested on the live site, and not run inside WordPress before this version: LMG Match has not been installed on traveltalk.dk until now. The bar and the window were tried in a browser against a test page only.
- The text in the bar is ours to change in Settings; it reaches visitors only after a cache purge.

**Older content**
- Not affected. Pages that already carry the questions work as before; no catch-up is needed.
