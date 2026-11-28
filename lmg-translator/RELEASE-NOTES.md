# LMG Translator – release notes

For editors and reviewers on traveltalk.dk, traveltalk.travel, winetalk.dk, worldsporttalk.com and think-smarter.net. Newest first. Technical details: README.md.

## 2.22.2 – 28 Nov 2026

### Changed
- **Tone leaves wordplay alone.** Puns, alliteration, rhythm and a headline or slogan with a twist that lands are craft and are never flagged. "Schweiz står for kvalitet fra ure til urlaub" is written into the rules as an example to keep. Rule 6 now catches only tired formulas and half-puns that fall flat. A bold or playful line is not treated as a claim that needs a source.
- The checks flag only clear errors and genuinely mediocre writing, never a creative choice.

## 2.22.1 – 28 Nov 2026

### Changed
- **Tone rule 5 no longer bans "Oplev".** Rule 5 now catches real sales voice only: pushy calls to the reader, ad copy and hype ("Lad dig forføre", "Glæd dig til", "Gå ikke glip af", "Book nu"). "Oplev" and "oplevelse" are left alone when they say what the reader actually does or meets there ("oplev byens skuespilhus", "oplev Schweiz' teatre og musicals"). They are flagged only when they stand in for content ("oplev magien", "en oplevelse for livet") or come with hype.
- **No rewrite that is not clearly better.** The Tone step flags only clear breaks and leaves doubtful passages alone. A rewrite must be plainer, more concrete and correct, unambiguous Danish. Vague or ambiguous words ("se stykker") and plain verb swaps are not offered; if there is no clearly better wording, the passage is not listed.

### What you do differently
- Nothing. A Tone list already waiting on a post was made with the old rule: Reject it and click "Check again".

### Good to know
- Built from the live 2.22.0 on traveltalk.dk (identical to the 2.22.0 build). Only class-lmgt-tone.php and the version number changed.
- If someone has edited rule 5 in Settings → Tone, that wording is kept. A saved copy of the old wording is replaced by the new one.
- check_zip.py reports tests/test-headfix.php as missing a file; that is a false alarm in the checker (it reads `__DIR__` as the plugin root). The file is in the zip. Same result on 2.22.0.

## 2.22.0 – 26 Nov 2026

### New
- **Notes for the editor no longer stay in the text.** Picture plans ("Billedforslag 3: …"), the "Til redaktionen" section with links, translation tips and checks, and similar notes in other languages are taken out of the text every time the post is saved, by you or by a Translator step. They move to a new box on the right, "Notes for the editor".
- **Deleted notes stay deleted.** Delete a note in the box and press Update: it is remembered and never put back, not by a later save, not by a Translator step and not by a new translation.
- **Readers never see them.** Older posts that still carry such notes show without them, even before they are saved again.
- **Translations never get them.** The notes are left out before the text is sent for translation.
- **Translator steps save your edits first.** Deepen, Structure, Tone, Links and Boxes worked on the last saved text. If you had deleted something in the editor and not pressed Update, the step brought it back (this is what happened on "Vinrejse i Østrig"). The editor now saves first, then the step runs.
- **The advice follows the site.** Translations, gaps, new sections, SEO texts, alt texts, structure and tone now speak wine on winetalk.dk, sport on worldsporttalk.com and clear thinking on think-smarter.net. Before, think-smarter.net got travel advice (best time to go, getting there, where to stay).

### What you do differently
- Nothing. Open "Vinrejse i Østrig", press Update once, and the notes move to the box on the right.

### Good to know
- Tested outside WordPress (finding and moving the notes, the wording for each site). Not yet tested inside WordPress itself.

## 2.21.2 – 25 Nov 2026

### New
- **The language front pages now fit the site they are on.** On winetalk.dk/en/ the top of the page said "Travel with soul" and "Destination guides and travel stories, written by people who have been there", the travel wording from traveltalk. The same happened on worldsporttalk.com/fr/ and /it/. Each site now gets its own wording, in every language: wine on winetalk.dk ("Wine first, then food"), sport on worldsporttalk.com ("World sport, in depth"), clear thinking on think-smarter.net ("Tools for clearer thinking"). traveltalk.dk, traveltalk.travel and vacation-talk.com keep the travel wording. The heading over the guides follows suit ("Wine guides", "Sport guides", "Guides").
- **The headings no longer touch the left edge.** On winetalk.dk/en/ the "Latest articles" heading started right at the edge of the screen, so its first letter was cut. On sites whose theme does not add its own side margin (winetalk.dk, think-smarter.net), the page now keeps a margin on both sides and the same width as the rest of the site.

### What you do differently
- Nothing. Update and look at winetalk.dk/en/.

### Good to know
- Which wording a site gets is decided from its web address. A new site that is not travel, wine, sport or think-smarter gets the travel wording until it is added.
- Checked on 25 Nov 2026: winetalk.dk/en/, worldsporttalk.com/fr/ and /it/ showed the travel wording. think-smarter.net had no language front page yet, so nothing showed there, but it is covered for when one appears.
- Tested outside WordPress (the wording for each site and language). Not yet tested inside WordPress itself.

### Older translations
- Not affected. Only the fixed words at the top of each language front page change.

## 2.21.1 – 23 Nov 2026

### New
- **Headings can no longer swallow the text under them.** On "Everything About Camping Holidays" the "Know before you go" heading lost its end, so the questions and answers below it showed in big heading letters. Every heading now ends where a heading must end: at its own end, a blank line, a paragraph, the next heading or a box. Text that was swallowed comes back as normal text. This covers every heading size (H1 to H6), not only the small headings fixed in 2.3.2.
- **The "Know before you go" box repairs itself.** If its questions were folded into the title or into each other, the box is drawn again as: title, then each question as a small heading with its answer under it. The Google question markup reads the repaired box too.
- **Translator → Heading check.** A new page that checks every page and post on the site (originals and translations, published or not) and lists those with a swallowed heading. "Repair all" fixes them in one click.
- **Daily check.** Once a day Translator checks the whole site. If it finds a swallowed heading, a yellow line at the top of wp-admin says how many and links to Heading check.

### What you do differently
- After installing, open Translator → Heading check once and click "Repair all".
- If the yellow line shows up later, click its link and "Repair all" again.

### Good to know
- The repair runs in four places: when a page is saved (by you, by Translator or by any other tool), before a text is sent for translation, when a visitor opens the page, and in Heading check. A visitor never sees a swallowed heading, even before the page is saved again.
- No word is removed. If a repair would make the text shorter, it is not done.
- The 2.3.2 repair could, in rare cases, take the paragraph markup out of a whole section after a broken heading. That repair is replaced.
- A heading written as a whole sentence (for example "Laos is one of Asia's smallest countries, but big on travel experiences.") is left alone, because it may be on purpose.
- Tested against 38 sample texts, including the camping box exactly as it was saved, and against 310 published pages on traveltalk.travel: 4 needed a repair (Camping Holidays, Canada, Nigeria and Golf in Ireland, the last three only a stray heading end) and the other 306 stayed exactly as they were. Not yet tested inside WordPress itself.

### Older translations
- Fixed for visitors from installation on, without changing the saved text.
- The saved text is repaired the next time a page is saved, or at once with Translator → Heading check → "Repair all". The previous version of each page stays under Revisions.

## 2.21.0 – 23 Nov 2026

### New
- **One Translator panel.** Every Translator box that used to sit on the right of the edit screen (Translations, Structure, Pictures, More about, traveltalk.travel, and on translations "What to do now", "Translation check", "Danish original") is now a section inside the one "LMG Translator" panel below the text. The steps come first, then the sections. Click a section's name to open or close it; the panel remembers what you left open.
- **Every "to do" now has a button.** If a step says "● to do", the button that does it is on the right. If what is left can only be done by hand in the editor, the step says "● to do by hand" and tells you exactly what to change and where.
- **Step 1 (Goal) can now be worked from step 1.** Every red ✗ says what is wrong, what to click, and whether another step already handles it, with its own button:
  - **Table of contents:** nothing added one before, not even marking the page as pillar. "Insert the table of contents" puts one in after the intro, before the first section, listing the section headings with jump links. After changing headings, click "Update the table of contents".
  - **Pages linking here:** "Propose links to this page" is now in step 1 too. On a page with no category (pillars often are pages) it now also finds posts that mention the page's focus keyword, and a pillar's own supporting posts are asked first.
  - **Marked as pillar in Rank Math:** "Mark as pillar" sets it in one click.
  - **Supporting posts:** "0 supporting posts chose this pillar" no longer shows a green tick. It now shows as advice (○), with up to 6 related posts you can tick and make supporting posts in one click. Their text does not change.
- **Clearer texts in Deepen, Structure, Tone, SEO and Boxes.** "Practical part middle" now reads "The practical part is in the middle (the section …). Readers look for it near the end. Propose the structure moves it there." Each SEO ✗ says where in Rank Math to fix it.
- **Structure: "Remove the repeated heading"** takes out a section heading that only repeats the title, keeping the text under it.
- **SEO on an original without a focus keyword:** a "Set the focus keyword" button. A keyword or description you have set is never changed.
- The yellow "Next" line names the first open check, so it says what its button is for.

### What you do differently
- Look for the Translator boxes in the one panel below the text, not on the right.
- In step 1, click the button under each red ✗, or the big button on the right (it does the first one).

### Good to know
- The table of contents is Translator's own box, not Rank Math's block, so it works in any editor and in translations. It does not update itself when you change headings: click "Update the table of contents" in step 1.
- If a text already has a table of contents of another kind (Rank Math's block, Easy TOC), Translator leaves it alone.
- Not tested on the live sites, only on test text: check one pillar page after installing (insert the table of contents, look at it in the editor and on the page).
- The one-panel layout can be switched off if it causes trouble (ask Claude; there is no button for it yet).

### Older translations
- Not affected. The panel and texts apply to every page from installation on; nothing in any text changes until you click a button.

## 2.20.0 – 23 Nov 2026

### New
- **A translation counts as new content when it goes live.** Its publish date is now the moment it is published, not the day its draft was made or last saved. The sitemap shows it as updated at that moment too, so Google sees traveltalk.travel (and the language versions on traveltalk.dk) growing every time a translation goes live.
- **Translated destination guides now reach the feed and the "latest" lists on traveltalk.travel,** not only translated articles. Until now a translated country guide such as Botswana or New Zealand never appeared in the RSS feed.
- **Fuller structured data (what Google reads behind the page), on both sites:**
  - The headline is the article's own title, without "- traveltalk.travel" after it.
  - The writer is the real writer of the Danish original. Until now Google was told the author of every copied page on traveltalk.travel was "LMG Translator bridge". Where the writer is not known yet, Traveltalk itself is named.
  - Each page states one language, its own. Before, the same English page said both "en" and "en-US", and a German page said "de" in one place and "en-US" in another.
  - A translation says which page it is a translation of, and the Danish original lists its translations. This repeats the language links Google already gets, in a second form it understands.
  - Destination guides are marked as a travel destination (for example "Botswana", in "Africa"), so Google ties the page to the place and not only to words.
  - The main picture's caption is in the page's language, or left out. Before, English and German pages carried the Danish caption.

### What you do differently
- Nothing. Publish translations as before.
- Each part can be switched off under **Translator → Settings → New content**.

### Good to know
- Scheduled translations keep the time you scheduled them for.
- A translation that is taken down and put back keeps the date it first went live.
- The writer's name travels with translations made or copied from now on. Older copies on traveltalk.travel show Traveltalk as the author until they are copied again from traveltalk.dk.
- Tested on a copy of the Botswana page's structured data, not on the live sites. After installing, check one guide and one article in Google's Rich Results Test (search.google.com/test/rich-results).
- traveltalk.dk could not be reached from where this was built, so its pages were not checked before the change. The old "TravelTalk Schema Enhancements" snippet on traveltalk.dk (if it is still active) says "da-DK" on every page, also Swedish, Norwegian and Finnish ones; it can be switched off once this version is in.

### Older translations
- Their dates are not changed. Every translation already live keeps the date it has, and that date is recorded as its go-live date on the first visit to wp-admin after the update.
- The structured-data fixes apply to all pages, old and new, from installation on.
- The feed change applies at once; older translated guides appear in the feed by the date they have.

## 2.19.6 – 23 Nov 2026

### New
- **Fixed: the edit screen broke on some articles.** On an article with "Who takes you there" suggestions but no company ticked yet, the Translations box hit an error. The rest of the edit screen then never loaded, so the editor looked empty ("Word count: 0") although the text was saved and safe. Seen on "Verdura Resort: Luksusgolf på Sicilien".
- **Safety net:** if any LMG box on the edit screen runs into an error in future, only that box shows a red line saying so. The editor, the other boxes and the Publish button keep working.

### What you do differently
- Nothing. Open the article again after installing: the text is back in the editor.

### Good to know
- Your text was never lost. The empty editor was a display fault; saving from it did not wipe the text (Translator already refuses to save an empty editor over a saved text).
- Verdura Resort is a draft at the moment, so visitors get "page not found". You still see it because you are logged in. Press **Publish** (Udgiv) on it after installing.
- Tested on a mock-up of the failing box, not on the live site.

### Older translations
- Not affected. The fix applies to every article from installation on.

## 2.19.5 – 22 Nov 2026

### New
- **A new step, Tone, right after Structure** in the steps panel at the top of the edit screen, on Danish originals and translations alike. Claude reads the text against the house-style tone rules ("Tone: what rings true") and lists the passages that break one. For each passage you see:
  - the words themselves,
  - the rule number it breaks (point at the number to see the rule) and why, in one line,
  - a proposed rewrite that keeps the meaning and uses only facts already in the text.
- **It never invents facts.** If a good fix needs something the text does not have (a place, a time, a number, a person's name, a source), the step says **"Needs a concrete detail"** and names what is missing. A rewrite that brings in a number or a name the text does not have is held back and shown the same way.
- **The status line in the step says it in one go:** "Tone: 3 passages to look at" or "Tone: OK".
- **Runs by itself on new articles:** a post is checked a couple of minutes after it is first published, and so are its automatic translations. Older texts: click **Check the tone** in the step. **Prepare all** and **Accept all waiting** include Tone, after Structure.
- **The rules live in Translator → Settings → Tone**, filled in with the 11 rules from the house style. Add, change or remove rules there; the next check uses them, with no new version needed.

### What you do differently
- When the Tone step says "waiting for you", read each passage. Every rewrite is ticked. Untick the ones you do not want, then click **Accept: put the ticked in the text**. The ones you untick are rejected. **Reject all** leaves the text as it is.
- "Needs a concrete detail" has no tick box: add the detail by hand in the editor if you know it, or leave the passage.
- A passage that runs across a link or bold text cannot be put in by itself. The step says so; change it by hand.

### Good to know
- **Advice only.** Tone never holds up publishing, also not while proposals wait.
- **Service pages are left alone.** Translator → Settings → Tone → "Leave these pages alone" starts with `travel-services`. Please add the agency pages there: a page ID or a word from their address, one per line. Their subpages are left alone too.
- Rewrites change single passages, never the whole article. The previous version is under Revisions.
- Accepting Tone on a Danish original does not send its translations off to be translated again; each translation has its own Tone step.
- Each check is one Claude call (about as much as Structure). Automatic checks only run on articles first published after you install this version, and on their automatic translations.
- **Not tested on the live sites, nor with Claude itself.** It was tested on a mock-up with a made-up Claude answer about the wellness text (post 82855): the proposal, the tick boxes, Accept, the check for invented numbers and the service-page skip. Please open post 82855 and click **Check the tone** once after installing.

### Older translations
- Not changed by installing. Older texts and translations show the step as "not checked yet" and are checked only when you click **Check the tone**. New articles and their automatic translations are checked by themselves from installation on.

## 2.19.4 – 22 Nov 2026

### New
- **Fixed: the screen went blank for a while after "Save the goal" or Update.** When the article page came back, Translator checked links it could not place by asking the web, up to six of them at up to six seconds each. That could take half a minute on worldsporttalk.com. The page no longer waits for that: links already checked keep their result, and new links it cannot place are shown as "not checked yet" in the Links step until you click **Count again**. Saving a goal no longer recounts the links at all.

### What you do differently
- When the Links step says some new links are "not checked yet", click **Count again** there to check them.

### Good to know
- Not tested on the live sites before delivery: the change only shows once installed. Please save the Maradona post once after installing; I will time the page on worldsporttalk.com.

### Older translations
- Not affected.

## 2.19.3 – 22 Nov 2026

### New
- **The translations list on worldsporttalk.com is no longer squeezed** (Translator → Translations).
  - Each column now gets the room its content needs: titles and originals read on a few lines instead of a narrow strip, and the Rank Math and page-view columns are no longer pressed to nothing.
  - When there are more columns than fit the screen, the list scrolls sideways instead of squeezing everything.

### What you do differently
- Nothing. To make the list fit without scrolling, untick columns you do not use under **Screen Options** (top right), for example ID, Pictures or Views 30d. WordPress remembers your choice.

### Good to know
- Checked on the live worldsporttalk.com translations list in the browser, signed in, by applying the same layout to the page and measuring it: rows went from about 310 to about 175 pixels high, the title column from 173 to 240 pixels, and no column is squeezed to zero. The installed plugin itself has not been tested live yet: please open the list once after installing and say if it looks right.
- Only the translations list changes. The ordinary Posts and Pages lists keep their layout.

### Older translations
- Not affected.

## 2.19.2 – 22 Nov 2026

### New
- **The translations list is readable again** (Translator → Translations, most visible on worldsporttalk.com, which has more columns from other plugins).
  - The title and the original get room; Translator's small columns (Language, Flags, Words, Structure) are kept narrow.
  - "Translations" is no longer shown on that list: it only means something on an original.
  - ID, Pictures and Views 30d start hidden there. Turn them on again under **Screen Options** (top right) if you want them.
- **Fixed: "Views 30d" showed "00"** (the number twice) on translations. It now shows the number once.

### What you do differently
- Nothing. If the list still looks crowded, open **Screen Options** and untick the columns you do not use. WordPress remembers your choice.

### Good to know
- If you have changed Screen Options on that list before, WordPress keeps your own choice, and ID, Pictures and Views 30d are not hidden for you. Untick them there.
- Tested on a mock-up of the list with the same columns. Not tested on the live sites.

### Older translations
- Not affected.

## 2.19.1 – 22 Nov 2026

### New
- **Fixed: "Page not found" at wp-admin/[object HTMLInputElement].** Buttons that send ticks or choices went to a wrong address instead of running. This hit "Write the ticked sections", updating the original from the English version, "Add the ticked sections" with unsaved edits, and the other buttons that run in the background. Since 2.17.27 on every site; seen on winetalk.dk. They now go to the right address.

### What you do differently
- Nothing. Click the button again on the article where it failed.

### Good to know
- Nothing was changed on the server by the failed clicks: they never reached Translator.
- Tested on a mock-up of the edit screen with the same kind of form: it now runs in the background and shows its result. Not tested on the live sites.

### Older translations
- Not affected.

## 2.19.0 – 22 Nov 2026

### New
- **A goal for each article: the new first step, "Goal".** Choose one of three, and the step shows what is still missing, each with what to do. Saving a goal never changes the text.
  - **Pillar – the main page on the subject.** Checks: at least 1,500 words, a table of contents, 5 or more pages linking to it, marked as pillar in Rank Math (set for you when you save), and that every supporting post links up to it.
  - **Supporting post – belongs to a pillar.** Choose its pillar from a list. Checks: it links up to the pillar, it has its own narrower keyword so the two do not compete in Google, and the pillar links down to it. **Propose links** now always proposes the link up to the pillar first.
  - **Top 10 on Google.** Checks: Rank Math score green (81 or more), 2 or more pages linking to it, and a content comparison. Deepen gets a new button, **Compare with the top 10**: Claude lists what the pages that rank best for your keyword usually cover and this article lacks. You then write the sections with Deepen as before.
  - Being an authority (facts from the text, sources, depth) is part of every step for every article, so it is not a separate choice.
- **Deepen on worldsporttalk.com and winetalk now thinks sport and wine.** The content check was always asked about a "travel article" and could suggest travel companies. It now uses the site's own subject, and suggests companies only on travel sites.

### What you do differently
- Open an article, choose its goal in step 1 and press **Save the goal**. Then work down the red ✗ in that step.
- For a supporting post, choose the pillar first, then use Links → Propose links.

### Good to know
- "Compare with the top 10" uses what Claude knows about the kind of pages that rank for a search. It does not read Google's live results.
- A post is offered as a pillar when it has the goal Pillar, or is marked as pillar in Rank Math.
- Translations (the language versions) do not get the Goal step; it belongs on the original.
- Tested: the code loads, and the goal checks were run on test data for all three goals. Not tested on the live sites.

### Older translations
- Not affected. Articles have no goal until you choose one.

## 2.18.1 – 22 Nov 2026

### New
- **Steps that only propose now run in the background.** Find content gaps, Write the ticked sections, Propose the structure, Propose links (out and in), Count again, the boxes (questions, fact box, map), Set SEO / Write the meta description, Suggest extra keywords and Fix the flags no longer freeze the page.
  - A small panel at the bottom right shows what is running and for how long. You can go on reading, scrolling and editing.
  - When it is ready the panel turns green with the result and a **Show it** button. **Later** closes it.
  - If you have unsaved edits, Show it saves them first.
  - Several steps can run at once, each with its own line in the panel.
- **A step keeps running on the server even if you leave or reload the page.** Its result is in the steps panel the next time you open the article.

### What you do differently
- Click a step once, keep working, and press **Show it** when the panel turns green.

### Good to know
- Steps that change the text (Accept, Add the ticked sections, Reject) still reload the page straight away. They are quick, and you should see the new text at once.
- The browser asks before you leave the page while a step is still running. Leaving is safe; the step finishes on the server.
- Tested on a mock-up of the edit screen: the step ran in the background while text was typed, and the result appeared in the panel. Not tested on the live sites.

### Older translations
- Not affected.

## 2.18.0 – 22 Nov 2026

### New
- **One main button per step.** Each step in "Translator – steps" now shows the one button you most likely want. The other buttons (propose again, count again, remove a box) are under a small **More ▾** link below it. A step that waits for you still shows Accept and Reject side by side.
- **SEO step shows the Rank Math score** (red, orange or green) and the checks behind it, each with what to do: keyword in the title, in the meta description, in the first part of the text, in a subheading and in the address, and the length of the meta description. The step is done when the keyword and meta description are there and every check is green.
- **"Write the meta description"** in the SEO step of an original article, when it has none. Claude writes it with your focus keyword in it. Your keyword and the address are never changed, and a description you have written yourself is never replaced.
- **The boxes speak the site's language.** On worldsporttalk.com (and winetalk) the Boxes step no longer names travel boxes. It says "Good to know" instead of "Know before you go", and "Who takes you there" is not mentioned. On sport and wine, the step counts as done once the fact box is in.
- **"Text changed since" only where it matters.** It is shown only next to a proposal that is waiting for you, because only there can it be out of date. Elsewhere you just see when the step last ran.
- **Fixed: the Accept buttons for the map, fact box and questions** looked like plain links. They are proper buttons again.
- **The panel never runs into the right-hand column.** In a narrow main column each step is shown as a block: name and state first, then the text, then the buttons.

### What you do differently
- Use the main button of each step; open **More ▾** only for the less common actions.
- In SEO: fix what has a red ✗, press Update, and watch the score.

### Good to know
- Rank Math works out its score in the editor when you press Update. Translator shows the score Rank Math saved last, so after a change press Update once to see the new number.
- Not in this version: steps that take a long time still keep the page busy until they finish. Moving them to the background is the next piece of work.
- Tested on mock-ups of the steps panel at wide and narrow widths. Not tested on the live sites. Please open one article on each site.

### Older translations
- Not affected. Applies from installation on.

## 2.17.30 – 22 Nov 2026

### New
- **"Prepare all" and "Accept all waiting" work again.** They did nothing when clicked: the buttons were not connected. Now they run.
- **You can see that it is working.** While Prepare all runs, a dark panel under the two buttons (and a bar at the top of the screen) shows a spinner, which step is running ("Step 2 of 3: Structure"), about how much time is left, the time so far and a progress bar. If a step takes longer than usual it says so, and that it is still working.
- **All buttons are locked while it runs,** and the browser warns you if you try to leave the page. At the end it says "Done" and the page reloads with the proposals to read.
- **Prepare all now also finds content gaps** (Deepen) when the text is too short, before the other steps.

### What you do differently
- Click Prepare all once, wait for "Done", then read the proposals below and press Accept all waiting (or accept them one by one).

### Good to know
- The time left is an estimate (about 40–60 seconds a step). Long texts or a busy server can take longer; the panel then says "Taking longer than usual".
- Tested on a mock-up of the steps panel: the buttons start, the panel counts down step by step, and the page reloads with the result. Not tested on the live sites. Please try it once on post 53494 on traveltalk.dk.

### Older translations
- Not affected.

## 2.17.29 – 22 Nov 2026

### New
- **The steps are readable again.** In 2.17.26–2.17.28 the text column of the steps could shrink to a word per line, and the fact-box preview to one letter per line. The text column now always keeps a readable width, the preview table fills it, and the buttons still wrap so the box stays inside the main column.

### What you do differently
- Nothing.

### Good to know
- Tested on a mock-up of the steps panel at main-column width, with the fact-box preview and three buttons in a row. Not tested on the live sites. Please open one article on worldsporttalk.com and one on traveltalk.dk.

### Older translations
- Not affected.

## 2.17.28 – 21 Nov 2026

### New
- **The "Working…" bar now always shows while a step runs.** If you answer OK on "You have unsaved changes", the dark bar at the top now appears, and the other buttons are locked until the page comes back. Before, nothing showed, so a slow step like "Add the ticked sections" looked as if it had done nothing.

### What you do differently
- Nothing. Wait for the bar to finish; do not click again.

### Good to know
- Adding sections saves the whole post, and other plugins (SEO, cache) also run on that save. On a busy server that can take a minute or more. The bar says so, and the page reloads by itself with the result.

### Older translations
- Not affected.

## 2.17.27 – 21 Nov 2026

### New
- **Your edits are saved first, then the Translator step runs, for every button.** Until now this worked for the link-style buttons only. Buttons that send a choice (Deepen → "Add the ticked sections", "Discard all", and the other buttons with ticks) showed "You have unsaved changes… OK: your unsaved changes are lost" instead. Now they save the post the same way as Update, then carry on with what you ticked.
- **No more false "unsaved changes".** Translator now asks WordPress the same question WordPress uses for its own "leave page?" warning: has the title, text or excerpt really changed? Before, the text editor could report a change that was never made, just from opening the page. Moving around with Tab, arrow keys or shortcuts no longer counts as a change either.

### What you do differently
- Nothing. If you have made real changes, you will see "Saving your edits first…", the page reloads once, and the step continues by itself.

### Good to know
- Tested on a mock-up of the edit screen: with a change made, "Add the ticked sections" saved first and then added the ticked sections, with no warning. Not yet tested on the live sites. Please try it once on the Las Vegas article.
- The block editor already saved first; it is not changed.

### Older translations
- Not affected. Applies from installation on.

## 2.17.26 – 21 Nov 2026

### New
- **The Translator box stays inside the main column.** Buttons in the steps (Propose "Know before you go", Propose the fact box, Propose the map) now wrap onto new lines instead of pushing the box over the widgets on the right. All sites with Translator.

### What you do differently
- Nothing.

### Good to know
- Tested on a mock-up at main-column width. Not tested on the live sites.

### Older translations
- Not affected.

## 2.17.25 – 20 Nov 2026

### New
- **No more copied intros.**
  - When a text opens with a label heading such as "Artiklen", "Intro" or "Indledning", Structure now proposes taking that heading out, so the first paragraph becomes the intro. It no longer writes a "new" intro that repeats that paragraph.
  - An intro from Claude that repeats sentences already in the text is left out, and the proposal says so.
  - Claude is told to write new sentences and never to name or link another article in the intro.
- **No links in the opening words.** Links are no longer placed in the first two sentences of a text (about the first 200 characters). Claude is also told to link only where the linked page is about what that sentence is about.

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.
- **On "Vinrejser i Italien" (traveltalk.dk, post 94018):** open Revisions and go back to the version from before the first "structure accepted". Or, by hand: delete the opening paragraphs above the heading "Artiklen", then delete the heading itself. Then run Structure again.

### Good to know
- Links already in texts are not moved. Links that are in the opening words today stay until you remove them.
- Tested: the label-heading and copy checks on a sample text. Not tested on the live sites.

### Older translations
- From installation on: applies to new proposals only. Texts changed earlier stay as they are until fixed by hand or through Revisions.

## 2.17.24 – 20 Nov 2026

### New
- **Working links are no longer called "not found".** The Links step now recognises a link to a page that shares its address with a category (such as /rejseinteresser/vinrejser/), and links to category and tag pages.
- **Moved links are named, with a one-click fix.** A link that still works but goes through a redirect (such as /emilia-romagna/, which now lives at /rejsemal/europa/italien/emilia-romagna/) shows as "moved", with its new address. A new button, **Point moved links at the new address**, changes only those links. Only links that really lead nowhere still say "not found".
- **Structure settles in one go.** When Claude cannot write a practical part (the text has no facts about when to go or getting there), or finds nothing to move, the proposal now says so. Accepting the proposal settles the step, instead of leaving "Practical part missing" so you try again and again.

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.
- Under Links → Show the links, use **Point moved links at the new address** when it appears.
- If Structure says "No practical part written", add the practical facts by hand if the text needs them; the step still counts as done.

### Good to know
- To find moved links, the site asks itself about up to 6 unclear addresses each time it counts. If the host blocks the site from asking itself, those links still show as "not found".
- Tested: the code loads without errors. Not tested on the live sites. Both addresses from your screenshot were checked from outside: /rejseinteresser/vinrejser/ answers (page 92657), and /emilia-romagna/ redirects to the address above.

### Older translations
- Applies automatically: links are counted again the next time a page is opened, and existing texts are not changed until you press the button.

## 2.17.23 – 20 Nov 2026

### New
- **Prepare all.** A new blue bar above the steps has two buttons. **Prepare all** lets Claude propose every step that is "to do", one after another: Structure, Links, Links to this page, Know before you go, Fact box and Map. A "1 of 5…" bar shows how far it has come. Nothing in the text changes. On a long text it takes a few minutes; leave the page open.
- **Accept all waiting.** After Prepare all, read the proposals in the steps. You can untick links, reject any proposal on its own, or edit the text. Then press **Accept all waiting**: everything still waiting goes into the text in the right order (Structure first, then links, then the boxes), with your ticks as they stand. You are asked once to confirm. Every step keeps the previous version under Revisions.
- **All waiting boxes show together.** Until now the map, fact box and questions waited one at a time. Now they show side by side, so they can be accepted in one go.
- **Structure no longer reopens after links.** "Checked: kept as it is" now looks only at the headings and the intro. Accepting links, boxes or a map no longer sends Structure back to "to do".

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.
- New way of working, per text: **Prepare all** → read and adjust → **Accept all waiting** → look at the preview → Publish. The single-step buttons are still there for going back, redoing a step or overruling it.

### Good to know
- If you edit the text between Prepare all and Accept all, the structure proposal is refused (it was made from the older text) and the summary says so. Run that step again on its own.
- A step that gets no answer (the host stopped it) is named in the summary; the other steps still run.
- "Links to this page" changes other pages only when you accept it, and only those pages.
- Tested: the order of steps and the summary were checked in a browser on a sample panel. Not tested on the live sites.

### Older translations
- Applies automatically: the buttons show on every edit screen from installation on. A "kept as it is" mark from 2.17.20–2.17.22 counts once more after one new "Propose the structure".

## 2.17.22 – 20 Nov 2026

### New
- **The green "Done" bar goes away by itself.** It shows for 8 seconds, then fades; it stays while your mouse is on it, and Close still works. The same message stays at the foot of the "Translator – steps" panel as **Last result**, so you can read it again. Reloading the page no longer brings the bar back.

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.

### Good to know
- Tested: the bar fades after 8 seconds and the "Last result" line appears, checked in a browser on a sample page. Not tested on the live sites.

### Older translations
- Not affected: this only changes how messages are shown on the edit screen.

## 2.17.21 – 19 Nov 2026

### New
- **The Links step says in plain words what is missing.** It says either "Done: links out and links in are in place", "To do: links out" (this text links to fewer than 2 of our pages) or "To do: links in" (fewer than 2 other pages link to this one). Before, a post could show "to do" right after you accepted its links, without saying why.
- **New button: "Propose links to this page".** It finds published pages that share a category with this one, plus its country or region page, and proposes one link in each, in a sentence that page already has. You tick which ones you want and press Accept. Only those pages change, and each keeps its old version under Revisions. A page edited in the meantime is left alone.
- **Map links are shown apart.** The Links step adds "Plus N from the map dots". Map links are added when the page is shown, so they are not in the written count.
- **Boxes and other steps no longer hang.** A click now waits at most about two and a half minutes for Claude. If no answer comes, it says so and changes nothing. If the server stops a step without answering, the "Working" bar now says so after three and a half minutes and gives you a "Reload the page" button, instead of spinning for ever.

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.
- On a post that says "To do: links in", click **Propose links to this page**, read the list, untick what you don't want, then Accept.
- If a box says Claude took too long, click it once more. Very long texts (Italy, about 4,200 words) can need two tries.

### Good to know
- "Links in" counts only links written in other pages' text, not menus, grids, map dots or the Read more box.
- On a translation, the proposed pages are the translations, in the same language, of the original's category neighbours.
- Tested: the code loads without errors. Not tested on the live sites. Why Italy hung for 10 minutes is not proven: the likely cause is the host stopping the page after a few minutes. If it still happens, tell me which button it was and how long it ran.

### Older translations
- Applies automatically from installation on: the Links step re-reads every page the next time it is opened. Nothing is changed in any text until you accept a proposal.

## 2.17.20 – 19 Nov 2026

### New
- **Every dot on a map is now a link.** A place with an article of its own links to it. A place without one links to the country or region page shown in the article's "Read more" box. Only when there is no such page does the dot jump to the place in the list under the map. The links are looked up again once a day, so a place gets its own link once an article about it is published.
- **Ideas for new articles from the map.** In the steps panel, under Boxes, the map places that have no article of their own are listed as ideas for new articles.
- **"Propose the structure" no longer loops.** The check reads headings in the page's own language only, and only the last three main headings decide whether the practical part is at the end. A road trip with a "getting there" stage early on is no longer reported as "practical part in the middle". When Claude finds nothing to change, the step says "Checked by Claude: nothing to move, kept as it is" and counts as done until the text changes.
- **"Possible errors in this original": Dismiss ticked.** Tick the notes you don't want and click **Dismiss ticked**; the article stays unchanged. Notes where Claude's own reason says "ignore" or "no change needed" are no longer shown at all. "Apply ticked" now also finds text with curly quotes, dashes or extra spaces.
- **Find pictures stays an option.** When it is switched off, the Pictures box no longer shows a button that ends in "Sorry, you are not allowed to access this page". It says where to switch it on instead.

### What you do differently
- Update both sites with the zip (Plugins → Add New → Upload Plugin → Replace current with uploaded), then purge LiteSpeed.
- For an extra picture: Translator → Parts → tick "Find pictures" → Save (administrator). The Pictures box on the edit screen then shows the **Find pictures** button.
- On the edit screen: if a note under "Possible errors" can't be applied, tick it and click **Dismiss ticked**.

### Good to know
- A map gets its new links the first time someone opens the page after the update. They are filled in in the background, so the links show from the next page view (after a LiteSpeed purge where the page is cached).
- A dot that links to the country or region page passes value to that page, not to the place itself. The article ideas under Boxes show which places would deserve a page of their own.
- Not built in this version: a related-articles grid for posts written on traveltalk.travel itself (post 1727, for example). Today that grid is copied from the Danish original's grid, so .travel's own posts don't get one. That comes as its own version after a short brief.
- Tested: the code loads without errors, and the map links were checked on a sample map (a dot without an article got the hub link; a dot with an article kept its link). Not tested on the live sites.

### Older translations
- Maps already in articles: applies automatically. Their dots get links from the first page view after installation; nothing in the text changes.
- Structure: applies automatically. The new check is used from installation on. Articles stuck on "practical part in the middle" may now show as done; for the rest, one click on "Propose the structure" settles it.
- Possible errors: applies automatically. Notes that say "no change needed" disappear from installation on.

## 2.17.19 – 18 Nov 2026

### New
- **Google's "default" version is now the English page.** When a reader's language has no version of a page, Google is told to show the English page on traveltalk.travel (until now: the Danish original). Pages without an English version keep the Danish original as default.

### What you do differently
- Nothing. Update both sites (Dashboard → Updates), purge LiteSpeed.

### Good to know
- After installation traveltalk.dk updates the existing pages by itself in the background, 15 pages a minute (about 133 pages, roughly 10 minutes), and passes the change to traveltalk.travel. Purge LiteSpeed on both sites once more after about 15 minutes.
- Translator → Checker already expected English as default and stops reporting it once done.
- Tested: the code loads without errors. Not tested on the live sites; Claude checks the pages from outside afterwards.

### Older translations
- Applies automatically: existing pages get the new default in the catch-up described above.

## 2.17.18 – 18 Nov 2026

### New
- **traveltalk.travel is English only (Travel 360).** A new setting, "English only" (Translator → Settings → New articles), is on from installation. Automatic translations go to English only; traveltalk.travel starts no new translations into other languages; its language button shows English and Danish (and, on a page in another language, that language too).
- **The pages already in other languages stay exactly as they are**: published, found by Google, in the sitemap, with their language links. Nothing is deleted, unpublished or redirected. They are just not updated for now.
- **New box on every traveltalk.dk post: "Oversæt til engelsk (traveltalk.travel)?"** – Ja (standard), Nej – aldrig, Senere. You only touch it when an article should *not* be translated. Under "Flere sprog" you can tick other languages for a single post; it is there for a later wave.
- **New list: Translator → Afventer oversættelse** (on traveltalk.dk): posts set to Senere, each with an "Oversæt nu" button.
- **Approve headline and intro, spot-check the rest.** "Translation: what to do now" shows the English headline and first paragraph with **Yes, fine** / **No**. When you say Yes, the **Publish** button appears.
- **Flags no longer stop you.** With flags open, the button reads **"Publish despite N flag(s)"** and asks once – for a deadline, or when the flag does not matter. It is noted on the translation.
- **English written for international readers.** Prices in Danish kroner come out as "DKK 5,000"; Danish-only references get a few words of explanation.

### What you do differently
- Update both sites (Dashboard → Updates), purge LiteSpeed.
- On .dk: write as usual. Set "Nej" or "Senere" only when an article should not go to English now.
- On .travel: open the draft, read headline and intro, click Yes, spot-check, Publish.

### Good to know
- Turn "English only" off in Settings and everything works as in 2.17.17; the other languages are kept, not removed.
- Swedish, Norwegian and Finnish are made on traveltalk.dk only, as before, when ticked under "Flere sprog".
- The steps panel (Structure, Links, Deepen…) is still there as help; it no longer stops publishing.
- Articles published before installation keep whatever they had; the choice box applies from now on.
- Tested: every file loads without errors; the English-only rules, the choice and the headline/intro extract with sample data. **Not tested on the live sites.** Please try one .dk post with Senere, and one translation from Yes to Publish.

### Older translations
- Not affected: existing translations in all languages stay as they are. Drafts waiting on traveltalk.travel get the headline/intro approval from installation on.

## 2.17.17 – 16 Nov 2026

### New
- **The featured image you choose on a translation stays.** Until now, a picture set in the Featured image box could jump back to the old one the next time the edit screen opened, if Translator had saved the text in the last half hour (its safety net for SEO fields also covered the picture). Choosing a picture yourself now switches that safety net off for that translation.
- **Deepen never blocks publishing.** In 2.17.16 a thin text with suggestions waiting ("Go to the suggestions") kept the Publish button away. Deepen is advice; now it never blocks, whether it says "to do" or "waiting".

### What you do differently
- Nothing. Update from Dashboard → Updates (or the zip) and purge LiteSpeed.

### Good to know
- Tested: the code loads without errors; which steps block, with sample step lists (South Africa: Deepen waiting no longer blocks; Structure "to do" still does). The picture fix is not tested on the live sites: set a featured image on one translation, reload the edit screen, and check that it stays.

### Older translations
- Applies automatically from installation on.

## 2.17.16 – 16 Nov 2026

### New
- **A fixed order before publishing.** The Publish button in "Translation: what to do now" only appears when steps 1 Check, 3 Structure, 4 SEO and 5 Links are settled and nothing in the steps says "waiting for you". Until then the box says which step is still open, for example "Finish step 3 Structure, step 5 Links first".
- **Step 7 Publish says the same.** "Not yet: finish … first", or, when everything is settled, "Ready: look at the preview, then press Publish in 'Translation: what to do now'".
- **Publish anyway, when you must.** Under "Not ready to publish" there is a small "Publish anyway" link. It asks you to confirm, and the translation remembers which steps were still open.

### What you do differently
Follow the steps in order for every translation:
1. Check: "No flags" (fix or Accept first).
2. Deepen: only if under 800 words – better on the Danish original.
3. Structure: Accept or Reject.
4. SEO: keyword and meta present.
5. Links: Accept the ticked ones, or Reject.
6. Look at the preview: pictures, headings, layout.
7. Publish with the button in "Translation: what to do now".

### Good to know
- Deepen (thin text) never blocks publishing; it is advice.
- If a step cannot be settled – for example Links when no suitable link was found, or Structure after you rejected the proposal – use "Publish anyway".
- The ordinary WordPress Publish box still works and does not check the steps. Use the button in "Translation: what to do now".
- Tested: the code loads without errors; which steps block, with sample step lists (Ireland: Structure and Links open; a page that is only thin: ready). **Not tested on the live sites.**

### Older translations
- Applies automatically from installation on, to every draft. Already published translations are not affected.

## 2.17.15 – 16 Nov 2026

### New
- **Your text can no longer be wiped by an empty editor.** Sometimes the edit screen opens with an empty text area although the text is saved (the preview shows it). Until now, saving from that screen – or clicking a Translator step, which saves first – stored the empty text. Now a save that would empty a page, post or translation keeps the text that was saved, and a yellow note says so.
- **Publish button where you look.** When "Translation: what to do now" says "No flags. Nothing to fix.", a blue **Publish** button sits right under it. It publishes the text as it is saved, without going through the editor. You no longer need to find the Publish box.
- **Clearer message after "Fix the flags".** The green bar now says the corrections are *ready, not yet in your text*, and to press Accept or Reject in the Check step. It no longer says "Done" while something is still waiting for you.
- **Tidier lists.** Translator's columns (Words, Translations, ID, Pictures, Structure, Views 30d) no longer appear on lists Translator does not work with, such as Travel deals. The column headings there get their room back.

### What you do differently
- Install on traveltalk.travel and traveltalk.dk (order does not matter), then LiteSpeed Cache → Purge All on each.
- To publish a checked translation: click **Publish** in "Translation: what to do now".
- If you see the yellow note "Your text was kept", reload the page. Do not paste the text in again.

### Good to know
- The Publish button only shows when there are no flags (or "I have read the check" is ticked) and the saved text is not empty. Nothing is published by itself; you still click.
- If you ever really want to empty a page, move it to Trash instead.
- Why the editor sometimes opens empty is not found yet; this release makes sure it does no harm.
- Tested: the code loads without errors; the text guard and the column filter with sample data (empty and "&nbsp;" editors keep the saved text; real new text is saved; Travel deals lose Translator's columns, posts keep them). **Not tested on the live sites.** Try the Publish button on one golf draft first.

### Older translations
- Applies automatically from installation on, to every translation, page and post. Nothing to catch up.

## 2.17.14 – 15 Nov 2026

### New
- **No more automatic language switching.** Until now, a reader who once chose a language in the language button was sent to that language on later pages without asking. A German reader who had once clicked English was moved off a German article they had found on Google. Google advises against this. The plugin no longer moves anyone.
- **A small note instead.** When the page exists in the reader's chosen language, a note in the bottom-left corner offers it, in that language: "Read this page in English →". One click takes the reader there; × closes it for the rest of the visit.

### What you do differently
- Nothing. Install on traveltalk.travel first, then traveltalk.dk, and purge LiteSpeed Cache on each.

### Good to know
- The reader's choice is still remembered in their own browser. The "not yet translated" line still shows where a page has no version in that language.
- The note never sits on top of another corner note (welcome, "Back to traveltalk.dk", "Read this page in English ↗" on traveltalk.dk), and it never points to the other site.
- Tested in a browser with the plugin's own page code on a stand-in page: with English remembered, a German page stays German and shows the note linking to the English version; closed, it stays away on reload; with German or Danish remembered, no note. **Not tested on the live sites.**

### Older content
- Applies automatically to every page from installation on. Nothing to catch up.

## 2.17.13 – 14 Nov 2026

### New
- **Links to other sites, from your approved list.** Translator → Settings → "Approved external sites": one address per line (for example formula1.com). Each site starts with a list for its subject (sport, wine or travel); change it as you like. **Propose links** now suggests up to 3 links out to official sources, from your list first. Another site can be suggested when it is the official source; it is marked "not on your list – your call".
- **You tick the links you want.** Every proposed link has a tick box. Untick what you don't want; only the ticked links go into the text.
- **Extra keywords.** Under step 3 SEO, **Suggest extra keywords** finds up to five words people search for that your text already mentions (places, people, events). Add the ones you want after your main keyword in Rank Math → Focus Keyword. Translator never writes them in.
- **Links counts links out.** Step 4 Links now also shows how many links go to other sites ("3 external").

### What you do differently
- Once per site: look at Translator → Settings → Approved external sites, and add or remove addresses. The number of links out per proposal (3) is set under the list.
- In a post: Propose links → untick what you don't want → Accept.

### Good to know
- The links open in a new window and count fully for Google (no "nofollow").
- Every suggested page is checked to answer before it is shown; a suggested address can still be a general page rather than the exact one. Open it before you accept.
- Tested on a test WordPress with a stand-in for Claude: the list, the ticks (only ticked links went in), the cap of 3, and keyword suggestions that are not in the text left out. Not yet tested with the real Claude on the live sites.

### Older content
- Not affected. Existing links stay as they are. A proposal made before the update and still waiting gets tick boxes too, but its links out all show as "not on your list"; press Reject and Propose links again to see the right mark.

## 2.17.12 – 14 Nov 2026

### New
- **The place names sit on the map as links** (G, 14 Nov: "add the links into the map – keep visitors 2 or more pages"). Next to each pin is a small label with the place's name; where we have an article it is a link ("Fontana di Trevi ↗") that opens it. These are real links in the page – Google counts them as internal links – and they show æ, ø and å correctly.
- **Green pin = an article of ours behind it, grey pin = not yet.** Readers see at a glance what they can click; editors see which places are deep-dive candidates.
- **Labels never cover each other or the pins:** each tries the right of its pin, then the left, then a little higher or lower; a label that finds no room is left out (the pin and the list still link).
- **Closer zoom when the places are close together**, down to street level (central Rome), instead of stopping at city level.
- On phones (narrower than 640 px) the labels are hidden so the map stays readable; the pins and the list still link.

### What you do differently
- Maps already in a text get labels and colours when you press **Propose the map again** → Accept. Works the same on all four sites.

### Good to know
- Tested in a browser at desktop and phone width with four places in central Rome: three linked labels and one plain, no overlaps; labels hidden on the phone. The map picture used stand-in tiles. **Not tested on the live sites.**

### Older translations
- **Applies to maps proposed from installation on.**

## 2.17.11 – 14 Nov 2026

### New
- **The map finds our articles under every name a place goes by.** On Antica Enoteca, "Trevi-fontænen" had no link although traveltalk.dk has "Fontana di Trevi, Trevi Fontænen. Et springvand i Rom." – the names were written differently. Propose the map now asks for each place's other names (the local original, English, the article's language) and its most distinctive word ("Trevi"), searches for all of them, and treats hyphens and spaces alike.
- **The article ABOUT a place wins over one that only mentions it.** For "Rom" the map now picks "Rejsen til Rom, den evige stad", not the Trevi article that ends "… i Rom": the title that names the place earliest is chosen.
- **Places without an article of ours are marked as an idea for a deep-dive post** in the panel – one place, its real history, why it is worth the trip, like Antica Enoteca.

### What you do differently
- On Antica Enoteca: Boxes → **Propose the map** → check that Trevi and Rom now say "→ links to …" → Accept.

### Good to know
- Tested: the code loads without errors; the name matching was tried on real traveltalk.dk titles (Trevi → the Trevi article; Rom → "Rejsen til Rom"; "Rom" does not match "Roms" or "from"). Not tried in a live proposal. **Not tested on the live sites.**

### Older translations
- **Applies to maps proposed from installation on.**

## 2.17.10 – 14 Nov 2026

### New
- **"What readers will miss" stays in the article's own language.** On the Danish Antica Enoteca article the suggestions suddenly appeared in Finnish. The cause: when a translation was made, the translation's own content suggestions – in Finnish – were saved on the Danish original and replaced its list. They no longer are; the list on an original comes only from its own check ("Find content gaps").
- **An old map at the top is replaced, also when the classic editor dropped its markers.** On Antica Enoteca the old map stayed at the top after a new one was proposed: the classic editor's Visual view had removed the invisible markers Translator uses to find its box. Accept now also finds an old map box by its own markup and removes it before putting in the new one.

### What you do differently
- On Antica Enoteca: Steps → **Find content gaps** once more to get the list back in Danish; Boxes → **Propose the map** → **Accept** (the old map at the top goes by itself).

### Good to know
- Tested: the code loads without errors; an old map box without markers was removed from sample text and the text around it stayed. **Not tested on the live sites.**

### Older translations
- **Applies automatically** from installation on. A list already overwritten in another language is replaced the next time Find content gaps runs.

## 2.17.9 – 14 Nov 2026

### New
- **What a person has set, Translator never changes – it only advises** (G, 14 Nov). Until now Translator could change SEO fields you had set yourself:
  - the SEO step added its own keyword to your list and replaced your meta description;
  - Catch-up put its keyword first, ahead of yours;
  - a new translation put into a text replaced your SEO title and meta description.
- Now, everywhere: a focus keyword, an SEO title or a meta description that is already there stays exactly as it is. Translator fills a field only when it is empty. Where it has a different suggestion, the green notice shows it ("Your focus keyword is kept: "…". Suggestion (not added): "…""), and you decide whether to use it.
- Together with 2.17.6 and 2.17.8 (fields put back when another plugin changes them during a Translator step), a keyword or category you set should now stay set.

### What you do differently
- Nothing. If a suggestion is better than yours, copy it into Rank Math yourself.

### Good to know
- Tested: the code loads without errors; every place in Translator that writes a focus keyword, SEO title or meta description was checked and now fills empty fields only. **Not tested on the live sites.**
- Keywords and descriptions lost before this version are not restored; set them once more.

### Older translations
- **Applies automatically** from installation on.

## 2.17.8 – 14 Nov 2026

### New
- **The map shows the article's own place, and its places link to our articles** (G, 14 Nov, the Roman wine bar: "throws the references all over mid Italy … what is the use of a Barolo dot without a link"). Propose the map now first decides the article's focus – the city, area or region it is about – and picks only places inside it; a wine region named for its wine, or a city mentioned in passing, is left out. Only a text about a whole country or a route spreads wider.
- **Each place links to an article where we have one**: first on the site itself, then on the sister sites in the same language (traveltalk.dk and winetalk.dk for Danish; traveltalk.travel and worldsporttalk.com for English). The place name in the numbered list under the map is a link with "Læs mere →" / "Read more →", and the pin goes straight to the article. Places without an article of ours stay without a link. In the panel, before you accept, each place says which article it will link to, and the focus is named.
- **No second credit line under the map.** The credit the map licence asks for stays in the picture's corner; the line under the box is gone.
- **Categories and SEO fields are guarded later too.** On the Roman wine bar the categories dropped out after a Translator step although 2.14 puts them back right after the save: the other plugin changes them later in the same request. Translator now checks again at the very end of the request, and once more when the post is next opened in the editor within 30 minutes (with a notice saying what it put back). A save you make yourself in the editor always wins: after you press Update, nothing is put back.

### What you do differently
- On the Roman wine bar: check the categories, then Steps → Boxes → **Propose the map again** → read the places and their links → Accept.

### Good to know
- Tested: the code loads without errors; on a test WordPress a stand-in plugin removed the category and the focus keyword during and at the end of a Translator save, and both were back afterwards; the article lookup was tried on the live sister sites (Barolo and Montefalco found their winetalk.dk articles; "Rom" no longer matches "from"); the map box with links was drawn. Not tried: the new focus rule in a live proposal. **Not tested on the live sites.**
- The plugin that drops the categories is still unknown; the guard works whatever it is.

### Older translations
- **Applies automatically** to every Translator save from installation on. Maps already in a text get links and focus when proposed again.

## 2.17.7 – 14 Nov 2026

### New
- **The map (and the fact box) land after the intro, also when the text opens with a heading.** On the Roman wine bar article (traveltalk.dk) the map went to the very top, above the first heading: Translator looked for "the first heading" and the text began with one. It now finds the end of the real intro – the first heading with at least 25 words of text above it, or else the first paragraph that ends past 25 words – and puts the map there. A fact box at the same spot follows right after the map.
- **The SEO keyword is no longer lost when you press a Translator button.** In the classic editor, a focus keyword typed in Rank Math and not yet saved was thrown away when you pressed a Translator button: Translator only watched the title, the text and the categories. It now notices any unsaved change in the edit screen (Rank Math's keyword, SEO title, description …), saves the post for you first ("Saving your edits first …"), and then runs the step by itself.

### What you do differently
- To move a map that sits at the top: Steps → Boxes → **Propose the map again** → Accept.
- Nothing else: type the keyword, press the Translator button – the save happens first.

### Good to know
- Tested: the code loads without errors; the new intro point was tried on four kinds of text (classic text opening with a heading, classic without headings, block text opening with a heading, intro then heading) and found the end of the intro in each. The save-first step in the classic editor was not tried in a browser. **Not tested on the live sites.**

### Older translations
- **Applies automatically** to every map and fact box accepted from installation on; maps already in a text move when proposed again.

## 2.17.6 – 14 Nov 2026

### New
- **Adding a box or a map no longer wipes the SEO work.** On "Antica Enoteca og Roms ældste vinhistorie" (traveltalk.dk) accepting the map emptied the focus keyword and the Rank Math score fell to 7/100. The cause is the same as with the categories in 2.14.0: another plugin listening to the save clears these fields when a text is saved from anywhere but the edit screen. Every Translator step that changes the text (map, fact box, questions, "Who takes you there", structure, links, pictures, accepting a translation) now remembers the post's SEO fields first and puts them back if the save changed them: Rank Math's focus keyword, title, description, score, schema and other Rank Math settings, the featured image, the page template and the theme's per-post settings.

### What you do differently
- Install on all three sites, then purge LiteSpeed.
- **On "Antica Enoteca" the keyword is already gone**: WordPress keeps no history of SEO fields, so it cannot be fetched back. Set it again: Steps → SEO → Set SEO again, or type it in Rank Math.
- Check any other text where you added a box or a map since 2.9 (fact box, questions, map): if its focus keyword is empty, set it again. The Translator's history under the Steps panel shows which texts had boxes added from 2.17.2 on.

### Good to know
- Tested: a save where another plugin cleared the focus keyword and lowered the score was simulated; both were put back. The Translator's text saves were checked: all of them now go through the protection. **Not tested on the live sites.** After installing, add a box to one text and check that its focus keyword stays.
- Which plugin clears the fields is not established. The protection works whatever it is.

### Older translations
- **Applies automatically** to every save from installation on. Fields already wiped before this version are not restored.

## 2.17.5 – 14 Nov 2026

### New
- **The map sits high on the page.** A map you accept now goes right after the intro, before the first main heading and before the fact box. "Canada map" is searched for, and the map is worth seeing first. A map already in a text moves up when you press **Propose the map again** → **Accept**. (Temperatures by month can come into this box later.)
- **Our map replaces hand-made Google maps.** When you accept our map, any Google map embedded in the same text is taken out in the same go, and the green notice says how many. 24 pages on traveltalk.travel have one (Austria, Cyprus, Hungary, the Central Europe road trip, Greece, Croatia, Belgium, the Azores, Canada and their translations). YouTube and other embeds are left alone.
- **The "Know before you go" box shows normal text again.** On Canada the box had come back with broken tags: its heading never closed, and every answer was saved as a large heading, so the answers showed in big heading letters. The box is now repaired every time the page is shown – heading, questions, answers as normal text – without changing the saved text. The question list for Google (FAQ schema) reads the repaired box too.

### What you do differently
- On Canada: Steps → Boxes → **Propose the map** → check the places → **Accept**. The map lands after the intro and the Google map near the end disappears.
- Nothing for the questions box: it looks right as soon as this version is installed.

### Good to know
- Every version includes all earlier ones: you can go straight from any 2.17.x to this one.
- Why the questions box broke is not established (inferred: the box was edited or translated together with the text and came back with damaged tags). The repair works whatever the cause.
- Tested: the code loads without errors; the box repair was tried on a copy of Canada's broken box (heading closed, answers as paragraphs, the text after the box untouched); the Google map removal was tried on sample text (Google map removed, YouTube kept). The new map position was not tried in WordPress. **Not tested on the live sites.**

### Older translations
- **Questions box: applies automatically** on every page. **Map position and Google maps:** change when the map is proposed again on that page.

## 2.17.4 – 14 Nov 2026

### New
- **No more "Nothing to fix" while a flag stays.** On Canada (traveltalk.travel) the panel said "1 flag" and Fix answered "Nothing to fix", however often it was pressed. The flag was a number that differs from the original (for example a price converted from DKK, or "ten" written for "10"). Fix only corrects meaning, never numbers, so it found nothing to do.
- **Number flags now have their own button: "Numbers are right – clear".** It sits in the Check step, in the box on the right and next to the list of numbers under Translation check. Check the number in the text, correct it by hand if it is wrong, then press the button. The flag leaves the list; the report keeps a note of who checked it and when.
- The Check step now says how many of the flags are numbers. "Fix the flags" only shows when there are meaning flags to fix.
- If the original text cannot be found, Fix now says so instead of "Nothing to fix".
- The history under the Steps panel records "numbers marked as checked".

### What you do differently
- On Canada: Translation check → read the numbers listed → **Numbers are right – clear**. Then the Check step turns done.

### Good to know
- Tested: the code loads without errors. **Not tested on the live sites.**

### Older translations
- **Applies automatically.** Translations stuck on a number flag can be cleared with the new button.

## 2.17.3 – 14 Nov 2026

### New
- **Choose which flags to fix.** Under Translation check, every flag now has a tick box under **Fix** (all ticked to start with). Untick the ones you are happy with and press **Fix the ticked passages**; only those go to Claude. The unticked ones stay on the list.
- **Publish as it is.** The tick under the check now reads "I have read the check – publish as it is", with a line saying you do not have to fix anything. Publish still waits for that one tick, so a person has read the check (G, 10 Nov), but fixing is never required.
- **Links to all four sites count.** Step 5 Links now counts links to traveltalk.dk, traveltalk.travel, winetalk.dk and worldsporttalk.com, each by name ("1 link out to this site, 9 to traveltalk.dk, 2 to winetalk.dk"), and these count towards "done".

### What you do differently
- Install on all three sites, then purge LiteSpeed.
- To publish a translation with open flags: tick "I have read the check – publish as it is" → Publish.
- To fix some flags only: untick the others under Fix → Fix the ticked passages → read the waiting version → apply it.

### Good to know
- Link counts made before this version are counted again the next time the edit screen opens.
- Tested: the code loads without errors. The choice of flags was checked in the code: unticked flags stay open, and the numbers Claude gets match the list. **Not tested on the live sites.**

### Older translations
- **Applies automatically** to every translation from installation on.

## 2.17.2 – 14 Nov 2026

### New
- **History under the Steps panel.** Right under the list of steps there is now a table, "History – what was done, when": the date and time, the step, what was done (for example "map accepted", "structure proposed", "fact box rejected", "links accepted"), whether the text changed, and who did it. Newest first, the last 20 actions per text.
- **Structure works on wine and sport texts.** On winetalk.dk ("Grechetto") Structure kept saying "Practical part missing" and "Propose the structure" could not fix it: it looked for a travel part (when to go, getting there, where to stay) that a wine article does not have. On winetalk.dk and worldsporttalk.com Structure now checks and writes only the intro; the practical part is a travel rule and stays on traveltalk.
- "Propose the structure" in the Steps panel and in the Structure box on the right is the same button; both now behave as above.

### What you do differently
- Install on all three sites, then purge LiteSpeed.
- On "Grechetto": Structure should now show done (unless the intro is missing or too short; then Propose the structure writes one).

### Good to know
- The history starts with this version; earlier actions are not in it (the small "Last run …" lines under each step still show them).
- Tested: the code loads without errors; the history was tried with two actions (time, step, "map accepted", "text changed", the user's name). **Not tested on the live sites.**

### Older translations
- **Applies automatically.** The Structure check on wine and sport texts changes at once; the history fills from installation on.

## 2.17.1 – 13 Nov 2026

### New
- **Pins no longer sit on top of each other.** Places close together (Montefalco and Bevagna, or two villages in Chianti) get their pins nudged apart, with a thin line and a small dot back to the exact spot.
- **The pins can be clicked again – without anything from outside.** Hover over a pin to see its name; click it and the page jumps to that place in the list under the map, which lights up pale green.
- **The list under the map has normal text.** On winetalk.dk the theme showed it in large bold heading letters; it now uses the article's normal size.

### What you do differently
- Install on all three sites, then purge LiteSpeed.
- The list size is fixed on every map at once. The nudged pins and the clickable pins come with each map you propose again: on "Kort over Italienske vine", press **Propose the map again** → **Accept**.

### Good to know
- Tested: the code loads without errors; a map was drawn with stand-in tiles (pins 1/5 and 3/4 now apart), and in a browser the hover ring, the jump to the list and the normal list size worked, with a theme rule that made lists 40 px bold. **Not tested on the live sites.**

### Older translations
- **List size applies automatically.** Pin nudging and clickable pins need the map proposed again.

## 2.17.0 – 13 Nov 2026

### New
- **The map is now a picture on your own site.** When you press Accept on a proposed map, Translator draws the map once on the server – grey with a hint of blue water, faint grey mountains and contour lines, numbered green pins – and saves it as one picture in the Media Library. Readers load only that picture from your own site.
- **More private:** no outside server sees the reader, no map script, nothing new for the cookie banner.
- **Faster:** one picture instead of 20–30 map tiles and a script.
- **Better for search:** the picture has an alt text naming the places ("Kort over Italienske vine med Montefalco, Umbrien, …").
- The numbered list under the map stays, so every place is still named in text.

### What you do differently
- To make a map: Steps panel → Boxes → **Propose the map** → check the places → **Accept**. Accept now takes 20–60 seconds while the picture is drawn.
- **Maps made with 2.15–2.16 (such as "Kort over Italienske vine" on winetalk.dk) still show the old live map.** Press **Propose the map again** and Accept on those pages to turn them into pictures. Once none are left, OpenStreetMap, OpenTopoMap and CARTO can come out of Complianz.
- Install on traveltalk.dk, traveltalk.travel and winetalk.dk, then purge LiteSpeed.

### Good to know
- Readers can no longer zoom or click a pin; the numbered list carries the names.
- The picture does not change when the text changes. Propose the map again after a large edit; the old picture stays in the Media Library.
- If the map service cannot be reached, Accept says so, nothing changes, and you can press Accept again a minute later.
- Tested: the code loads without errors, and a picture was drawn on the test machine with stand-in map tiles (pins, numbers, credit line and the grey look in place, 1200 × 720). Real OpenStreetMap tiles could not be reached from the test machine. **Not tested on the live sites.**
- The server needs PHP's image library (GD), which nearly every host has; if it is missing, Accept says so.

### Older translations
- **Not affected by themselves.** Existing live maps keep working until they are proposed again.

## 2.16.1 – 13 Nov 2026

### New
- **No more "API KEY REQUIRED" across the map.** CARTO, which drew the grey map in 2.15.1, now wants a paid key and wrote its warning over the tiles (seen on winetalk.dk, "Kort over Italienske vine"). The map now uses OpenStreetMap's own map, turned almost grey with a hint of blue water, under the same faint grey mountains and contour lines. Same calm look, no key.

### What you do differently
- Nothing. Install on every site that has 2.16.0 (traveltalk.dk, traveltalk.travel, winetalk.dk), then purge LiteSpeed. Maps already in a text change by themselves.
- In Complianz you can remove CARTO again; OpenStreetMap and OpenTopoMap stay.

### Good to know
- Tested: the code loads without errors. The look has not been seen on the live site yet: open the winetalk map after installing.
- If the grey is too grey or not grey enough, one number changes it.

### Older translations
- **Applies automatically** to every map already in a text.

## 2.16.0 – 13 Nov 2026

### New
- **The boxes and the map work on winetalk.dk and worldsporttalk.com.** Translator now knows what a site writes about: travel on traveltalk, wine on winetalk.dk, sport on worldsporttalk.com. The boxes ask the right questions for each:
  - **Fact box** – on winetalk: region, grapes, style, alcohol, price, serve at, drink with, keeps for, good vintages. On worldsporttalk: born, years active, club, titles, records, the number that says it all (the "Immortal record").
  - **Questions box** – "Good to know: …" ("Værd at vide om …") on wine and sport, with the questions a wine lover or a fan asks. "Know before you go" stays on traveltalk.
  - **Map** – wine regions, villages and estates on winetalk; venues, stadiums, circuits and courses on worldsporttalk.
- **A new site starts with no languages switched on,** so installing Translator on winetalk.dk or worldsporttalk.com translates nothing and adds no language links until someone ticks a language. traveltalk.dk and traveltalk.travel keep their settings.
- The Parts page now names all four boxes and the map.

### What you do differently
- **On traveltalk:** nothing.
- **On winetalk.dk (first trial, G 13 Nov: boxes and map only):**
  1. Plugins → Add New → Upload → this zip → Activate.
  2. Translator → Settings: paste the Claude key (the same one as on traveltalk, or a separate one for winetalk), and leave every language unticked.
  3. Translator → Parts: leave **Boxes** and **Steps panel** on; switch off everything else that is on.
  4. Open one wine article → Steps panel → Boxes → **Propose the fact box**, then **Propose the map**, then **Propose the questions**. Read each and press Accept.
  5. Purge LiteSpeed. Add OpenStreetMap, CARTO and OpenTopoMap in Complianz.

### Good to know
- Not tested on winetalk.dk or any site outside traveltalk. The code was checked to load without errors, and the site detection was tried for winetalk.dk, worldsporttalk.com and traveltalk.travel. **This install is the test.** If anything looks wrong, deactivate the plugin: the boxes already in a text stay as plain text, nothing is lost.
- The Steps panel on winetalk will also show translation steps; with no language ticked they do nothing.
- "Who takes you there" is a travel box; on wine and sport it is simply not proposed unless you tick companies under Deepen.

### Older translations
- **Not affected.** Nothing changes on existing traveltalk pages.

## 2.15.1 – 13 Nov 2026

### New
- **The map's look: grey with mountains and lakes.** The map is now grey on white, with lakes and the sea in a pale tone, and the mountains showing through as faint grey relief and contour lines. Place names sit on top. Simple and calm, so the green pins stand out.

### What you do differently
- Nothing. Install on both sites, then purge LiteSpeed. Maps already in a text change look by themselves.

### Good to know
- The map pictures now come from three free services built on OpenStreetMap: CARTO (the grey map and the names) and OpenTopoMap (the relief). The credit line under each map names them. Add CARTO and OpenTopoMap next to OpenStreetMap in Complianz.
- The relief shows up to a close zoom; beyond that the plain grey map carries on.
- Tested: the code loads without errors. The map pictures could not be loaded on the test machine, so **the look has not been seen yet**: open a page with a map after installing and tell Claude if it is too faint or too strong (one number changes it).

### Older translations
- **Applies automatically** to every map already in a text.

## 2.15.0 – 13 Nov 2026

### New
- **A map box.** Under the Steps panel → Boxes there is a new button, **Propose the map**. Translator reads the article, picks 4 to 8 places it names (regions, cities, parks, lakes, sights), finds each on OpenStreetMap and shows you the list, with where each was found in brackets so you can check it is the right Lake Louise. Press **Accept** and the map goes into the text: a map with numbered pins, and the same places as a numbered list under it, each with a short note from the article.
- **Where it sits:** straight after the fact box when the article has one (facts, then where they are); otherwise at the end with the other boxes. It looks like the other boxes, and it travels with the text to translations like they do.
- **Nothing invented:** a place goes on the map only if the article names it; a place the map cannot find is left out and named in the panel.

### What you do differently
- On a country page: Steps panel → Boxes → **Propose the map** → check the places → **Accept**. It takes about half a minute (the map search allows one place a second).
- To take it out again: **× Remove Map** in the same row.

### Good to know
- **Cookie banner:** the map loads its drawing code from unpkg.com and the map pictures from openstreetmap.org. Neither sets cookies, but the reader's browser contacts them. Add "OpenStreetMap" as a service in Complianz (Complianz → Integrations → Services) so the cookie and privacy statements name it.
- Readers can zoom and click a pin to see its name; the page does not zoom when they scroll past.
- Without JavaScript the numbered list still shows.
- A map does not change itself when the text changes. Press **Propose the map again** after a large edit.
- Tested: the code loads without errors; the box was drawn in a browser with four places (pins, list and credit line in place). The map pictures and the place search could not be reached from the test machine. **Not tested on the live sites.**

### Older translations
- **Not affected.** No existing page gets a map by itself; each map is proposed and accepted on its page.

## 2.14.1 – 13 Nov 2026

### New
- **The link fix from 2.14.0 now works on old Danish addresses.** In 2.14.0, links such as /rejsemal/europa/frankrig/paris/ on traveltalk.travel were still left alone, and still opened the homepage: before removing a link, Translator asked WordPress whether a page lives at that address, and WordPress answers yes when any page has the same last word (here "paris"). Translator now counts a page only if it lives at exactly that address. Checked after 2.14.0: the France guide still had 42 such links.
- **"Review draft" opens Swedish, Norwegian and Finnish drafts.** Since 2.11.0 these drafts are saved on traveltalk.dk, but the link in Translator → Queue on traveltalk.dk pointed to traveltalk.travel, so the drafts looked gone. They were never lost; the link now opens them where they are.

### What you do differently
- Nothing. Install on both sites, then purge LiteSpeed on traveltalk.travel.

### Good to know
- Tested: the code loads without errors, and the link handling was tried on sample text with a lookup that behaves like WordPress's (a Danish address whose last word matches another page). **Not tested on the live sites.** Check after install: https://traveltalk.travel/travel-france-many-destinations-guide/ should have no links that open the homepage.
- Why 2.14.0 missed it is inferred from how WordPress looks up addresses, not seen on the server.

### Older translations
- **Applies automatically** from installation on, to every page on traveltalk.travel. Drafts listed in the Queue before this version open correctly too.

## 2.14.0 – 13 Nov 2026

### New
- **Links on traveltalk.travel no longer send readers to a Danish page or to the homepage.** A link to a traveltalk.dk article now goes to its English page on traveltalk.travel; if there is none, the link is taken out and its words stay. Until now this worked only on translations. It now works on every page on traveltalk.travel, including the site's own English posts.
- **Old Danish addresses written as if they were on traveltalk.travel are caught too.** Some older copies carry links such as /rejsemal/europa/frankrig/… without the traveltalk.dk part. On traveltalk.travel those addresses do not exist, so readers landed on the homepage. They are now treated as traveltalk.dk links (English page, or the words without a link). On the France guide this was 37 links.
- **Categories and tags stay put when a Translator step changes the text.** On traveltalk.dk, an article could fall back to "Uncategorized" after Structure, Boxes, Links or pictures. Translator now remembers the categories and tags first and puts them back if anything changed them. If you have changed categories or tags without saving, it saves first or asks.
- **The Structure check ignores the Translator's own boxes** (the fact box, "Know before you go", "Who takes you there"). Boxes at the end no longer make the practical part look misplaced, and a new section goes before those boxes, never after them.

### What you do differently
- Nothing. Install, then purge LiteSpeed on both sites.

### Good to know
- The text in the database is not changed. The links are fixed when a page is shown, so they switch by themselves as more English pages are published.
- Links that name their language (the family line, "Read in Danish") and a link to traveltalk.dk's front page are left alone. So are pictures and files on traveltalk.dk.
- An address counts as Danish only if it starts with one of traveltalk.dk's Danish sections (rejsemal, rejsetyper, rejseinteresser, europa, asien, afrika, amerika and so on) and no page on traveltalk.travel answers to it.
- Tested: the code loads without errors, and the link handling was tried on sample text (Danish links with and without the domain, a real page here, pictures, the family line, an outside link). **Not tested on the live sites.** Check after install: https://traveltalk.travel/travel-france-many-destinations-guide/ should have no links that open the homepage.

### Older content
- **Applies automatically** from installation on, to every page on traveltalk.travel, old and new. No catch-up run is needed.
- Categories already lost to "Uncategorized" before this version are not put back by themselves; set them again by hand.

## 2.13.0 – 10 Nov 2026

Fewer moving parts. Nothing readers see changes.

### New
- **Translator → Parts.** One page that lists the plugin's optional parts in plain words, each with an On box and a line saying what happens when it is off. Nothing is deleted when you switch a part off; switch it on again and it is back.
- **Switched off (only in wp-admin, readers never saw them):** Find pictures, Save pictures, Improve and keep, the cost meter (Pilot), Translate everything, the old language setup finder, and the "Copy to traveltalk.travel" button in Catch-up. Their menu items are gone.
- **Still on (readers see them, or you work with them every day):** breadcrumbs, "Read more" and "Most read", the boxes, "More about", the country-page lists, the related-articles grid, image texts, the Steps panel, the Work list, the Outreach list and "work in one place". You can switch each one off yourself under Parts, one at a time.
- **Nothing is published by itself any more.** A translation is always saved as a draft and waits for a person to read it and click Publish. This replaces the 1 November rule.
- **The small corner notes are off:** "Read this page in English", "Back to traveltalk.dk" and the welcome note. The language button stays.
- **Claude is the only engine.** DeepL and Gemini are no longer used, whatever Settings says.

### What you do differently
- Install on traveltalk.travel and traveltalk.dk (the order does not matter), then purge LiteSpeed on both.
- After a translation is made, open it, read it and click Publish. Nothing goes out unread.
- To try the site without a part: Translator → Parts, untick one, Save, look at a page. Tick it again if something is missing.

### Good to know
- Tested on a test WordPress with the plugin as traveltalk.dk, as traveltalk.travel and as a single site: the plugin starts, the Parts, Settings, Queue and Catch-up pages open, the menu lists only the parts that are on, and the front page, an article and a Swedish translation give exactly the same page code as with 2.12.0. **Not tested on the live sites.**
- Switching off "Country pages and their articles" changes what some traveltalk.dk addresses show. Leave it on until we look at it together.
- If you had "Translate everything" running, it stops filling the queue. Translations already in the queue are still made, as drafts.
- The corner notes and automatic publishing can still be switched on under Settings, but should not be without a new decision.

### Older translations
- Not affected. Published translations stay published; drafts stay drafts.

## 2.12.0 – 10 Nov 2026

### New
- **Translator → Catch-up on traveltalk.dk: "Swedish, Norwegian and Finnish still only on traveltalk.travel".** It lists the Swedish, Norwegian and Finnish pages that were made for traveltalk.travel and have no copy on traveltalk.dk (on 10 Nov: Irland and Filippinerne in Swedish, Østrig in Swedish and Finnish, Italien in Norwegian, and the Finnish Finland page).
- **"Fetch back" copies each one to traveltalk.dk as it is:** text, title, excerpt, meta description and focus keyword, at the same address under /sv/, /no/ or /fi/, and published. Nothing is translated again, and no Claude call is made.
- **Then traveltalk.travel sends that address to traveltalk.dk for good**, and the language links on both sites name the traveltalk.dk page.

### What you do differently
- Install on **traveltalk.travel first**, then on **traveltalk.dk**. traveltalk.travel must have 2.12.0 before you click, or every item stops with an error.
- On traveltalk.dk: Translator → Catch-up → the new section near the top → **Fetch back**. It does one page every two seconds; leave the page open until it says Finished.
- Then purge LiteSpeed on both sites.

### Good to know
- The pages count as read, because they were already published on traveltalk.travel.
- Pictures in the text keep pointing to traveltalk.travel's media library. They show as before; nothing is copied.
- traveltalk.travel's own overview pages ("Traveltalk reseguider på svenska", "reiseguider norsk") are not translations of a traveltalk.dk article and are not listed. They stay as they are.
- Tested: the code loads without errors. **Not tested on the live sites.** Check after the run: open https://traveltalk.travel/sv/resa-till-osterrike-guide/; it should land on traveltalk.dk under /sv/. The Catch-up section should then say "None".

### Older translations
- Needs a catch-up: the pages only on traveltalk.travel move when you click "Fetch back". Nothing moves by itself.

## 2.11.1 – 10 Nov 2026

A fix to 2.11.0, found while checking it from outside right after installation.

### New
- **The old Swedish, Norwegian and Finnish addresses on traveltalk.travel now really send readers to traveltalk.dk.** In 2.11.0 they still opened on traveltalk.travel, because traveltalk.travel knows traveltalk.dk without "www" and the pages carry "www". The pages already had no language links, so Google saw no conflict, but readers and Google still landed on the old copy.

### What you do differently
- Install on **traveltalk.travel**, then purge LiteSpeed there. traveltalk.dk can have it too, but nothing changes there.

### Good to know
- Tested: the code loads without errors, and from outside after 2.11.0: the Swedish, Norwegian and Finnish articles on traveltalk.dk open with complete language links and x-default on the Danish page. Not tested: the redirect itself on the live site. Check after installing: https://traveltalk.travel/sv/resa-till-singapore-stadsguide/ should land on traveltalk.dk.
- **Not this plugin:** traveltalk.dk's /sv/, /no/ and /fi/ front pages are still sent to traveltalk.travel by something called "LMG DK Language Redirects" (a snippet or small plugin on traveltalk.dk), and traveltalk.travel sends them back. That makes a loop. It must be switched off on traveltalk.dk.

### Older translations
- Applies automatically from installation on.

## 2.11.0 – 10 Nov 2026

Traveltalk Nordic: Swedish, Norwegian and Finnish live on traveltalk.dk again. traveltalk.travel is the English site.

### New
- **Swedish, Norwegian and Finnish translations stay on traveltalk.dk.** New ones are saved on traveltalk.dk and are no longer sent to traveltalk.travel.
- **The ones that were copied to traveltalk.travel come back by themselves.** On traveltalk.dk they answer again at their own address. On traveltalk.travel the same address now sends readers and Google to the traveltalk.dk page, for good. Their place in traveltalk.travel's sitemap goes too.
- **traveltalk.travel no longer makes Swedish, Norwegian or Finnish.** Its own /sv/, /nb/ and /fi/ front pages send readers to the same language on traveltalk.dk.
- **The language versions now name the Danish original as the default page for Google.** Before, it was the English page.
- **The plugin description on the Plugins page now says what it does today:** Claude writes and translates.

### What you do differently
- On **traveltalk.dk**: Translator → Settings → Translate into: tick Svenska, Norsk and Suomi where you want them.
- On **traveltalk.travel**: Translator → Settings → Translate into: untick Svenska, Norsk and Suomi. It no longer makes them anyway, but this keeps the page true.
- Install on traveltalk.dk first, then on traveltalk.travel. Then purge LiteSpeed on both sites.

### Good to know
- Tested: the code loads without errors. **Not tested on the live sites.** Please check these after installing (about 10 minutes):
  1. Open a Swedish translation on traveltalk.dk, for example the Thailand one under /sv/. It should open, not jump to traveltalk.travel.
  2. Open a Swedish, Norwegian or Finnish address on traveltalk.travel that used to work. It should land on traveltalk.dk.
  3. On a traveltalk.dk article with translations, open the page source and search for hreflang. The Swedish, Norwegian and Finnish lines should point to traveltalk.dk, English to traveltalk.travel, and x-default to the Danish page.
  4. On the traveltalk.dk front page, open the language button: Svenska, Norsk and Suomi should stay on traveltalk.dk.
  5. Translator → Bridge → Log on traveltalk.dk: the upgrade line should say how many Nordic translations came back.
- A Swedish, Norwegian or Finnish page that exists only on traveltalk.travel, with no copy on traveltalk.dk, stays where it is. Tell us if you find one.
- German, French, Spanish and Italian pages on traveltalk.travel are not touched by this version.

### Older translations
- Applies automatically on installation. Swedish, Norwegian and Finnish translations copied to traveltalk.travel earlier are taken back to traveltalk.dk once. Nothing needs to be run by hand.

## 2.10.0 – 9 Nov 2026

The first step toward making Translator easy as well as able. Nothing is taken away. Every step, box and button is where it was.

### New
- **"Next" at the top of every Translator panel.** A yellow box says the one thing to do now and has its button, for example "Next · Waiting for you – 5 Links: 3 links proposed… [Accept] [Reject]".
  - Proposals waiting for you come first, then the steps still to do, in the order of the steps.
  - When everything is done, the box turns green: "✓ All steps done."
  - All steps are still listed below it, so you can choose another one.
- **Translator → Work list.** One page with every page and post on this site where something waits for you, oldest first.
  - Each row shows what waits, in which step, and since when, with an **Open** button.
  - Below that come the translations that are still drafts.
  - The menu shows how many items are waiting.
- **No more dead ends on "Not accepted – your edits would be lost".** The page now has a button that fixes it:
  - For a structure: **Propose again from my text**. It makes a new proposal from the text as it is now.
  - For a waiting version: **Reject the waiting version**.
  - **Back: keep my text** and **Accept anyway** are still there.

### What you do differently
- Start your day at Translator → Work list and work down it.
- On a page, do what "Next" says. Use the steps below only when you want something else.

### Good to know
- "Next" picks the first thing waiting, by step order. If you would rather do something else first, just use that step below.
- The Work list shows proposals and unpublished translations. It does not yet show flags from the translation check that nobody has read, or texts that are too short. Tell us if you want those on it too.
- Tested: the code loads without errors. Not tested on the live sites. Please open the Work list on both sites and open one item from it. Then try it with Mio on one article, from start to Publish.

### Older translations
- Applies automatically from installation on. Proposals already waiting show on the Work list and in "Next" right away.

## 2.9.6 – 9 Nov 2026

### New
- **"Not accepted – your edits would be lost" only when the text really changed.** Until now, any save after a proposal counted as an edit. That included the save Translator makes for you before it runs a step, and pressing Update without changing anything. So the warning came up again and again. Now Translator compares the text itself: the warning shows only when words in the text changed after the proposal was made. This applies to Accept for a waiting version, for a new structure, and for proposed links.

### What you do differently
- Nothing. If the warning still shows, the text really did change. Then choose:
  - **Back: keep my text**, then Reject the proposal and press its Propose button again. The new proposal starts from your current text.
  - **Accept anyway**, to take the proposal and lose the changes made since.

### Good to know
- Tested: the code loads without errors. Not tested on the live sites. Propose a structure, press Update without changing anything, then Accept: it should go through.

### Older translations
- Applies to proposals made from installation on. A proposal made before 2.9.6 still uses the old rule once: Reject it and propose it again.

## 2.9.5 – 9 Nov 2026

### New
- **Read more has a date too.** In the Structure box, "Read more block" shows when its choices (place, region, interests, or "No Read more block") were last changed. It counts from installation on.
- **No more getting stuck on "You have unsaved edits".** In the classic editor, ticking Translator suggestions no longer counts as an unsaved edit; only changes to the title, the text or the excerpt do. When there really are unsaved edits, you now choose: Cancel stays so you can press Update first, OK goes on, and the unsaved edits are lost.

### What you do differently
- Nothing new. If you see "You have unsaved edits", choose Cancel and press Update, or OK to go on without them.

### Good to know
- Everything in 2.9.4 is included unchanged.
- Tested: the code loads without errors. Not tested on the live sites. In the classic editor, tick a suggestion and press "Apply ticked to this article": it should run without the message.

### Older translations
- Not affected. The Read more date appears once you change a Read more choice.

## 2.9.4 – 9 Nov 2026

### New
- **More about [country]** on traveltalk.travel. At the end of every country page and every article with a traveltalk.dk original, readers get up to three rows of cards. Each row shows at most 3 cards, and a row with nothing to show is left out.
  - **Get inspired**: articles about the same country.
  - **Plan your trip**: the country page itself, plus articles on when to go, budget, routes, where to stay or visas.
  - **Nearby**: the country pages of other countries in the same region.
  - The cards are in English and link only to traveltalk.travel. Articles already linked from the text are left out.
- **The fact box.** Step Boxes has a new button, "Propose the fact box". It makes 4 to 8 short rows from the text, such as best time to go, budget per day, a night in a guesthouse or getting around.
  - Every number in a row must be in the text. A row with a number the text does not have is left out, and the panel says how many rows were left out.
  - You read the rows and press Accept. The box goes in after the intro and says "From this article. Checked [date]. Prices are a guide."
  - "× Remove Facts" takes it out again.

### What you do differently
- To put an article in a different row, open it on traveltalk.travel and use the box "More about – row" on the right. "Leave it out" keeps it out of every row.
- Use the fact box where the text has long paragraphs of prices and practical advice. Shortening those paragraphs is up to you; Translator does not remove text.
- After changing prices in the text, press "Propose the facts again", so the box and the text say the same.

### Good to know
- On traveltalk.dk nothing changes on the front end. The Danish "Flere artikler om …" grid stays as it is.
- On traveltalk.travel, a translation that already carries the grid copied from traveltalk.dk now shows both the old grid and the new rows. If that is too much, tell us and we will hide one of them.
- The rows can only find articles that have a traveltalk.dk original. Articles written only for traveltalk.travel do not show yet.
- An article goes under "Plan your trip" when its title sounds like planning. Otherwise it goes under "Get inspired". Use the row box where the guess is wrong.
- Nearby shows a different set of neighbours from time to time.
- A fact box made on traveltalk.dk travels with the text when it is translated. Check the rows in the translation, or propose them again on traveltalk.travel.
- Tested: the code loads without errors, and the number check rejects a number that is not in the text. Not tested on the live sites. Check one country page (Indonesia) and one article on traveltalk.travel, and make one fact box.

### Older translations
- More about: applies automatically, from installation on, to every page and article on traveltalk.travel that has a traveltalk.dk original.
- Fact box: only where you propose and accept it. Nothing is added by itself.

## 2.9.3 – 9 Nov 2026

### New
- When each step last ran. In the "Translator – steps" panel, every step (Check, Deepen, Structure, SEO, Links, Boxes) now has a small grey line, for example "Last run 30 mins ago". Hover over it to see the full date and time.
- "Text changed since": when the text has been changed after a step last ran, an orange note appears next to the date. That step may be worth running again.
- Improve and keep on every translated page. On traveltalk.travel, the box "traveltalk.dk original" now also shows on pages Translator translated. "Propose improvements from the Danish original" adds what is new on the Danish page and removes nothing.

### What you do differently
- Use the dates and orange notes to see which steps to run again. There is no button that reruns everything; run the steps you need one by one.
- When the traveltalk.travel page is richer than the Danish one, use "Propose improvements from the Danish original" instead of accepting a full new version from traveltalk.dk.
- If a new version from traveltalk.dk is already waiting, accept or reject it first. Until then the improve button is not offered.

### Good to know
- A step's date is set when you click its button, even if the step found nothing to change.
- The orange note appears after any change to the text, also one made by another step (for example adding links after SEO).
- Tested: the code loads without errors. Not tested on the live sites: please click one step and check its date, then run Improve and keep once on a translated page on traveltalk.travel.

### Older translations
- Dates: from installation on. Steps run before 2.9.3 show no date until you run them once.
- Improve and keep: applies automatically to every translation already on traveltalk.travel.

## 2.9.2 – 9 Nov 2026

### New
- One place to work on a translation: traveltalk.travel. On traveltalk.dk, a translation that has been sent to traveltalk.travel now leaves Translator → Translations. A new view at the top of that list, "Sent to traveltalk.travel (N)", still shows them all.
- Opening one of them on traveltalk.dk shows a short page with a button, "Open it on traveltalk.travel", which goes straight to its edit screen there.

### What you do differently
- Make every change to a translated page on traveltalk.travel, not on the traveltalk.dk copy.
- If you really need the traveltalk.dk copy, the page has a link "Open the workshop copy here anyway". Changes made there are not sent on by themselves.

### Good to know
- Nothing is deleted. New versions from the Danish original are sent as before and wait on traveltalk.travel for Accept.
- Everything from 2.9.1 (the boxes, the FAQ, Remove (x), the steps) works as before.
- Tested: the code loads without errors. Not tested on the live sites yet: please open one sent translation on traveltalk.dk and click the button once.

### Older translations
- Applies automatically from installation on, to every translation already sent. For older ones the button finds the right page on traveltalk.travel the first time you use it.

## 2.9.1 – 9 Nov 2026

**New**
- **Old question lists become the new box.** Many pages already have a questions section ("Ofte stillede spørgsmål", "Frequently asked questions" …) written the old way. Propose "Know before you go" now keeps those questions, corrects and adds to them, and on Accept the box **replaces the old section where it stood** – no second list. The panel says when that will happen.
- **New translations get the box proposed by themselves.** About a minute after a new translation is saved, Translator proposes the questions for it (once per translation). They wait in the panel; nothing goes on the page until you press Accept. If the original already has the box, it simply comes with the translation.
- **Remove a whole box with one click.** In step 6, "× Remove Know before you go" and "× Remove Who takes you there" take the box out of the text (asks first; the old version stays under Revisions).

**What you do differently**
- On older pages with a questions section: Propose "Know before you go" → Accept. The old section is replaced.
- On new translations: open them, read the waiting questions, Accept or Reject.

**Good to know**
- The automatic proposal uses the writing engine like the button does, so it costs the same small amount per translation.
- Tested: the code loads without errors, and finding the old questions section was tried on a sample page. Not tested on the live sites.

**Older translations**
- Existing translations do not get an automatic proposal; use the button. New ones from now on do.

## 2.9.0 – 9 Nov 2026

**New**
- **Three boxes on a page.** Box 1 is "Read more", as before. Two new ones, both with markup in the page code that Google reads (schema), so the questions and the companies can show up in search and AI answers:
  - **Box 2 – "Værd at vide om [land] før du rejser" / "Know before you go".** Step 6 in the panel: **Propose "Know before you go"**. Translator writes 5–7 questions with short answers, only from facts already in the text (if the text has a list of questions, it uses those). On traveltalk.dk the answers take the Nordic view (flights from Copenhagen, Danish holidays); on traveltalk.travel the international view – no "Danish citizens". You read them in the panel and press **Accept: put the box in**. The box carries FAQ markup for Google.
  - **Box 3 – "Hvem tager dig til [land]" / "Who takes you to [place]".** The suggestions under Deepen → Who takes you there now come in four groups: **local operators and guides, airlines, travel agencies** (Nordic ones on traveltalk.dk) and **getting around** (domestic flights, trains, car hire). Each comes with its website, checked. Tick the ones that fit and press **Put them in the box**: the box is put in the text, grouped, each company linked to its website, and each goes onto Translator → Outreach. Only where you tick something (G, 9 Nov). When you come back, the companies already in the box are ticked; untick to take one out.
- Each box sits in the text between invisible markers, so pressing the button again replaces the box instead of adding a second one, and the box travels with the text into translations.

**What you do differently**
- On a destination article: step 6 → Propose "Know before you go" → read → Accept.
- Under Deepen: Check gaps again → tick companies → Put them in the box → Translator → Outreach for the mail.

**Good to know**
- Companies are named and linked, never ranked or graded, airlines included (house style). We sell no trips.
- An older translation can still say "Danish citizens" in an FAQ written before 2.6.0; it changes when the page is translated again, or by hand.
- The boxes have a light frame in the site's colours; tell Claude if they should look different.
- Tested: the code loads without errors, and putting and replacing a box was tried on sample text. Not tested on the live sites.

**Older translations**
- Not affected until a box is added; then the box goes along at the next translation.

## 2.8.0 – 9 Nov 2026

**New**
- **Who takes you there – with their websites, checked.** The suggested local companies now come with their website, and Translator checks that the site answers: "✓ website answers" or "✗ website does not answer". Open it, judge the fit, and tick only those you want on the site. The ticked ones go into one section, each name linked to its own website. The old line asking whether they want a direct link is gone.
- **Translator → Outreach.** Every company that goes onto the site with a link lands on this list: company, website, the article, the site, the date. For each there is a ready mail ("a free test ride on Traveltalk…", in Danish for traveltalk.dk articles, otherwise English) to copy into your own mailbox, a status (New, Mailed, Replied, No reply, Working with us, Not interested) and a note. **Download CSV for LeisureRelate** gives the list for Relate, so Mio can take it from there.

**What you do differently**
- In "More depth", under Who takes you there: open the website, check the fit, tick, Write the ticked sections, read, add.
- Then Translator → Outreach: copy the mail, send it from your own mailbox, set the status to Mailed.

**Good to know**
- Nothing is sent from Translator. The mail is always sent by a person.
- "Website answers" means the address replies; it does not prove the company is the right one. That is your check.
- Tested: the code loads without errors. Not tested on the live sites.

**Older translations**
- Companies you linked by hand before this version are not on the list; add the next ones through the section.

## 2.7.4 – 9 Nov 2026

**New**
- **Propose links finds articles on traveltalk.travel.** On a translation it only looked among other translations, but most English articles on traveltalk.travel are the site's own posts, so on the Tanzania test it found nothing to link to and came back empty. It now also looks among the site's own posts and pages. The same applies to the links in newly written sections.

**What you do differently**
- Try Propose links again on the Tanzania post.

**Good to know**
- Tested: the code loads without errors. Not tested on the live sites.

**Older translations**
- Not affected.

## 2.7.3 – 9 Nov 2026

**New**
- **Propose links** (step 5 in the panel). Translator puts links into sentences the text already has: 3 to 6 internal links to the site's own articles in the same language, and at most 2 external links to official or primary sources (a park authority, a tourist board, a government page) – never booking sites, operators or blogs. An external link is only proposed if the page answers. You see each one (the words and where they lead) and press **Accept: put them in the text** or **Reject**. Nothing changes before that. Headings and existing links are left alone.
- **Set SEO keeps your keyword in the meta description.** When a page already has a focus keyword, Set SEO now writes the meta description around exactly that keyword, so Rank Math's "Focus Keyword not found in your SEO Meta Description" goes green. Before, it wrote the meta for a new suggested keyword, which is why "Safari parks in Tanzania" was missing from it.

**What you do differently**
- On a text with few links: step 5 → Propose links → read the list → Accept.
- Where Rank Math says the keyword is missing from the meta: step 4 → Set SEO again.

**Good to know**
- On the Tanzania post these two fix four of Rank Math's red lines (keyword in meta, internal links, external links, DoFollow external links). "Keyword density is low" stays red on purpose: the house style says not to repeat the keyword to please the meter.
- If you edit the text after links were proposed, Accept refuses and asks you to propose again, so your edits are not lost.
- Tested: the code loads without errors, and the link placement was tried on sample text (it skips headings and existing links). Not tested on the live sites.

**Older translations**
- Not affected; use the buttons where you want them.

## 2.7.2 – 9 Nov 2026

**New**
- **Your unsaved edits are saved before a Translator button runs.** If you have typed something (a link, a name, a sentence) and then click a Translator button before pressing Update, the editor used to leave the page and the unsaved edits were gone – the button then worked on the last saved text. Now Translator saves your edits first ("Saving your edits first, then: …") and only then runs. In the classic editor, where it cannot save for you, it stops and asks you to press Update first.

**What you do differently**
- Nothing: type, then click. If you use the classic editor and see the message, press Update and click again.

**Good to know**
- This is the likely reason the links and safari names you added in "Safariparker i Tanzania" disappeared after 2.7.1: they were added in the editor but not yet saved when a Translator button was clicked. Inferred from how the editor works; not seen on the live site.
- The Rank Math score is not a ranking signal (house style, SEO). A drop from 72 to 70 after the text grew is the density meter reacting to more words around the same keyword – ignore it. Check only that the keyword is in the title, the meta description, the address and the first paragraph.
- Tested: the code and the screen script load without errors. Not tested on the live sites.

**Older translations**
- Not affected.

## 2.7.1 – 8 Nov 2026

**New**
- **Your own edits on traveltalk.travel are no longer overwritten.** Until now, when traveltalk.dk sent a new copy of a translation that was still a draft on traveltalk.travel, the copy replaced the draft – including names, links and sections you had added by hand. That is how the three safari companies and your internal links disappeared. Now a draft you have edited is left alone: the new copy waits, and the "Translator – steps" panel shows "A new version is waiting" with Accept / Reject.
- **Accept warns before it throws away edits.** If you edited the text after a waiting version (or a proposed structure) was made, Accept stops and says so: "Back: keep my text" or "Accept anyway".
- **Written sections now contain internal links.** When Translator writes new sections (Find content gaps → Write the ticked sections), it links to the site's own articles where they fit, one to three per section, chosen from up to 40 related articles in the same language. It can only use addresses that exist; anything else keeps just its words.

**What you do differently**
- After this, add your own links and names freely; they stay.
- If a version is waiting on a draft you have edited, Reject it unless you want the new copy.

**Good to know**
- Drafts on traveltalk.travel made before this version are treated as edited, so they are never overwritten: the next copy from traveltalk.dk waits instead.
- What was lost before this version cannot be brought back by the plugin; look under Revisions on the edit screen – the edited version may still be there ("Browse" revisions, then "Restore This Revision").
- Rank Math's score is not something Google uses; the house style says to look at its placement checks (keyword in title, meta, URL, first paragraph) and ignore the density meter. Links in the text do help readers and Google; the Links step shows them.
- Tested: the code loads without errors. Not tested on the live sites.

**Older translations**
- Applies from installation on. Lost edits can often be restored from Revisions.

## 2.7.0 – 8 Nov 2026

**New**
- **"Translator – steps": one panel at the top of every edit screen** (posts, pages and translations, on both sites). The work in the order it is done, each step with its state – **✓ done**, **● waiting for you**, **● to do** or **– not needed** – and one button that does the next thing:
  1. **Check** (translations): Fix the flags, or Accept / Reject a version that is waiting.
  2. **Deepen**: words against the minimum; Find content gaps, or go straight to the suggestions or the sections waiting to be read.
  3. **Structure**: intro, practical part, a heading that repeats the title, broken shortcodes; Propose the structure, or Accept / Reject.
  4. **SEO**: the keyword and the meta length; Set SEO (translations).
  5. **Links**: how many links the text has to this site (and to the sister site), and how many pages on this site link to it. "Show the links" lists both, and marks links that point nowhere. "Count again" recounts.
  6. **Publish** (translations): what is still needed before Publish.
- The detailed boxes stay where they were; the panel tells you where to look.

**What you do differently**
- Start every article at the panel and work down it.

**Good to know**
- Links are counted in the text itself. Menus, the article grid and the Read more block are not counted, so a page can be well linked in practice and still show few links in.
- A page counts as linking in only once it is published. The count is kept for six hours; "Count again" refreshes it.
- Tested: the code loads without errors. Not tested on the live sites. Please check the panel on the four cases (traveltalk.dk post and page, traveltalk.travel post and page).

**Older translations**
- Applies straight away to every post, page and translation; nothing in the texts changes.

## 2.6.4 – 8 Nov 2026

**New**
- **You can see when Translator is working.** Every Translator button that works on the server (Find content gaps, Write the ticked sections, Fix the flags, Propose the structure, Set SEO, Suggest, and the others) now shows a dark bar at the top of the screen: what it is doing, that it usually takes 20–60 seconds, and not to click again. The other Translator buttons are greyed out until the page comes back. After 90 seconds the bar says it is still working.
- **You can see when it is done.** The result appears in a green "Done:" bar at the top that stays until you close it. It also shows in the block editor, which used to hide these messages.
- **Clearer words on the buttons that change your text.** "Apply it" is now **Accept: put it in the text**; "Discard it" is now **Reject: keep my text**.
- **Clusters → Travel interests:** the switch shows its state as a green **ON** or grey **OFF**, with a button beside it saying **Turn on** or **Turn off**.

**What you do differently**
- Click once and wait for the green bar.

**Good to know**
- The next step for the screens (grouping related actions so you know where to look) is described in the handover; it is a larger change and comes as its own version once agreed.
- Tested: the code loads without errors and the new screen script was checked for errors. Not tested on the live sites.

**Older translations**
- Not affected.

## 2.6.3 – 8 Nov 2026

**New**
- **The flags go away when they are dealt with.** On traveltalk.travel, "Fix the flags" did nothing on translations that came from traveltalk.dk: the original sits there, so the plugin stopped at "Nothing to fix". It now fetches the original from traveltalk.dk. Passages the fix judges as wording only leave the list.
- **No more false flags.** The check sometimes listed a passage and then said in its own note "Equivalent; no omission". Such lines are no longer flags: they leave the list, the count and the publishing block. A real difference, such as a changed number, stays.
- **"Translation: what to do now"**, a box at the top right of every translation, beside Update. It shows one thing: a waiting version with a large **Apply it** button, or the number of flags with a large **Fix the flags** button, or "No flags".
- **The pillar tick stays.** Working with Translator's buttons (structure, more depth, fix, improve, apply) no longer removes Rank Math's pillar tick. A translation sent from traveltalk.dk carries the original's pillar tick with it. The Structure box shows "Pillar: yes, ticked" or "no", so you can see it at a glance.

**What you do differently**
- Install on both sites.
- On a translation, use the box at the top right: Fix the flags, then Apply it.

**Good to know**
- Ticking and unticking pillar is still done in Rank Math; Translator only shows it and keeps it.
- Tested: the code loads without errors, and the rule for false flags was tried on the notes from your screenshot (Equivalent; no omission / Equivalent wording; no difference / Equivalent: cleared; a changed number: kept). Not tested on the live sites. Please test the four cases (traveltalk.dk post and page, traveltalk.travel post and page): flags, Fix and Apply, the pillar tick after using a button, and the review tick.

**Older translations**
- Applies straight away: false flags disappear from existing translations when you open them. Pillar ticks already lost are not put back by themselves; tick them again in Rank Math once.

## 2.6.2 – 8 Nov 2026

**New**
- **"More depth" on translations that came from traveltalk.dk** (traveltalk.travel). These translations have their original on the other site, so the gap check had nothing to read and the suggestions for more text never appeared. The Translation check box now has a "More depth" part: Find content gaps checks the translation itself, you tick what to add, and the sections are written in the translation's own language, for that translation only.
- **Set SEO shows what is set.** Under the button you now see the focus keyword and the meta description (with its length), so you can see it worked without opening Rank Math. The button then reads "Set SEO again".
- **"I have read the check" is never ticked for you.** A copy that arrives from traveltalk.dk as a draft arrives unticked. Adding sections or applying a new structure unticks it. The browser can no longer restore an old tick when the page reloads.
- **Structure: the result is checked.** After "Apply it", the plugin checks that the text really changed. If it did not, or something changed it back straight after, it says so instead of reporting success.

**What you do differently**
- Install on both sites.
- After "Apply it" in the Structure box, reload the edit page before you press Update, so the editor does not save its old copy over the new text.

**Good to know**
- Tested: the code loads without errors. Not tested on the live sites. Please test the four cases: traveltalk.dk post, traveltalk.dk page, traveltalk.travel post, traveltalk.travel page. For each: the tick (unticked until you tick it), Structure (Apply it, then reload), More depth / Find content gaps, and Set SEO.

**Older translations**
- Ticks given before this version on drafts that came from traveltalk.dk stay until the text changes. Untick and tick again if in doubt.

## 2.6.1 – 8 Nov 2026

**New**
- **"Pages win" now works on traveltalk.dk.** In 2.6.0 the switch was on but the golf address still showed the category: the plugin waited for a signal that traveltalk.dk's address setup never gives. It now decides on the address itself, and runs after every other plugin, so a page and a category at the same address show the page.
- Each such address now carries a small technical marker that tells Claude, from outside, whether the page won. Readers do not see it.

**What you do differently**
- Install on traveltalk.dk (and traveltalk.travel, to keep both on the same version).
- Then LiteSpeed Cache → Toolbox → **Purge All** once on traveltalk.dk, so the cached category pages go.
- Tell Claude when it is done; Claude checks golf, mad-og-vin, storbyferie and charterferie from outside.

**Good to know**
- "Page 2" and later still list the category's articles, as before.
- Charter, bus and business travel are never promoted.
- Tested: the code loads without errors. Not tested on the live site; checked from outside after you install.

**Older translations**
- Not affected.

## 2.6.0 – 8 Nov 2026

**New**
- **Clusters → Travel interests** (traveltalk.dk). One table with every travel interest: its page and its word count, its category and number of posts, and its state. "Page hidden by the category" means a page and a category share an address and readers only get the category. On traveltalk.dk that is 28 interests, golf among them: the golf page has 850 words nobody sees. "Thin" marks a page under the word minimum. "No page" marks an interest that only has a category.
- **Pages win shared addresses** (a switch on that tab, off until you switch it on). When on, an address such as /rejseinteresser/golfrejser/ shows the page, with the category's newest articles listed under it and a link to the rest. No address changes, nothing is redirected, nothing is deleted. Charter, bus and business travel are never promoted (house style: out on mission grounds).
- **Translations take the international view.** Texts on traveltalk.dk speak to Danish and Nordic readers ("tæt på Danmark", "danske golfere", Danish airports). Their translations now say the same thing for international readers, without the Danish point of view, and never swap Denmark for another country.

**What you do differently**
- Install on both sites (traveltalk.dk first).
- On traveltalk.dk: Translator → Clusters → Travel interests. Read the table, then press **Switch on**. Open three interest pages (golf, mad-og-vin, storbyferie) and check that the page text shows with the articles under it.
- If something looks wrong, **Switch off** puts everything back as before at once.

**Good to know**
- After switching on, LiteSpeed's cache is emptied so the pages show at once; the first visits are a little slower.
- The site may already show a grid of articles on these pages. If you see the same articles twice (grid and list), tell Claude and the list goes.
- New translations after this version use the international view. Existing translations change only when they are translated again.
- Tested: the code loads without errors. Not tested on the live sites: the switch, the pages under it, and the article list. Try it at a quiet time and check the three pages straight after.

**Older translations**
- Not affected until they are translated again; then they get the international view.

## 2.5.3 – 7 Nov 2026

**New**
- **"I have read the check" is no longer ticked in advance.** The tick now belongs to one version of the text and its check. When the text changes by itself (sections added, a waiting version applied, a new copy arriving from traveltalk.dk) or the check is run again, the box is unticked, so you tick it after reading, not untick and tick again.

**What you do differently**
- Install on both sites.
- Read the check, then tick. If you edit the text yourself and save with the box ticked, it stays ticked.

**Good to know**
- Translations that are already published keep their tick from before. Drafts ticked before this version show unticked once: read the check and tick again.
- Tested: the code loads without errors. Not tested on the live sites.

**Older translations**
- Applies from installation on. Published translations are not affected; unpublished drafts need one fresh tick each.

## 2.5.2 – 7 Nov 2026

**New**
- **"A heading repeats the title."** The Structure box on the edit screen now says when a heading inside the text only repeats the page title, as on the Botswana country page ("Botswana" as title and again as the first heading). The house style wants the title once. You decide each case: rename the heading to what its section is about, or remove it.
- **"A shortcode without its opening or closing tag."** The Structure box also says when a shortcode is incomplete, as in the Botswana safari article, where "[/nordic]" stands twice and "[nordic]" is missing. Readers then see the brackets as text, and every translation copies the fault. Fix it in the Danish original before it is translated.
- **Both show in the lists too.** The Structure column in the post and page lists shows "title twice" or "broken shortcode" in red, so you can find the pages without opening each one.

**What you do differently**
- Install on both sites.
- On traveltalk.dk, sort or scan the Structure column for the red marks and fix the pages one by one. Botswana: the country page (heading "Botswana") and post 82859 (first "[/nordic]" should be "[nordic]").
- After fixing an original, the translations are offered the new version as usual.

**Good to know**
- These are marks only. Nothing is changed in any text by itself.
- "Repeats the title" means the same words, ignoring capitals and punctuation. A heading such as "Botswana i dag" is not marked.
- Tested: the code loads without errors, and the shortcode check was tried on the Botswana fault (it finds 0 opening and 2 closing tags). Not tested on the live sites.

**Older translations**
- Not affected, but they show the same marks when their original has the fault. Fix the original; the translations follow when they are translated again.

## 2.5.1 – 7 Nov 2026

**New**
- **Links in translations reach pages whose Danish address has moved.** Many older Danish texts link to the old addresses of the country pages, such as "rejsemal-i-hele-verden/afrika/kenya", which traveltalk.dk now forwards to "afrika/kenya". On traveltalk.travel those links lost their target and showed as plain words: on the Botswana page only "Botswana" itself stood out in the list of African countries. They now go to the country's page on traveltalk.travel in the reader's language, or in English.

**What you do differently**
- Install on traveltalk.travel (and on traveltalk.dk, to keep both on the same version).
- If the Botswana page still shows plain names, wait a day or deactivate and reactivate the plugin once: the list of addresses is refreshed daily.

**Good to know**
- A country with no version yet on traveltalk.travel still shows as plain words, on purpose: since 2.2.17 a translation never sends readers into Danish. As more country pages are translated, their names turn into links by themselves.
- Nothing in the Danish texts changes. Updating the old addresses in them is still worth doing one day, but it is not needed for this.
- Tested: the code loads without errors. Not tested on the live site.

**Older translations**
- Applies automatically from installation on, to every translation, as the page is shown.

## 2.5.0 – 7 Nov 2026

**New**
- **Translator → Clusters** (traveltalk.dk). Pick a country page; Botswana opens first. You see every article that belongs to it: those in the country's category and those whose title names the country. For each one: does it link up to the country page, and does the country page link down to it? This is read from the pages as a reader sees them, so the menus, the related-articles grid and the "Read more" block all count.
- **Problems in the set.** The page also reports what only shows when you look at the whole cluster: an article with the same title as the country page (for Botswana: the article "Botswana" competes with the country page), and a country category that does not sit under its continent. These are reported only. Nothing is merged, moved, redirected or deleted.
- **Links from the country page, when you switch them on.** "Switch on for this page" lists the articles the country page does not already link to at its end, under "Mere om Botswana". The page's own text is not changed, and "Switch off" removes the list. An article that competes with the country page is not added to the list.
- **Suggestions.** "Suggest new articles" proposes 4 to 8 articles the cluster lacks, each with a working title and a one-line angle, and lists the site's travel interests that fit the country but have no article for it yet. They are ideas for you to judge; nothing is written. Tell Claude which ones to draft, and the drafts come as Google Docs.

**What you do differently**
- Install on traveltalk.dk. traveltalk.travel does not need it this time; the Clusters page only appears on traveltalk.dk.
- Open Translator → Clusters, look at Botswana, and decide about the problems it reports.
- Switch on the links for Botswana if the list looks right, then open the Botswana page to see it.

**Good to know**
- The first time a country is opened, the site reads each of its pages, which takes a few seconds per article. After that, the result is kept for 12 hours. Press "Read the pages again" after changing a page.
- If the site cannot read its own pages (the host can block that), the link columns show "–" and a warning.
- Which pages count as country pages follows the site's own grid rule: a page with the same address as a category (page "botswana", category "botswana").
- Only traveltalk.dk for now; other sites come when this works well (G, 7 Nov).
- Tested: the code loads without errors, and the link test was checked on Botswana-style addresses. Not tested on the live site: the Clusters page itself, the self-reading of pages, and the list on the country page. Try Botswana first.

**Older translations**
- Not affected. The list on a country page appears only on traveltalk.dk and is never copied into translations.

## 2.4.2 – 7 Nov 2026

**New**
- **Content suggestions that fit the article.** "Find content gaps" now knows what kind of text it is looking at. On a country or destination page it suggests the practical basics, as before. On an article about one subject, such as the Botswana safari piece, it suggests what takes the reader deeper into that subject: kinds of safari, the seasons for wildlife, how the camps differ, local guides, what a day costs. Visa, entry and currency are left to the country page, at most as one line pointing to it.
- **Who takes you there.** On articles about one subject, the check also proposes names of local companies, camps and guides, and up to three companies abroad that sell trips there. They appear under the gaps as **names to check, not verified**, and none is ticked. Tick only those you have checked. They then go into one section, without links and without ranking, ending with the line "Er din virksomhed indforstået med et direkte link, så giv os besked." (in English on English texts).
- **What the English version has that this lacks** (traveltalk.dk). A new button in the Translations box on a Danish article. It reads the English version on traveltalk.travel and lists the parts it has that the Danish text lacks or covers more thinly, with the numbers and names in them. You or Mio write them in Danish. Nothing is added or translated into Danish by itself.

**What you do differently**
- Install on both sites (traveltalk.travel first, then traveltalk.dk).
- On an article you have checked before, press **Check gaps again** to get the new kind of suggestions.
- Check every provider name before ticking it: the engine can be wrong about names. A name you are not sure of stays unticked.
- The line about a direct link has no address in it. If you want readers to write to a specific address, add it by hand to the section before you publish.

**Good to know**
- Whether a text is a "country or destination page" follows the same rule as the word minimum: pages, airline pages and Rank Math pillar content count as hubs; posts count as articles on one subject.
- Translations get the same, better-fitting suggestions in their "Translation check" box.
- The English comparison needs the two sites paired, as for translations, and an English version on traveltalk.travel (draft or published).
- Tested: the code loads without errors, and the instructions sent to the engine were checked for an article and a country page. Not tested on the live sites: what the engine actually returns for Botswana, and the English comparison over the bridge. Please try both on post 82859 first.

**Older translations**
- Not affected. Suggestions already shown stay until you press "Check gaps again". Nothing in any text changes by itself.

## 2.4.1 – 7 Nov 2026

**New**
- **A clearer message when traveltalk.travel refuses a translation** ("HTTP 401" at the save stage). The message used to say "install 2.3.1 there too", which sent you looking for the wrong thing. It now says what to check: that application passwords are switched on at traveltalk.travel (Users → Profile shows an "Application Passwords" section), then Retry, and if that does not help, pair again under Translator → Bridge.

**What you do differently**
- Install on both sites. Nothing else changes.

**Good to know**
- On 7 November the refusals came from TT Admin Speed Fix 1.1, which switched application passwords off on traveltalk.travel. Version 1.2 of that plugin fixed it. If the message appears again, look first at any plugin that has been added or updated on traveltalk.travel.
- Only the wording of the message changed. Tested: the code loads without errors. Not tested on the live sites before handover.

**Older translations**
- Not affected. Translations already saved, published or waiting in the queue stay as they are. A row that failed before shows the old message until you press Retry.

## 2.4.0 – 5 Nov 2026

**New**
- **Airline pages (and other custom post types) get the same tools as posts and pages:** Translations box, Suggest extra content, Structure, Pictures, correction function, bulk queue, and on .travel the "Propose improvements from the Danish original" box. They count as hubs (1500 words minimum).
- **Translator → Settings → Post types:** tick which extra types are included. Until you save it once, types whose name or address says airline/flyselskab/airport/lufthavn are included automatically.

**What you do differently**
- Install on both sites, open Translator → Settings and check that the airline type is ticked, then Save.

## 2.3.2 – 5 Nov 2026

**Fixed**
- **A heading that swallowed the paragraph after it** (`<h3>Heading … paragraph</h3>`). It happens in the classic editor when a heading and the next paragraph are separated by a line break only. On every save, and before a text is translated, the heading is now closed after its first line and the rest becomes normal text again, so translations no longer copy the fault. Works for classic and block text. A deliberate two-line headline (short line after a line break) is left alone.

**What you do differently**
- Install on both sites. An article that already has the fault is repaired the next time it is saved (open it, Update).

## 2.3.1 – 5 Nov 2026

**Fixed**
- **"HTTP 401: Sorry, you are not allowed to do that" at the save stage.** The other site sometimes received the bridge call without its login (the host can strip the login header), so drafts were refused after the translation was paid for. The login now also travels in its own header and is checked by the plugin itself.

**What you do differently**
- Install on both sites (traveltalk.travel first), then click **Retry** on the failed rows in Translator → Queue. No new translation cost: the engine work is kept.
- Still 401 after that: Translator → Bridge on traveltalk.dk, make a pairing code and use it on traveltalk.travel.

## 2.3.0 – 4 Nov 2026

**New**
- **"Most read about [place]" inside the Read more block.** Under the place, region and interest links, the block lists the five related texts that readers have opened most in the last 30 days, in the page's own language. Related means the same category and its sub-categories, sibling and child pages, or, for a translation made on traveltalk.dk, translations under the same place in the breadcrumb. Until at least three related texts have counted readers, the block lists the newest related texts under "More about [place]" instead, so it never claims "most read" without numbers.
- **The plugin counts readers itself.** A small script counts each page once per visitor per browser session, so it also counts when LiteSpeed serves the page from cache. It does not count logged-in editors or visitors that identify as robots. A new column **Views 30d** in the Posts, Pages and Translations lists shows the figure.
- **The list is cached** and refreshed twice a day per page, so pages are not slowed down.
- Switch it off: Translator → Settings → Read more block → untick "Most read about the place".

**What you do differently**
- Install on both sites (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded), then LiteSpeed Cache → Toolbox → Purge → Purge All on both.
- Nothing else. Counting starts on installation; give it a few weeks before the list means much. Until then you see "More about".

**Good to know**
- Counted views are the plugin's own, not Google Analytics, and will be lower. They only rank texts against each other.
- A text that is in no category and has no sibling pages has no related texts and shows no list.
- Not tested on the live sites.

**Older translations**
- Applies automatically from installation on. Views before installation are not known.

## 2.2.32 – 4 Nov 2026

**New**
- **Fewer, better travel interests.** An interest in the Read more block is now offered only when the text is really about it: its name must appear at least four times, or in the title, or in a couple of headings. Before, one passing mention was enough ("Camping" on an article about a Vietnam bike tour). When no interest fits, the block shows the "Related travel interests" link to the overview instead.

**What you do differently**
- Install on both sites (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded), then LiteSpeed Cache → Toolbox → Purge → Purge All on both.
- To name the right interest for one text, use Structure box → Change it → Travel interest page IDs (for example the Adventure travel page).

**Good to know**
- The plugin only matches names that appear in the text. It does not know that a jungle bike tour is adventure travel; that is set by hand per text, or by naming it in the text.
- Not tested on the live sites.

**Older translations**
- Applies automatically from installation on, since the block is built when a page is shown.

## 2.2.31 – 4 Nov 2026

**New**
- **Every text gets a Read more block.** Before, a post whose category has no destination page (or none yet in that language) got no block at all. Now it always gets a way on: "Read more about" its category (articles written on the site itself) or the destinations page, and a "Related travel interests" link to the overview of all interests when no specific interest is named in the text. Texts that have a place, region or named interests look as before.
- **New setting: Destinations page ID** (Translator → Settings → Read more block). On traveltalk.travel it is page 79; on traveltalk.dk leave it at 0 and Danish posts fall back to their category.

**What you do differently**
- Install on both sites (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded), then LiteSpeed Cache → Toolbox → Purge → Purge All on both.
- On traveltalk.travel: Translator → Settings → Read more block: check Destinations page ID = 79, Travel Interests page ID = 84, Never link = 79,84 → Save.
- To give one text exact links instead: Structure box → Change it.

**Good to know**
- On traveltalk.travel, translations of Danish posts have no category of their own, so without a place they link to the destinations page.
- Not tested on the live sites.

**Older translations**
- Applies automatically from installation on, since the block is built when a page is shown.

## 2.2.30 – 4 Nov 2026

**New**
- **Travel interests from a category.** Settings → Read more block has a new field, Travel Interests category ID, for a site where the interests are categories, as on traveltalk.dk (Rejseinteresser). The Read more block then offers up to three of its sub-categories that the text mentions, linking to the category pages. Nothing else in 2.2.29 changes.

**What you do differently**
- On traveltalk.dk: Translator → Settings → Read more block → Travel Interests category ID: 3053 → Save. Leave the page ID field at 0 there.

**Good to know**
- Only sub-categories of 3053 are offered, and only those with posts. If Rejseinteresser has no sub-categories, the .dk block shows the place and region lines only.
- Category interests show on Danish texts only. Translations on traveltalk.dk use the interests pages on traveltalk.travel, as before.
- Not tested on the live sites.

**Older translations**
- Not affected. The block is built when a page is shown.

## 2.2.29 – 4 Nov 2026

**New**
- **Translations show as new posts on traveltalk.travel.** English translations of articles are now listed with the site's own posts: on the front page, the blog page, the RSS feed and in latest-posts blocks, newest first. Before, they were never listed, so a translation like post 2779 did not show up as new. Category and tag sections still show only posts with that category (translations carry none). Translations of pages (destination guides) stay out of the post lists. Switch: Translator → Settings → Front page.
- **Added sections land where they belong.** Ticked extra content and "Propose improvements" no longer drop sections at the end. A section goes after the heading it belongs under (matched even when the wording differs slightly); when no heading is named, after the section that talks about the same things; when nothing fits, just before the practical part at the end, never after it. A heading inside a Kadence row or column no longer sends the section to the end: it goes inside that column, after its text.
- **One structure for every text: intro, middle, practical part last.** A new **Structure** box on every post, page and translation shows ✓/✗ for the intro (40–150 words before the first heading) and for the practical part (last). **Propose the structure** writes a missing or weak intro, moves practical sections (getting there, when to go, getting around…) to the end, and writes a short practical part from facts already in the text when there is none. It waits for you to apply or discard; nothing is invented. Applying on an original queues its languages again, so the translations follow. A **Structure** column in the Posts and Pages lists shows where work is needed.
- **Read more block at the end of every text, in its language.** "Read more about Singapore · Read more about Asia · Related travel interests: …", linking the place's page, its region's page and up to three Travel Interests pages the text mentions. It uses the same path as the breadcrumb, so translations link to the versions in their own language and leave out levels not yet translated. Change the links or switch it off per text in the Structure box; put `[lmg_read_more]` in the text to place it elsewhere.

**What you do differently**
- Install on traveltalk.dk and traveltalk.travel (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded). Then LiteSpeed Cache → Toolbox → Purge → Purge All on both.
- Check Translator → Settings → Read more block: on .travel the Travel Interests page is 84 and the skipped top pages are 79 and 84. On traveltalk.dk fill in its own Rejseinteresser page ID (0 until then = no interests line).
- Work the ✗ marks in the Structure column, longest and most read first.

**Good to know**
- SEO: the Read more block is a few links to the hub pages above the text and to closely related interests, the same on every text, printed in the page itself (Google reads it). It does not replace the best links inside the text, which still count most.
- News posts keep their text as written; they get the Read more block but no structure proposals.
- Checked for errors in the code and the placement rules tested on sample texts outside WordPress. **Not tested** on the live sites.

## 2.2.28 – 3 Nov 2026

**New**
- **Search on traveltalk.travel finds translations.** Until now, search there left out everything that came over from traveltalk.dk, so "Holland" found nothing although The Netherlands (Holland) is published. Search on the English site now finds English translations alongside the site's own articles and pages. Versions in other languages are not mixed into the English results.
- **Translations can be added to menus on traveltalk.travel.** In Appearance → Menus, a "Translations" box now sits beside Pages and Posts. traveltalk.dk is unchanged: its translations still stay out of its search and menus.

**What you do differently**
- On traveltalk.travel: Appearance → Menus → main menu → tick "Translations" under Screen Options if the box is hidden → search "Netherlands" → add it under Travel Destinations → Europe → Save Menu. Add other translated destination guides the same way.
- After installing on both sites: LiteSpeed Cache → Toolbox → Purge → Purge All on both.

**Good to know**
- The Travel Destinations menu is hand-made. Publishing a translation never adds it to a menu by itself.
- Search in German, French and the other languages is not changed in this version.
- Contains everything from both 2.2.26 releases (Translate everything, and Alt texts) and from 2.2.27.
- Checked for errors in the code only. Not tested on the live sites.

**Older translations**
- Applies automatically to every published English translation on traveltalk.travel, from installation on.

## 2.2.27 – 2 Nov 2026

**New**
- **News is translated exactly as written.** A post in a News category (News, Nyheder, Rejsenyt) and the Travel News and Rejsenyt pages get no "thin" mark, no content-gap suggestions and no offer to write extra sections, in any language. They are never hidden from Google for being short. The same goes for anything where you tick the new **Translate as written** box in the Translations box on the edit screen (for other editorial texts you want left exactly as they are).
- **Find pictures is sharper.** Words now match only as whole words ("sea" no longer finds "season"). A picture's alt text and title count most, its caption next, its file name least. When a section heading gives three or more search words, a picture must match at least two of them. Under each suggestion you see why it was offered ("Matched: riquewihr (alt text), alsace (title)"). When a heading finds nothing, the article title's words are tried on their own, and the page says so; before, they were mixed in with the heading's words, which brought in many off-the-mark pictures.
- **Clearer names inside the plugin.** Parts that served "the AI engine" were named after Gemini although Claude does the work on both sites. Nothing changes in what you see, except that the Gemini key field in Settings now says "saved" only when a Gemini key really is saved.

**What you do differently**
- Install on traveltalk.dk and traveltalk.travel (Plugins → Add New Plugin → Upload Plugin → Replace current with uploaded).
- News: nothing, if the post is in the News category or is the Travel News or Rejsenyt page. For any other text you want translated as written, tick **Translate as written** in the Translations box before you queue the languages.
- Find pictures: open it from the Pictures box as before. If you get too few suggestions, Translator → Settings → **Find pictures**: untick "at least two of them" for the wide search.

**Good to know**
- "Translate as written" decides whether the plugin suggests additions; the translation itself was never meant to add anything, and it does not.
- Not yet covered: translations sent from traveltalk.dk to traveltalk.travel. If a Danish news post is translated on traveltalk.dk and sent over, its copies on traveltalk.travel can still show the "thin" mark there. It is only a mark (they are indexed, since you set the limit to 0), and the suggestions it offers can be ignored. News written on traveltalk.travel itself, like Travel News, is fully covered.
- Videos: they were already kept as they are in translations. The Travel News languages lacked the video because they were made before it was added to the English page.
- Tested: the whole-word matching and the two-word rule on samples outside WordPress; every file checked for errors. **Not tested** on the live sites: Find pictures on a real article (try "Europe Does Not Change at the Border", which gave the wide results), and the News marks on the Travel News page.

**Older translations**
- From installation on: news posts and the Travel News and Rejsenyt pages, and all their translations, lose the "thin" mark and the suggestions straight away. Nothing in their text changes. Find pictures works the new way on every article. No catch-up needed.

## 2.2.26 (Translate everything) – 3 Nov 2026

**New**
- **Translator → Translate everything.** One Start button. The plugin finds every published article on the site that has no version yet in a language and works through them in the background, until nothing is missing. You can close the page; Pause stops it. The page shows, per language, how many have a version, how many are in the queue, what could not be done (with the reason) and what comes next.
- **English first, pages before posts.** Languages are worked in the order English, German, French, Spanish, Italian, Portuguese, Swedish, Norwegian, Finnish. Within a language: the IDs you paste under "Do these first", then pages (longest first), then posts (newest first).
- **Several at once.** "Languages side by side" (2 = English and German at the same time) and "Workers at a time" (2 = two translations made at the same moment). The background workers and the Queue page can run at the same time, each on a different translation.
- **x-default.** Google's "world default" (x-default) points to the English version as soon as one is published, as before. Pages that have, say, German but no English still point to the Danish original: the page lists them, and their English is queued first. Check Google tags notes them too.

**What you do differently**
- Install on both sites (traveltalk.dk does the work). On traveltalk.dk: Translator → Translate everything → choose languages and settings → Save → Start.
- Results are **drafts for review**, as before. Tick "Publish what passes the check" to have them published like the translations of new articles (flagged ones held back, all listed under Auto-published on traveltalk.travel).
- If the site gets slow or answers 508, set "Workers at a time" to 1.

**Good to know**
- Left out by themselves: the front page, the blog page, password-protected pages, pages set to noindex in Rank Math and very short ones. Add IDs under "Leave out" for more.
- A translation that fails is not tried again by itself; Retry it in the Queue or press "Try these again".
- Works on any site with the Translator, also one without a partner site: there the versions stay on that site.
- Tested on stand-ins for WordPress (order, lanes, locks, background), not on the live sites. Please start with Workers 2 and watch the first hour.

## 2.2.26 (Alt texts) – 2 Nov 2026

**New**
- **Alt texts no longer stops on a map or an outside picture.** Claude fetches each picture itself, and other websites (Google's maps, for example) tell it not to. Before, one such picture stopped the whole check with "This URL is disallowed by the website's robots.txt file" (seen on the Central Europe road-trip article). Now only pictures from traveltalk.dk and traveltalk.travel are sent; maps and other outside pictures are left out and the line for that post says how many ("1 picture(s) left out").
- **If Claude cannot fetch one picture, the post is not abandoned.** The others are checked one by one and the one that fails is left out.
- **The post-ID box says so when it finds no numbers.** Typing words (for example "the strongest in Search Console") used to be ignored without a word, and the plugin checked the next unchecked post instead. Now it stops with a message. Numbers separated by spaces, commas or new lines work as before; an empty box still means "the next unchecked posts, newest first".

**What you do differently**
- Nothing. In Translator → Alt texts, type post numbers only, or leave the box empty.
- Pictures that were left out (maps, outside pictures) keep their alt text as it is; give those a text by hand in the article if needed.

**Good to know**
- Install on traveltalk.dk and traveltalk.travel (2.2.26 contains 2.2.24 and 2.2.25 too, see below: install it instead of those, not after them).
- Tested on stand-ins for WordPress: which addresses count as our own, and that the file has no errors. **Not tested** on the live sites: a real check of the road-trip article (the post that stopped) and a post with several pictures where one fails.
- This build also carries everything in 2.2.24 and 2.2.25 below, including the automatic publishing of new articles' translations. Read those notes before installing.

**Older content**
- Not affected. Alt texts already applied stay as they are. Posts that were checked before are not checked again by themselves; a post that stopped earlier is simply checked again when you give its number.

## 2.2.25 – 1 Nov 2026

**New**
- **A new article is translated into every ticked language by itself.** About 30 minutes after a new article is first published (time for last touches), the plugin translates it into every language ticked in Translator → Settings → "Translate into", one step a minute in the background. It applies to articles published from now on, not to older ones, and not to Pages. Nothing else in the queue is touched: translations you start by hand run as before.
- **Those translations are published at once, as you decided, and you are told.** One e-mail arrives about an hour after the first one is made: what was published (with its address) and what is waiting. Translator → **Auto-published** (on traveltalk.travel) lists them all until you click "Mark all as looked at" or tick a translation as read on its own screen. A notice on the Translator pages shows how many are not looked at yet.
- **Flagged ones are not published.** If the check finds a language doubt, a number that changed or a gap in the text, that translation stays a draft and is listed as waiting for you. Untick "Hold back" in Settings if you would rather have them published too.
- **A short welcome note on translated pages of traveltalk.travel,** once per visitor (60 days), in the page's own language: "New in your language every few days: guides from traveltalk.dk, checked by our editors. Come back soon ✈" (nine languages). It appears about 2 seconds after the page opens, waits while a cookie banner is up, stays about 7 seconds, stays while the pointer rests on it, and has a ×. It gives way to "Back to traveltalk.dk" while that note is up.

**What you do differently**
- Install on both sites. The work runs where the article is written (traveltalk.dk for Danish articles); the list and the e-mail are on traveltalk.travel, so both must run 2.2.25.
- Settings has a new row **New articles** (three tick boxes, all on, and the e-mail address; empty means the site administrator) and a fourth tick box in **Between the two sites** for the welcome note.
- The welcome note says "checked by our editors" and "every few days": make sure it stays true. Untick the welcome note, or the automatic publishing, in Settings at any time.
- To look at the welcome note: add #lmg-welcome to the end of a translated traveltalk.travel address.

**Good to know**
- Automatic publishing is a change from "every translation is read before it is published" (26 Oct). You read them afterwards, all of them, in the Auto-published list.
- The background work needs WordPress's own scheduler, which runs when someone visits the site. On a quiet night a translation can take longer.
- If the original is edited while it is being translated, that translation stops with a message and is not published; retry it from Translator → Queue.
- Tested: the queue, the 30-minute delay, hold-back, publishing, and the manual queue left as before, on stand-ins for WordPress (not the real thing), and the welcome note in Chrome (timing, hover, ×, cookie banner, once per visitor, phone width). **Not tested** on the live sites: a real new article through all steps, the e-mail, the Auto-published page, the real cookie banner. Please watch the first new article closely.

**Older translations**
- Not affected. Existing translations and the existing queue are left as they are; only articles published from now on are handled automatically. The welcome note appears on all translated pages from installation on.

## 2.2.24 – 1 Nov 2026

**New**
- **"← Back to traveltalk.dk" now shows for everyone who clicks over from traveltalk.dk,** also when their browser or an extension hides where they came from (as on the laptop you tried). Links from traveltalk.dk to traveltalk.travel now end in a short marker. traveltalk.travel reads it and removes it from the address at once. It does not change which page opens.
- **The links back to traveltalk.dk's front page go straight to www.traveltalk.dk,** with no redirect in between ("Dansk · traveltalk.dk" in the button on front pages and listings, and the back note on pages without a Danish original).
- A reader who closed the back note and then clicks over from traveltalk.dk again sees it again.

**What you do differently**
- Install on both sites. The marker is written on traveltalk.dk and read on traveltalk.travel, so the fix works only when both run 2.2.24. There is nothing new to set.
- The back note appears after a click from traveltalk.dk (language button, "Read in" line, line at the bottom of the page, or the English offer). It does not appear when you type the address or use a bookmark. To look at it anyway, add #lmg-back to a traveltalk.travel address.

**Good to know**
- The marker is only in links readers click on traveltalk.dk. It is never in the language tags (hreflang), the canonical addresses, the sitemaps or the redirects, and Google ignores it.
- If "Back to traveltalk.dk" is switched off in Translator → Settings → Between the two sites, the marker is still removed from the address.
- Tested: the links on stand-in data for both sites (the language button, the "Read in" line, the bottom line, the English offer) and the note in a real browser (Chrome) with the referrer withheld, closed and reopened, with the setting off, and through a real click from the language button into the new tab. **Not tested** on the live sites, or in Safari and Firefox.

**Older translations**
- Not affected. Applies to every page automatically from installation on; no catch-up needed.

## 2.2.23 – 1 Nov 2026

**New**
- **The language button on traveltalk.dk now leads every language to traveltalk.travel.** On the front page and other listings it used to link to leftover language pages on traveltalk.dk (English, Deutsch, Svenska) and said "not yet translated" for Français, Español, Italiano, Norsk and Suomi, although traveltalk.travel has them. Now each language goes to traveltalk.travel: the same article in that language when it exists there, otherwise that language's front page. A language traveltalk.travel does not have yet (Português today) still says "not yet translated".
- **The button says when you leave the site.** Every link to the other site carries an arrow (↗) and opens in a new window, so the reader's traveltalk.dk page stays open behind it. At the bottom of the list on traveltalk.dk: "↗ traveltalk.travel". On traveltalk.travel the Danish entry reads "Dansk · traveltalk.dk".
- **Visitors who do not read Danish are offered their language, never moved.** On traveltalk.dk, a visitor whose browser is not set to Danish sees a small note above the language button: "Read this page in English ↗" (or Deutsch, Français … when this page exists in the browser's language on traveltalk.travel). It only appears when that page really exists there. Closing it, or using it, hides it for 60 days. A browser that lists Danish at all never sees it.
- **A way back on traveltalk.travel.** A visitor who arrives from traveltalk.dk sees a small note above the language button, "← Back to traveltalk.dk", in the page's own language. It goes to the Danish original of the page they are on (the traveltalk.dk front page when there is none). The × closes it for the rest of the visit.

**What you do differently**
- After installing on both sites: Translator → Settings has a new row **Between the two sites** with three tick boxes, all on. New window for links to the other site (both sites); the English offer (traveltalk.dk); the way-back note (traveltalk.travel). Untick any one you do not like and save.
- To see a note without being the right visitor: add **#lmg-offer** to the end of any traveltalk.dk address, or **#lmg-back** to the end of any traveltalk.travel address.
- Nothing to catch up. The page cache is cleared by the install itself. If a page still shows the old button after a few minutes: LiteSpeed Cache → Toolbox → Purge → Purge All.

**Good to know**
- **Leaving traveltalk.dk is always the reader's own click.** Before, a reader who had once chosen English on traveltalk.dk was moved to traveltalk.travel on every later article that had an English version. That no longer crosses between the two sites. Inside one site it works as before.
- Nothing Google reads has changed: the language tags (hreflang), the canonical addresses and the sitemaps are untouched. The two notes are drawn by the visitor's browser, so cached pages stay the same for everyone.
- The way-back note depends on the browser telling traveltalk.travel where the visitor came from. Nearly all browsers do. If one does not, the note simply does not show; the "Dansk · traveltalk.dk" entry is still there.
- The English offer follows the browser's language setting. A Dane whose browser is set to English only will see it once and can close it.
- Still on traveltalk.dk on 1 Nov: Thailand in English, Deutsch, Svenska, Norsk and Suomi, and Singapore in English. Their own article page links to them until Translator → Catch-up has copied them; then the leftover /en/, /de/, /sv/ pages on traveltalk.dk send readers to traveltalk.travel by themselves.
- Tested: the button's links for traveltalk.dk and traveltalk.travel on stand-in data (front page, article with versions, article with a leftover translation, article with none), and both notes in a real browser at desktop and phone width, with Danish, English, German, French and Japanese browser settings. **Not tested** on the live sites, with real referrers, with LiteSpeed's cache, or on an iPhone.

**Older translations**
- Not affected. This changes the button and two small notes around the pages, nothing in any translation, address or search tag. It applies to every page automatically from installation on; no catch-up is needed.

## 2.2.22 – 31 Oct 2026

**New**
- **The Translations list has one "Words" column, and it sorts.** 2.2.21 added a second "Words" column next to the one that was already there, and only the new one sorted. The extra one is gone; the original column now sorts. Click "Words" in Translator → Translations: shortest first shows the pages that most need filling out.

**What you do differently**
- Nothing else. The indexing change from 2.2.21 (threshold 0, Rank Math sitemap Save, LiteSpeed purge) is unchanged.

**Good to know**
- The red "thin" mark in that column still follows the minimum length for translations (Settings), not the noindex limit. With the noindex limit at 0 you can still see which pages are short.
- Pages saved before 2.2.21 got their length stored when 2.2.21 was installed. If the list looks empty when sorted, tell us.
- Tested for syntax only.

**Older translations**
- Not affected.

## 2.2.21 – 31 Oct 2026

**New**
- **Switching off "Noindex thin translations" now carries through.** On traveltalk.travel, Translator → Settings → "Noindex thin translations": with 0 there, every translation is indexed like the rest (your decision of 31 Oct). When you change that number, the plugin now clears Rank Math's sitemap list and the page cache, and tells traveltalk.dk the new status of every translation whose state changed, six at a time with a pause. Before, traveltalk.dk kept the old status ("thin"), so those translations stayed out of the language links until each was saved again.
- **A "Words" column in Translator → Translations.** It shows each translation's length, in red when it is under the limit. Click the column heading to sort: shortest first shows the pages that most need filling out.
- **The Settings page says how many translations are still waiting** to be re-reported to traveltalk.dk.

**What you do differently**
- After installing on both sites: on traveltalk.travel set "Noindex thin translations" to 0 and save (if you have not already). Then Rank Math → Sitemap Settings → Save changes, and LiteSpeed Cache → Toolbox → Purge → Purge All.
- Then in Google Search Console for traveltalk.travel: Indeksering → Sitemaps, open `sitemap_index.xml` and use the "read again" option if it is offered. Google needs days to weeks to pick the pages up.
- Work from the shortest: Translator → Translations → click "Words".

**Good to know**
- The re-reporting runs in the background (about 30 seconds between batches), so a few minutes pass before traveltalk.dk shows the new status for all. The Settings page counts down.
- Indexing many short pages at once can lower how Google rates the whole site. The Words column is there so the shortest ones can be worked first. Setting the number back to 800 reverses it.
- Not tested on the live sites. The background job was not run against a real traveltalk.dk.

**Older translations**
- Word counts are stored for every translation when the plugin is installed (automatic, a few seconds).
- Translations that were marked thin: they need the setting changed to 0 as above. Installing alone changes nothing about their indexing.

## 2.2.20 – 31 Oct 2026

**New**
- **Pictures are saved on traveltalk.travel.** Until now every picture inside a translation on traveltalk.travel loaded from traveltalk.dk, so traveltalk.dk's host served traveltalk.travel's pages, and Google Images credited traveltalk.dk. On traveltalk.travel there is a new page, Translator → Save pictures. One click copies each picture once into traveltalk.travel's own media library and points the translation at it. A picture used in several languages is copied once. English translations go first; their picture texts give the file names (English, no Danish file names). The other languages reuse the same file.
- **Catch-up on traveltalk.dk says what traveltalk.travel answered.** When it reports a language as "not switched on at traveltalk.travel", it now also lists the languages traveltalk.travel did report. If the language is ticked there and still missing from that list, the answer is out of date and the cause can be found.

**What you do differently**
- On traveltalk.travel: Translator → Save pictures → "Save the pictures". Leave the page open until it says Finished; it works two pictures at a time with a pause. If your computer sleeps or you close the page, open it again and continue: what is done stays done.
- A picture that cannot be fetched is left as it was and named in the log. Tick "also try again the pictures that failed before" to try those again.
- Run the step again after a translation has been applied from a waiting version or copied again: those bring traveltalk.dk's picture addresses back.
- Do not run it at the same time as Catch-up → Copy on traveltalk.dk: both put load on the same hosts.

**Good to know**
- Translations are changed directly: no new revision, no "Mother text changed", no notice to traveltalk.dk, and the saved date stays.
- A picture whose first translation is not English gets the Danish file name if no English translation uses it. The picture text stays in each translation.
- Pictures go in at the size the translation used, with the usual smaller sizes made by WordPress. This uses space on traveltalk.travel and some load while it runs.
- Tested on sample text with a stand-in for the media library. Not tested on the live sites, not tested with Kadence or LiteSpeed. Try it first on one or two translations (stop after the first lines of the log and look at the page) before running all.
- The "not switched on" line itself is not fixed; only its cause is made visible.

**Older translations**
- Pictures: need a catch-up. After installing on traveltalk.travel, run Translator → Save pictures there once. Translations made or applied from now on also need it until a later version saves pictures on arrival.
- Everything else: not affected.

## 2.2.19 – 31 Oct 2026

**New**
- **Keyword proposals use the page's own language.** Catch-up → "Propose keywords" used to ask from the Danish text, so it sometimes answered with the Danish name: Østrig for a Norwegian page, Filippinerne for Norwegian and Finnish, Ungarn for English. It now asks from the translation's own title, with the Danish title only as context, and the answer is the destination's name as speakers of that language write it, with nothing added.
- **A page about no single place gets no proposal.** A theme, a list or the website itself shows "no proposal" instead of a guess.
- **A proposal that is not in the page's own title is shown unticked,** with a red note "not in the page's title – check". A proposal found in the title is ticked as before. Nothing changes until you tick and click "Apply ticked keywords".

**What you do differently**
- On traveltalk.dk: Translator → Catch-up → Focus keyword on destination guides → "Propose keywords" once more, then read the list. Look first at the rows marked in red.

**Good to know**
- The earlier proposals are cleared when the plugin is installed, because they were made from the Danish text. Keywords you already applied are not touched.
- The check is simple: it looks for the proposed name inside the page title. A correct name that the title spells differently (for example a title with an inflected form) is shown unticked and is yours to accept.
- Tested for syntax only. Not tested with a real Claude answer, and not tested on the live sites.

**Older translations**
- Keyword proposals: need a catch-up. Run "Propose keywords" again on traveltalk.dk, as above. Keywords applied earlier stay as they are.

## 2.2.18 – 31 Oct 2026

**New**
- **Breadcrumbs use the short name.** A level above the page now reads "Amerika", not the whole title "Amerika — zwei Kontinente, eine ganze Welt". The short name is the part before the first dash, colon or bar of the page title, or the page's Breadcrumb Title in Rank Math if one is set there.
- **Copied translations leave traveltalk.dk's sitemap at once.** Rank Math keeps the sitemap in a stored copy that a copy to traveltalk.travel did not clear, so all 50 old translations were still listed. The copy now clears it, and the sitemap leaves moved translations out of its counts and pages.

**What you do differently**
- Nothing. After installing on traveltalk.dk, open the translation sitemap once (Rank Math's sitemap, "lmgt_translation" part) and check that translations already moved to traveltalk.travel are no longer listed.

**Good to know**
- The breadcrumb change happens when the page is shown; stored names are not changed. A page whose short name is the same as its title is unchanged. A title such as "Bosnien-Hercegovina" (a dash without spaces) is left whole.
- Tested on sample text and sample titles. Not tested on the live sites, not tested with Kadence, and the sitemap clearing was not tested against a live Rank Math.

**Older translations**
- Breadcrumb short names: apply automatically to every translation, from installation on.
- Sitemap: cleared once on installation on traveltalk.dk; applies automatically after.

## 2.2.17 – 30 Oct 2026

**New**
- **Translations on traveltalk.travel no longer send readers into Danish.** A link in a translation to a page on traveltalk.dk now goes to that page on traveltalk.travel in the reader's language; if it has none, to its English version; if there is no English version either, the link is taken out and its words stay. Links to pictures and files, and the "Read in" and family lines, are not touched. Seen on the Spanish Austria page: 77 of its 85 links went to Danish pages.
- **The related-articles grid follows the same rule.** Each article shows in the page's language, else in English. An article with neither is left out of the grid, instead of appearing in Danish.
- **Pictures with a broken address show again.** Some pictures were stored with a short address (for example "2022/06/picture.png") that loads nothing. Greece had 9 of its 10 pictures broken this way, on traveltalk.dk and on traveltalk.travel. They are now shown from traveltalk.dk's picture folder, on both sites.
- **A copy that is older than its original is marked.** If the Danish original has changed since a translation was made on traveltalk.dk, "Copy to traveltalk.travel" (and the bulk copy in Catch-up) still copies it, but on traveltalk.travel it now shows "Mother text changed" in the Translations list and on the edit screen, so it gets translated again. Before, such a copy looked up to date.
- **"Newer version waiting" in the Translations list on traveltalk.travel.** When a fuller version has arrived for a published translation, the list says so in red. Open the translation and choose Apply it or Discard it, as before.
- **The ID in the Translations list shows once** (it showed twice, for example 21952195 for 2195).

**What you do differently**
- Look for red "Newer version waiting" and "Mother text changed" in Translator → Translations on traveltalk.travel. Read and apply the waiting ones; translate the changed ones again (Re-translate on the edit screen).
- After installing on both sites: LiteSpeed Cache → Toolbox → Purge → Purge All on both, and purge the QUIC.cloud CDN too if it is listed there. traveltalk.dk's outer cache was still showing old pages on 30 Oct (the Greece English address answered normally from the cache while the site itself forwarded it).

**Good to know**
- The link and picture changes happen when the page is shown. The stored text is not changed, so Rank Math's link count in the list still shows the old number of external links.
- "Mother text changed" is decided by the date the original was last saved. A small edit to the original also counts, so a copy may be marked although little changed.
- Pictures still load from traveltalk.dk. Saving them on traveltalk.travel is for a later version.
- Tested with sample pages on a test copy of the code. Not tested on the live sites.

**Older translations**
- Links, the related-articles grid and broken picture addresses: apply automatically to every translation, from installation on.
- Copies made before 2.2.17 from an older original are not marked afterwards. They are marked when copied again or translated again.
- The "Newer version waiting" line shows for every waiting version, including those that arrived earlier.

## 2.2.16 – 28 Oct 2026

**New**
- **Translations leave traveltalk.dk and live on traveltalk.travel.** Google does not accept language versions on a .dk address, so traveltalk.dk keeps Danish only.
  - Once a translation is copied and published on traveltalk.travel, its old .dk address sends readers and Google straight there, for good. The .dk copy is kept out of sight, not deleted.
  - .dk's language front pages (/en/, /de/ …) send readers to the same language on traveltalk.travel once every translation in that language has moved.
  - **Translator → Catch-up → Translations still on traveltalk.dk** (on traveltalk.dk): one button copies the rest, one at a time, with a log. Published ones stay published, drafts arrive as drafts. Where traveltalk.travel already has that article in that language, the .dk copy is simply pointed at it.
  - English is checked first: if traveltalk.travel may have its own English page on the subject, the item is listed for you instead of copied.
  - The departure pages for Swedish, Norwegian and Finnish readers (/se/, /no/, /fi/) stay on traveltalk.dk as they are.
- **Pointers to the international site on traveltalk.dk.**
  - Near the bottom of every page: "traveltalk.travel – our international site: English · Deutsch · …", each language linking to its front page there.
  - On an article with versions on traveltalk.travel, the row near the top now reads "Læs på · Read in: English · Deutsch – traveltalk.travel".
  - Both open traveltalk.travel in a new window.
- **Breadcrumbs in the page's language on traveltalk.travel.** A German page now reads "Startseite / Europa / Österreich" instead of "Home / Österreich": Home goes to the German front page, each level links to its German version where there is one, and shows as plain text where there is not yet.
- **"Copy to traveltalk.travel" is lighter.** Fewer calls between the sites and one Claude call fewer per copy; the picture comes over in a step of its own. If traveltalk.travel answers "resource limit reached" (the error seen on Greece), the Translator waits five seconds and tries once more by itself.
- **Catch-up has an overview.** Translator → Catch-up starts with a table: how many translations each version made, and what later versions may add. New sections: **Focus keyword on destination guides** (the country name, proposed per language; you tick and apply) and **Breadcrumbs**.

**What you do differently**
- After installing on both sites: on traveltalk.travel, Translator → Settings → Translate into: tick **Swedish, Norwegian and Finnish** too, so their few test translations can move.
- On traveltalk.dk, Translator → Catch-up, top to bottom:
  1. **Copy … to traveltalk.travel.** Then check the English items it lists, if any (link the matching English page in the Danish original's traveltalk.travel box, or copy it by hand).
  2. **Send the breadcrumbs.**
  3. **Propose keywords**, look the list over, **Apply ticked keywords**.
- On any translation, "Copy to traveltalk.travel" works as before; the box then says the .dk address sends readers to the new page.

**Good to know**
- The redirect follows the page on traveltalk.travel: if you take it offline there, the .dk address shows its own copy again.
- Applying a keyword changes only the keyword. The meta description and the address stay; the result names the pages whose meta description does not contain the new keyword (use Set SEO there, or edit it).
- A breadcrumb level whose name could not be translated is left out rather than shown in Danish.
- Installing clears the page cache once on both sites, so the redirects and the new line show at once.
- Not yet: ordering the catch-up by Search Console traffic.
- Tested on two test sites talking to each other, with Claude stood in. Not tested on the live sites, with the real Kadence breadcrumb or with Rank Math's breadcrumb.

**Older translations**
- Translations already copied to traveltalk.travel (Greece, Austria English): their .dk address redirects from installation on.
- Breadcrumbs: new translations get them automatically; older ones need the catch-up (Send the breadcrumbs).
- Focus keyword on older destination guides: needs the catch-up (Propose keywords, then apply).
- The article text of a translation is not touched by any of this.

## 2.2.15 – 27 Oct 2026

**New**
- **Hints in English, in more places.** Under every proposal that is not in English, a grey line "In English: …" says what it means, word for word, so any reviewer can follow it, whichever languages they read.
  - Alt texts and Find pictures: under proposals in every language but English, Danish included (2.2.14 gave a Danish line; proposals made then keep theirs).
  - Image texts: under each proposal, when the site's language is not English.

**What you do differently**
- Nothing. Read the proposal, or its English line, and apply.

**Good to know**
- The English line explains the proposal; the proposal itself is written in the page's language.
- Tested on test copies, not on the live sites.

**Older translations**
- Not affected.

## 2.2.14 – 27 Oct 2026 (handed out the same day; 2.2.15 includes all of it)

**New**
- **An alt text comes with every picture you place.** After "Put it here" on Find pictures, Claude looks at the picture and the section it lands in and proposes an alt text right there on the page. Edit, then **Apply**, or keep the one it has.
- **Always in the right language.** Danish on traveltalk.dk, English on traveltalk.travel's own pages, and the page's own language on a translation (German on a German translation, Finnish on a Finnish one). Alt texts on translations now work the same way: Translator → Alt texts lists translations too.
- **A Danish line under proposals in other languages.** For Finnish, German, Japanese and the rest, "På dansk: …" shows what the proposal says, word for word, so you can judge it without reading the language.
- On a translation, the featured image's alt text is stored for that language only; the image's own text, used by the other languages, stays as it is.

**What you do differently**
- Nothing new to remember: place a picture, read the proposal (and its Danish line), apply.

**Good to know**
- The Danish line is for checking the meaning; the proposal itself is written in the page's language, not translated from the Danish line.
- Tested on test copies, not on the live sites.

**Older translations**
- Not affected. Alt texts on older translations can now be improved in their own language from Translator → Alt texts on traveltalk.travel.

## 2.2.13 – 27 Oct 2026 (handed out the same day; 2.2.14 includes all of it)

**New**
- **The country name as focus keyword is back.** On destination guides (country, region and city pages), the suggested focus keyword is the place's name alone in the page's language: Austria, Österreich, Autriche. This was agreed and built on 26 Oct, but that build never reached the live sites, because another version with the same number was built alongside it. So "Set SEO" suggested "vacanze in Austria" instead (score 40 instead of about 85).
- **"Set SEO" no longer replaces your keyword.** A focus keyword already there stays first; a different suggestion is added after it.
- **Image texts per language in the Media Library** (traveltalk.travel). Below the image's own fields: "Alt text (Italiano)", "Caption (Italiano)" and so on, as pages in that language show them. You can read and correct them there.

**What you do differently**
- On a translated destination guide whose keyword went wrong: put the country name back first (or press Set SEO again; it now suggests it).
- To check an image's Italian text: Media Library → the image → "Alt text (Italiano)".

**Good to know**
- One image serves every language, so its own title, caption and file name stay in one language. Readers and Google get the language's alt text and caption on that language's pages.
- If ShortPixel's AI Image SEO writes alt texts by itself, it fills only the image's own fields, not the language fields.
- Tested on test copies of both sites, not on the live sites.

**Older translations**
- Not affected automatically: a keyword already set stays as it is. Use Set SEO, or type the country name first, on guides that need it.

## 2.2.12 – 27 Oct 2026

**New**
- **Find pictures.** A button in the Pictures box opens Translator → Find pictures for that article. For each section in a long stretch without a picture, it searches your own Media Library for the section's words (in image titles, captions, alt texts and file names; "ø" also as "oe"), leaves out pictures already in the article, and shows the best matches.
  - **Put it here** places the chosen picture under that section's first paragraph. Nothing changes before you click; the earlier text stays in Revisions.
  - Below: the media banks from Media → Image Banks (the Austrian tourist board's bank among them), to search with the same words when the Media Library has nothing. Download there, upload to the Media Library, and the next look finds it.

**What you do differently**
- When the Pictures box shows a long stretch: click **Find pictures**, pick, done.
- A picture without an alt text gets a note; Translator → Alt texts can then propose one.

**Good to know**
- The search goes by words, not by what the picture shows. "Salzburg" finds pictures named or described with Salzburg; a picture called "IMG_2231" with no text is not found.
- Downloading from the media banks stays with you, under each bank's terms.
- Tested on a test copy, not on the live sites.

**Older translations**
- Not affected. Pictures added to a Danish article reach its translations with the next re-translation.

## 2.2.11 – 27 Oct 2026 (handed out the same day; 2.2.12 includes all of it)

**New**
- **Pictures box: the sections inside a long stretch.** Under each stretch without a picture, the box now lists the sections it runs through with their words, e.g. "Wien og omegn 520 · Salzburg 610 · Hallstatt 521", so you can see where the pictures belong.

**What you do differently**
- Nothing.

**Good to know**
- Tested on a test copy, not on the live sites.

**Older translations**
- Automatic: the box applies to every post at once.

## 2.2.10 – 27 Oct 2026 (handed out the same day; 2.2.11 includes all of it)

**New**
- **The related-articles grid reaches traveltalk.travel, also for country pages like Austria.** On traveltalk.dk the grid on a country page is added by a snippet that stays quiet when the Translator asks, so 2.2.8 still found nothing. The Translator now uses the snippet's rule, read off the Austria page: the 12 newest articles in the category with the same name as the page (page "oestrig", category "oestrig").
- **No more "No posts".** Translations that still carry the old grid block show the grid there; without a grid they show nothing instead of "No posts".

**What you do differently**
- After installing, on traveltalk.dk: Translator → Catch-up → **Send the grids** once more.

**Good to know**
- The rule was checked against the Austria page (all 12 articles in the same order). If another page's grid on traveltalk.dk follows a different rule, its grid on traveltalk.travel may differ; tell me which page.
- Tested on test copies of both sites, not on the live sites.

**Older translations**
- Needs a catch-up, now complete: Send the grids (Translator → Catch-up on traveltalk.dk).

## 2.2.9 – 27 Oct 2026

**New**
- **You can see that it runs.** Every run button on the Translator pages (Alt texts, Image texts, and the three on Catch-up) now shows a spinner and "Working …" while it works, and stops when it is finished or stopped.
- **Proposals show by themselves.** Alt texts and Image texts reload the page when a run is finished, so the proposals appear without reloading by hand.
- Titles in the Alt texts log show "&" and "–" as they are, not as codes.
- The proposal field on Alt texts is wider and has two lines, so the whole proposal shows.

**What you do differently**
- Nothing.

**Good to know**
- Tested in a browser on a copy of the Alt texts page with simulated answers, not on the live sites.

**Older translations**
- Not affected.

## 2.2.8 – 27 Oct 2026 (handed out the same day; 2.2.9 includes all of it)

**New**
- **Related articles, now also where traveltalk.dk adds them separately.** On many traveltalk.dk articles (Austria among them) the related-articles grid is not saved in the article but added when the page is shown, so 2.2.7 did not find it. The Translator now looks at each Danish article as its page shows it. On traveltalk.travel, a grid that has no place in the translation's text is shown at the end of the article, where it is on traveltalk.dk.

**What you do differently**
- After installing, on traveltalk.dk: Translator → Catch-up → **Send the grids** again. The count now covers every translation; articles without a grid are named in the log.

**Good to know**
- Fixed: on traveltalk.travel the upgrade ran six times when 2.2.7 was installed (harmless, every step could be repeated). It now runs once, also with the site's cache.
- Tested on test copies of both sites, with a stand-in for the snippet that adds the grid, not on the live sites. Check the Finnish Austria page on traveltalk.travel after the catch-up: the grid should be at the bottom, with pictures.

**Older translations**
- Needs a catch-up, now complete: Translator → Catch-up → Send the grids (on traveltalk.dk).

## 2.2.7 – 27 Oct 2026

**New**
- **Related articles on traveltalk.travel.** The grid of related articles at the bottom of a traveltalk.dk article (with its pictures) now appears on its translations too. Until now it came out empty there, so those pictures were lost. Each article in the grid links to its translation in the reader's language when one is published; otherwise it links to the Danish article, with its title translated and marked "Dansk".
- **Pictures per text length** (both sites). A **Pictures** box on every post and page, and a **Pictures** column in the posts list: how many pictures the text has, one per how many words, and the stretches longer than 400 words without a picture, named by the sections they cover ("from 'Wien' to 'Salzburg': 751 words"). The limit is in Translator → Settings → "A picture at least every".

**What you do differently**
- Once, on traveltalk.dk: Translator → Catch-up → **Send the grids**, so translations made earlier get theirs. Run it again now and then: the grid on traveltalk.dk changes as articles are published.
- When writing or extending an article, look at the Pictures box: it shows where a picture would help. Adding the picture is still done by hand.

**Good to know**
- The grid on traveltalk.travel shows the articles traveltalk.dk's grid showed when it was last sent. Links switch to a new translation by themselves as soon as it is published.
- The titles of articles not yet translated are translated once and kept, so later sends cost nothing for them.
- The Pictures box says where a picture would help, not which picture to use.
- Tested on test copies of both sites with a stand-in for the Kadence grid, not on the live sites. Check one translated article on traveltalk.travel after the catch-up: the grid should look like the one on traveltalk.dk.

**Older translations**
- Needs a catch-up, now available: related-articles grids (Translator → Catch-up on traveltalk.dk → Send the grids).
- Automatic: the Pictures box and column apply to every post at once.

## 2.2.6 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- **Check Google tags, rebuilt for the two sites** (Translator → Check Google tags). It now checks from the database what each page tells Google: its language, noindex, canonical, and the language links (its own address in the set, x-default, every listed version published and long enough, the same set on every version). It shows only pages with problems; "Show all pages" lists the rest.
- Things that look odd but are on purpose are named, not counted as problems: short pages hidden from Google until filled out, and traveltalk.dk translations copied to traveltalk.travel.
- **Check live** on a row fetches that one page as a visitor sees it and compares it with what it should be.
- On traveltalk.dk: **Compare the sets with traveltalk.travel** (one call) shows any translation whose language set differs between the two sites, and **Send the set again** fixes an original whose set is out of date.

**What you do differently**
- Open Translator → Check Google tags on both sites now and then, for example after a batch is published. Problems are in red, with what to do.

**Good to know**
- Until 2.2.5 this page opened every translation and its original over the web with the rules from before the two-site setup, so most of what it reported on the bridge was not wrong. It now fetches nothing unless you press Check live on one page.
- A page in the cache shows changes when the cache renews; Check live sees the cached page, as Google does.
- Tested on test copies of both sites, not on the live sites.

**Older translations**
- Automatic: every published translation is checked, whichever version made it.

## 2.2.5 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- **Alt texts with context** (Translator → Alt texts, on both sites). For each image in a post, Claude looks at the picture and the text around it and proposes an alt text that says what the picture shows in the article's context: "Sailing boat at anchor in a bay on the Amalfi coast", not just "Italy". The featured image is included.
  - You see the alt text now and the proposal side by side, can edit the proposal, tick and apply. Nothing changes before that.
  - Give post IDs in the order you want (e.g. the strongest in Search Console), or let it take the next unchecked posts, newest first.
- **Catch-up: alt texts in articles** (traveltalk.dk, Translator → Catch-up, second section). Once you have applied new Danish alt texts, one click brings them, translated, into every translation of that post on traveltalk.travel. Only the image texts change; the article text stays as it is.

**What you do differently**
- Work through the posts under Translator → Alt texts on traveltalk.dk, the strongest first. Then run the catch-up so the translations get the same texts.
- traveltalk.travel's own English posts can be done the same way there.

**Good to know**
- Claude names a place only when the article or the old alt text names it; it does not guess places from the picture. Still read each proposal: you know the place, Claude only sees the photo.
- A featured image's alt text belongs to the image, so it changes wherever that image is used. Images in the text change in that post only.
- Earlier text is kept in each post's Revisions.
- Changing alt texts does not mark translations "Mother text changed": only the article text counts for that.
- Costs more than a text call, because Claude looks at each picture; still small on the agreed model. Up to 20 images per post.
- Tested on test copies of both sites with simulated calls, not on the live sites.

**Older translations**
- Needs a catch-up, now available: after you apply new Danish alt texts, Translator → Catch-up → "Bring alt texts over" updates the translations.

## 2.2.4 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- **Catch-up: featured-image texts** (on traveltalk.dk, Translator → Catch-up). Translations on traveltalk.travel whose featured image has no alt text in their language (mostly made before 2.2.0) get the Danish alt text and caption translated. One click runs through them all. The article text and the image stay as they are, so nothing needs review.
- **Image texts** (Translator → Image texts, on both sites). Checks that each image's alt text, caption, title and description are in the site's own language (English on traveltalk.travel, Danish on traveltalk.dk), and proposes texts where they are not, such as "Le Danemark Travel Guide …" on traveltalk.travel. You see the text now and the proposal side by side, tick, and choose "Apply the ticked" or "Keep the ticked as they are".

**What you do differently**
- Once, on traveltalk.dk: Translator → Catch-up → Translate image texts.
- On traveltalk.travel: Translator → Image texts → Check the rest, then go through "Texts to fix". New images can be checked the same way from time to time.

**Good to know**
- Nothing changes in the Media Library until you apply. The old texts are kept with each image.
- Only texts that already exist are changed; an empty text stays empty. Images without any text are not sent for checking.
- The check costs one short call per 25 images.
- A Danish image without alt text or caption is skipped in the catch-up and named in its log.
- Pages already in the cache show new texts when the cache renews.
- Tested on test copies of both sites with simulated calls, not on the live sites.

**Older translations**
- Needs a catch-up, now available: featured-image texts for translations made before 2.2.0 (Translator → Catch-up on traveltalk.dk).

## 2.2.3 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- **"Leer en" on every translation on traveltalk.travel.** Near the top of each translated article, a line in the page's own language lists the other languages it can be read in, with the original marked. On a Spanish page: "Leer en: English · Deutsch · Dansk (original)". Until now readers only had the globe button in the lower left.
- For a translation of one of traveltalk.travel's own English pages (such as Mio's Indonesia in Spanish), the English page is marked as the original.

**What you do differently**
- Nothing.

**Good to know**
- The line sits under "From the traveltalk.dk family …" on translations of traveltalk.dk articles.
- A short translation that is hidden from Google until it is filled out still shows the line, with at least the original.
- The globe button stays as it is.
- Fixed: in 2.2.0–2.2.2, the link to the Danish original in "From the traveltalk.dk family …" pointed back to the page itself. Links that name their language now always go where they say.

**Older translations**
- Automatic: every published translation shows the line from installation on. Nothing in their text changes.

## 2.2.2 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- Every translation now records the Translator version that made it. Translator → Review shows it in the column "Made with". Translations made earlier say "before 2.2.2".

**What you do differently**
- Nothing.

**Good to know**
- This is the groundwork for a catch-up screen (planned): it will list older translations that lack something newer versions add, and offer to bring them up to date.

**Older translations**
- Marked "before 2.2.2" on installation. Nothing in their text changes.

## 2.2.1 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- Release notes, built in: Translator → Release notes shows this page. After an update, editors see a one-time notice with a link to it.

**What you do differently**
- Nothing.

**Good to know**
- The notice shows once per editor; closing it or opening the page counts as seen.

**Older translations**
- Not affected.

## 2.2.0 – 27 Oct 2026 (handed out the same day; 2.2.7 includes all of it)

**New**
- **Links follow the translations.** On traveltalk.travel, a link in an article to a traveltalk.dk article now goes to that article's version in the reader's language, as soon as it is published. Until then it goes to the Danish article, as before. Nobody has to edit old articles: the links switch by themselves.
- **"Mother text changed".** When the Danish original is edited on traveltalk.dk, every translation of it on traveltalk.travel is marked. Changing only a link does not count.
  - On the translation's edit screen, the box **Danish original** shows the date and two buttons: **Re-translate** (a new version is made on traveltalk.dk and waits for you; the live page does not change until you apply it) and **Dismiss – change not relevant**.
  - The Translations list has a filter "Mother text changed".
- **Review list.** Translator → Review lists drafts waiting for review, and published translations whose Danish text has changed or that have a new version waiting.
- **Partner boxes stay Danish.** GetYourGuide, Airalo and Nordic partner boxes and links are not shown on translations. The link text stays; only the link goes. Boxes that traveltalk.travel does not have are hidden too, so readers never see raw code such as `[tt_gyg …]`.
- **Glossary.** Translator → Settings → Glossary has a box per language for fixed terms, one per line: `Danish term = term in that language`. The names traveltalk, traveltalk.dk and traveltalk.travel are always kept as they are.
- **Featured image in the reader's language.** The featured image's alt text and caption are translated with the article and shown in that language. The image itself is shared, and the Danish texts on it are not changed.

**What you do differently**
- Check Translator → Review when you start a review session.
- When a translation says "Mother text changed", open the Danish revision on traveltalk.dk, then choose Re-translate or Dismiss.
- Re-translate runs on traveltalk.dk while Translator → Queue is open there.

**Good to know**
- Only edits made to the Danish text after this update are noticed.
- Existing translations get a translated featured-image text the next time they are re-translated.
- A page saved in the cache shows its new links when the cache renews.
- Tested on test copies of both sites. The first real check is the Austria page: edit a sentence on traveltalk.dk and look for "Mother text changed" on its translations.

**Older translations**
- Automatic: links that follow translations, hidden partner boxes.
- From installation on: "Mother text changed" (earlier edits to the Danish text are not known).
- Needs a catch-up: the featured image's translated alt text and caption; old translations get them when re-translated.
- Only new translations: the glossary.

## 2.1.6 – 26 Oct 2026

- A published translation under 800 words on traveltalk.travel stays readable but is hidden from Google (noindex, out of the sitemap and language links) until it is filled out. The limit is in Settings.

## 2.1.5 – 26 Oct 2026

- Link an existing English page on traveltalk.travel to its Danish original by its address.
- Translations made on traveltalk.travel of a linked English page join the Danish article's language set.
- "Propose improvements from the Danish original" on a linked English page: the proposal waits until applied.
- Queue by ID: paste post or page IDs in Translator → Queue.

## 2.1.4 – 26 Oct 2026

- traveltalk.travel's own pages and their translations get correct language links and language menu (Mio's Indonesia report).
