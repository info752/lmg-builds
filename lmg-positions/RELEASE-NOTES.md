# LMG Positions – release notes

For editors and reviewers on traveltalk.dk and traveltalk.travel. Newest first. The page itself is in Danish.

## 0.4.0 – 1 Nov 2026

**New**
- **"AI-synlighed (ChatGPT og Perplexity)" at the bottom of Positioner (LeisureIntel → Positioner).** It asks ChatGPT and Perplexity, with their web search on, 12 travel questions in Danish (8 in English on traveltalk.travel) and shows, per answer, whether our pages are linked, whether "Traveltalk" is named, and which other sites they looked at. A line on top counts how many answers named or linked us.
- **Every call costs money at DataForSEO, so it is under your control.** The price of each answer is read from DataForSEO's own reply and added up; the page shows this month's total against a monthly limit (to begin with $2.00). A run stops by itself when the limit is reached.
- **The questions are yours to edit** (Spørgsmål, loft og modeller): one per line, up to 40. The first 12 were chosen from traveltalk.dk's Search Console topics of 28 Oct (ski in Norway and Austria, train journeys, Maldives, Filipino food, taverna, Danang, small Asian countries, Hemingway, art trips, travel agencies, inspiration).

**What you do differently**
- Enter the DataForSEO login first (1. Forbindelser → DataForSEO-login; the API login and API password from DataForSEO → API Access, not the website password).
- Press **Pilot: 3 spørgsmål, kun ChatGPT** first. It makes 3 calls. Look at the price per answer in the table. If it is acceptable, press **Kør alle spørgsmål** (12 questions × 2 engines = 24 calls on traveltalk.dk). Keep the page open while it runs; each call takes some seconds.
- Send a screenshot of the pilot, also if a row shows "fejl": the message says what DataForSEO answered.

**Good to know**
- Not verified against DataForSEO's live documentation, which could not be reached while building: the calls follow the LLM Responses API as known, and the answer is read in a way that tolerates different layouts. If the pilot shows errors or empty "sider de kigger på", that is the first place to look; nothing is spent on a call that is refused.
- "Os?" means: a link to traveltalk.dk or traveltalk.travel in the sources (yes, link), or the word Traveltalk in the answer text (nævnt). Because AI answers vary from one asking to the next, one run is a sample, not a measure; compare runs month by month.
- The model is chosen automatically from DataForSEO's list (a small, cheap one). You can set a model by name under Spørgsmål, loft og modeller.
- Only the last six runs are kept.
- Tested with sample answers on a stand-in database. Not tested on the live sites and never against DataForSEO.

**Older content**
- Not affected. The earlier baseline runs and the Overblik are unchanged. This version is built on 0.2.1; the Search Console direct-from-Google changes of 0.3.0 (parked) are not in it.

## 0.2.1 – 31 Oct 2026

**New**
- **Visits from Google Analytics on both sites, without a credentials file.** The line "Besøg (GA4)" in the Overblik now reads the copy that Rank Math keeps of your Google Analytics data, when LeisureIntel's own GA4 connection is not set up (it is not, on either site). It shows page views, visitors and (where Rank Math has them) sessions for the last 28 days against the 28 before, for the whole site.
- **A "Datakilder" panel under the Overblik.** It lists the data tables Rank Math keeps (Search Console, Analytics and others), with how many rows, the first and the last day they cover, and their columns. Its heading says how old the newest Search Console day is, and warns in orange when it is older than four days.

**What you do differently**
- Open LeisureIntel → Positioner. Nothing needs to be set up. If the GA4 line says Rank Math has no Analytics data or unknown columns, send a screenshot of the Datakilder panel.
- Use the Datakilder panel to judge how current the numbers are before acting on a verdict.

**Good to know**
- The figures are Rank Math's copy of Google's data, not Google directly. Rank Math fetches new data in batches every few days, so the newest two to three days are always missing.
- "Visitors" is added up per page and per day, so one person who reads several pages is counted more than once. Treat it as a trend, not as a count of people.
- Built from Rank Math's table names as they are normally laid out; where a table looks different on your sites, the page says which columns it found instead of showing wrong numbers.
- Tested with sample data on a stand-in database. Not tested on the live sites.

**Older content**
- Not affected. Earlier baseline runs stay as they are.

## 0.2.0 – 31 Oct 2026

**New**
- **An overview at the top of Positioner (LeisureIntel → Positioner), one line per language.** It shows how many search words we hold in gold (positions 1–10, with how many are in the top 5), silver (11–20), bronze (21–30) and the rest (31 and below), how clicks and visits changed over the last 28 days against the 28 days before, and how many translations are published in that language.
- **A verdict per language:** Dive (clicks or visits falling), Defend (gold words losing places or clicks), Attack (silver and bronze words with many views, the cheapest places to win), Climb (clicks growing). Several can apply at once; the most urgent is shown first. Under each language, a list shows the actual words and pages: what to defend, what to attack, and what has climbed at least three places.
- **GA4 visits for the whole site,** shown when LeisureIntel has its Google Analytics connection set up on that site.
- **The old baseline table now uses the same metals** (gold, with top 5 inside it, silver, bronze, other) instead of the older bands. The overview shows small plus and minus numbers against the latest baseline.
- **A "Release notes" section** at the bottom of the Positioner page, and a one-time "updated" notice in wp-admin.

**What you do differently**
- Open LeisureIntel → Positioner and start with the overview. Nothing needs to be run first: it reads what Rank Math already has from Google Search Console.
- "Opdatér nu" refreshes the overview. Otherwise it is refreshed on its own every six hours.

**Good to know**
- Search Console gives one average position across countries, so English counts the same for the UK and the US here. The per-country positions are still in the table further down.
- Rank Math's data runs two to three days behind. The overview says exactly which days it covers.
- Words with fewer than 5 views in the 28 days are not counted. Words seen too few times would otherwise swing the numbers.
- GA4 on traveltalk.travel is only shown if it has been set up there; the page says "not connected" otherwise. The figure is for the whole site, not per language.
- The count of translations looks at the Translator's published translations on that site. Translations already moved from traveltalk.dk to traveltalk.travel are not counted on traveltalk.dk.
- Tested with sample Search Console data on a stand-in database, not on the live sites. Not tested with real GA4.

**Older content**
- Not affected. Baseline runs taken with 0.1.0 stay as they are and are shown with the new metals. No catch-up is needed.

## 0.1.0 – 28 Oct 2026

First version: a baseline of our Google positions per language from Rank Math's Search Console data, who holds the places above us, who advertises on our search words, and a suggested action per word.
