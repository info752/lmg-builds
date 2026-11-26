# LMG Faktabokse – release notes

## 1.3.0 – 26 November 2026

### New

- **Fact boxes for wine and sport.** Faktabokse now also fits winetalk.dk and worldsporttalk.com. Each site gets its own facts:
  - **winetalk:** "Fakta om Bordeaux" with Grapes, Wine styles, Classification, Vineyard area, Good recent vintages and Best time to visit.
  - **worldsporttalk:** "Facts about the Tour de France" with Sport, When, Venue / host cities, Format, Record / most titles, How to watch and Tickets.
  - Under these, "More facts" still lets you add your own lines, for example famous producers or prize money.
- On posts in the same category, the "Want to know more about …?" box links to the region or event page, as it does to country pages on the travel sites.
- On wine and sport sites, the travel parts are switched off: no "How to get there" routes, no Travel Services section, no travel providers and no partner boxes.
- **Settings → LMG Faktabokse → Settings → Kind of site** shows which kind the site is (Travel, Wine or Sport). It is set automatically from the site address, so normally you leave it alone.

### What you do differently

- **traveltalk.dk, traveltalk.travel, think-smarter.net:** press **Update all now** in the yellow LMG notice. Nothing changes for readers or editors.
- **winetalk.dk and worldsporttalk.com (first time):** go to Plugins → Add New Plugin → Upload Plugin, choose the zip, then Install Now and Activate. After this, LMG Updater keeps it up to date.
- To make a region or event page: open the page, scroll to the **Faktabokse** panel below the editor, choose its category (for example Bordeaux or Tour de France), fill in the facts you know for certain and set "Facts last checked". Every post in that category then gets the "Want to know more" box linking to the page.
- Check every fact against a reliable source before you publish. Never take figures from memory or AI.

### Good to know

- Empty fields are left out of the box, so a page with three facts shows only those three.
- Nothing shows on winetalk or worldsporttalk until a page has a category chosen in the Faktabokse panel.
- The labels come in all ten LMG Translator languages, so translated pages get translated labels.
- Tested on a test WordPress set up as a travel, a wine and a sport site, in Danish and English. The boxes, the editor panel and the settings page worked, and the travel parts stayed off on wine and sport. Not tested on the live sites.

### Older content

- Not affected. Country pages, routes, travel services and providers on the travel sites are unchanged. On winetalk and worldsporttalk there is no older content, because the plugin is new there.

## 1.2.0 – 23 November 2026

### New

- **Providers tagged by where they travel.** When you edit a travel agency, airline or other provider, a new panel on the right, **Rejser til / fra** (on traveltalk.travel: **Travels to / from**), lets you tick the countries and regions it travels to and type the airports it departs from. Countries named in the provider's own text are shown in bold, with a link to tick them all at once.
- **"Rejs til Italien med" box.** Country pages, country category pages and every post about a destination can show the providers that travel there, at the end of the text. Put [lmg_udbydere] in a post to place it somewhere else.
- **Relevance comes first, payment second.** A provider that names the country itself always ranks above one that only covers the region (for example "Asia"). Only among equally relevant providers do partners go first. The order of the rest rotates daily, so the same agency is not always on top.
- **Partner levels.** Under **Partner level** an administrator can choose Partner, Premium partner (the box then shows at most 3) or Exclusive (shown alone), with an end date. Partners carry the label "Annonce" ("Sponsored" on .travel) and can have a link to their own site. A partner who is less relevant than others is not lifted above them, and an exclusive partner only gets the box to itself where it is also the most relevant.
- **Filter on the Rejsebureauer page.** The Rejseservice category pages get a drop-down "Rejser til", so readers can pick a country and see only the agencies that go there (or to its region).
- **Clicks per provider and destination.** Settings → LMG Faktabokse → **Providers by destination** shows clicks this month and last month for each provider, both to its profile on our site and to its own site. A CSV with 13 months, per provider and destination, is there for partner reports.
- **Tag the untagged in one go.** The same tab lists the providers without destinations, with the countries found in their text ticked. Untick what is wrong and save.
- **Old traveltalk.travel pages can come back.** Posts → Travel Services, section "Restore old pages", lists 60 airline, airport and hotel pages saved by the Internet Archive, plus new hub pages for /airlines/, /airports/ and /hotels/. Ticked pages come back as drafts at their old address, text only.

### What you do differently

- Install 1.2.0 on both sites. Nothing readers see changes until you switch the box on.
- Open **Settings → LMG Faktabokse → Providers by destination**, section 3, and save the destinations for the agencies (check a handful first). Then set the box to **Pilot** with two or three country pages, look at them, and switch it **On** when you are happy.
- Partner levels and partner links can only be set by an administrator. Set an end date for every paid placement; when it passes, the provider is shown as a normal one again.
- On traveltalk.travel: open **Posts → Travel Services**, look at "Restore old pages", and press **Restore the ticked pages as drafts**. It does 12 pages per press; press again until all are done. Then read each draft, add images from the media library and publish what you want.

### Good to know

- If no provider travels to a country or its region, no box is shown. An empty box never appears.
- The drop-down on the Rejsebureauer page appears as soon as some agencies have destinations, also while the box is off. Filtered pages are kept out of Google's index, so they do not compete with the main page.
- The box only shows on posts and pages in the site's own language for now, not on .travel translations.
- Click counts are rough: search robots and logged-in editors are left out, but a determined visitor could still add clicks. Use them as a guide, not as an invoice.
- Restored pages: Aeroflot (banned from EU airspace), Alitalia (stopped flying in 2021) and a duplicate EgyptAir page are not ticked. Jet Time, ITA, TAP and the long Copenhagen Airport and New York hotel pages have a note to check facts. The old pages are short (50–350 words) and from 2023–2024, so check every fact before publishing; they are a good base to deepen with the .dk airline pages through LMG Translator.
- A page that already exists at the old address is never touched. If the Internet Archive does not answer, the page is skipped and the message says so; try again later.
- Not tested on a live WordPress site. The ranking was tested on its own with made-up providers; the restore was tested on a sample page, not against the Internet Archive from your server.

### Older content

- Applies from installation on, but only once you act: existing posts and pages get no destinations until you tag them, and no box shows until you switch it on. Nothing in any post's text is changed; the box is added when the page is shown.
- Categories, addresses and the Rejsepraktisk box from 1.1.3 are not affected.

## 1.1.3 – 23 November 2026

### New

- **Your existing categories move under Rejseservice (traveltalk.dk).** One press of **Make the top-level category and subcategories** builds this tree:
  - Rejseservice
    - Flyselskaber (existing, 6 posts)
    - Lufthavne (existing, 5 posts)
    - Krydstogter & rederier (new)
    - Tog & jernbaner (new)
    - Bus & fjernbus (new)
    - Biludlejning & transport (new)
    - Hoteller (existing, 4 posts)
    - Rejsebureauer (existing, 81 posts)
    - Rejsepraktisk (new), with Rejseforsikring, Rejseøkonomi and Rejseudstyr (existing) under it
- **Every post keeps its address.** /rejsebureauer/tui/ stays /rejsebureauer/tui/, even though Rejsebureauer now sits under Rejseservice. Before and after each move the plugin compares the address of every published post in that category. If a single one would change, that move is undone and the tab says which category was left where it was.
- **Category pages move with the tree.** The Rejsebureauer category page now lives under Rejseservice. Its old address sends readers on to the new one.

### What you do differently

- Install 1.1.3, open **Posts → Rejseservice** and press **Make the top-level category and subcategories**. The table shows each category as "in place", "existing category, will be moved in" or "new, will be made" before you press.

### Good to know

- Krydstogt, Togrejser, Bilferie, Busrejser, Ferieboliger and Glamping stay under Rejseinteresser, as the brief says. Their posts are filed in the Rejseservice subcategories as well, with the lines from the inventory.
- Existing names are kept (for example "Hoteller" rather than "Overnatning"). Rename a category under Posts → Categories if you want; that does not change any address.
- traveltalk.travel has no service categories left from earlier, so all nine are new there.
- Not tested on a live WordPress site. Check two or three post addresses in Rejsebureauer right after pressing the button.

### Older content

- Applies when you press the button. Categories that 1.1.0 or 1.1.1 had already moved keep their posts' old addresses automatically from installation on.

## 1.1.2 – 23 November 2026

### New

- **No post changes address.** On traveltalk.dk a post's address includes its category (for example /flyselskaber/…). Moving the existing Flyselskaber and Lufthavne categories under Rejseservice would have changed the address of every post in them. They now stay where they are, keep their addresses, and are still shown as subcategories of Rejseservice in the menu and on the Rejseservice page. The tab marks them "kept at its own address".
- **Repair.** If you already pressed **Make the top-level category and subcategories** with 1.1.0 or 1.1.1 on traveltalk.dk, press it again after installing 1.1.2. It puts Flyselskaber and Lufthavne back at the top level, so their posts get their old addresses back.

### What you do differently

- Nothing new. Install 1.1.2 over 1.1.1 and press the button once.

### Good to know

- traveltalk.travel is not affected: its post addresses do not include the category.
- Not tested on a live WordPress site.

### Older content

- Applies when you press the button: categories moved by 1.1.0 or 1.1.1 on traveltalk.dk are put back at the top level. Nothing else changes.

## 1.1.1 – 23 November 2026

### New

- **Clearer: Rejseservice is a category.** Rejseservice (traveltalk.dk) and Travel Services (traveltalk.travel) are top-level categories, and the nine services are their subcategories. The tab is now called **Travel Services categories** and says so at the top. It can also be opened from **Posts → Rejseservice** (Posts → Travel Services on traveltalk.travel).
- **Main menu in one click.** Step 6 on the tab adds the top-level category to the main menu, with the nine subcategories under it.
- **The optional links from destination posts have their own step (5).** They stay off unless you switch them on, and they are separate from the categories.

### What you do differently

- Open **Posts → Rejseservice**, press **Make the top-level category and subcategories**, then **Add to the main menu** when you want readers to see it.

### Good to know

- The menu button uses the theme's main menu. Readers see the new menu item at once. Move or remove it under Appearance → Menus.
- Not tested on a live WordPress site, same as 1.1.0.

### Older content

- Not affected. Categories, posts and settings made with 1.1.0 stay as they are.

## 1.1.0 – 23 November 2026

### New

- **The Rejseservice / Travel Services section.** A new tab, Settings → LMG Faktabokse → **Rejseservice**, sets up "the practical side of travelling" on each site: one parent category and nine children, with the names and descriptions from the brief. On traveltalk.dk: Rejseservice, with Flyselskaber & fly, Lufthavne, Krydstogter & rederier, Tog & jernbaner, Bus & fjernbus, Biludlejning & transport, Overnatning, Rejsearrangører & rejsebureauer and Rejsepraktisk. On traveltalk.travel: Travel Services, with Airlines & Flights, Airports, Cruises & Cruise Lines, Trains & Railways, Buses & Coaches, Car Rental & Mobility, Accommodation, Tour Operators & Travel Agencies and Travel Essentials.
- **Existing categories are taken in, not doubled.** On traveltalk.dk the existing "Flyselskaber" category becomes the first child, with its posts. If its category page gets a new address, the old address sends readers on to the new one.
- **Inventory, look-up only.** The tab counts posts and pages in every status (published, drafts, private and trash) whose title fits each child, and gives a CSV to download, with a ready line per post for the next step.
- **Add posts to a child in one go.** Paste lines such as "48211 | 2" (post and child number), check the preview, then add. The child is added as an extra category: the primary category and the post's address never change. A post whose address would change is put back as it was and listed. Every run is saved and can be undone.
- **Hero image and related pages per child.** Choose each hero from the site's own media library. Link existing pages to a child, for example /rejsebureauer/ and /rejseforsikring/ on traveltalk.dk or the airline and airport pages on traveltalk.travel; their sub-pages are listed on the child's category page.
- **Landing page with nine cards.** One button makes a draft page at /rejseservice/ (or uses the existing /travel-services/ on traveltalk.travel without changing it). The cards come from [lmg_rejseservice]: the line "Den praktiske side af rejsen", then a card per child with hero, name and description.
- **The "Rejsepraktisk" / "Practical travel" box.** On destination and travel-interest posts, after the first paragraph under the second heading: up to four posts that sit both in a Rejseservice child and in the post's own destination category. If there are none, posts from the child that fits the post's travel interest (cruise posts get cruise lines). Otherwise no box. It is added when the page is shown and never written into the post.

### What you do differently

- **Setting up a site:** Settings → LMG Faktabokse → Rejseservice → **Make the categories**. This changes no post.
- **Choosing posts:** download the inventory, mark what belongs where, and paste the approved lines into step 3. Press **Show what will happen**, then **Add the categories**.
- **Pilot:** set the info box to **Pilot** and enter the IDs of three destination posts. Tick **Show hero, cards and related pages** only when the pilot is approved. Publish the landing page yourself when you are happy with it.
- **Menu:** add Rejseservice / Travel Services under Appearance → Menus once the pilot is approved.
- **To hide the box on one post:** tick **Hide the "Rejsepraktisk" box** in the post's Faktabokse panel below the editor.

### Good to know

- Nothing visible changes on installation. The box starts **Off**, the category pages show nothing extra until you tick the box, and the landing page is a draft.
- The inventory matches on titles only. It is a starting list for your approval, not a decision. Posts that exist only in old backups are not in it.
- Restoring removed content (from trash or backups) is not part of this version. Restore approved posts the usual way, then add them in step 3.
- Pages have no categories in WordPress, so the airline and airport pages are linked as related pages, not added as posts.
- The box shows only on posts in the site's own language. Translations on traveltalk.travel get no box for now.
- Not tested on a live WordPress site. It was checked for errors and the box placement was tested, but WordPress itself could not be run from the build session. Test on traveltalk.dk first.

### Older content

- Not affected until you act: country pages, fact boxes and the "Vil du vide mere" box work as in 1.0.0. Posts get the Rejseservice categories only through step 3, and the box only once you switch it to Pilot or On.

## 1.0.0 – 4 November 2026

### New

- **Fact boxes on country pages.** A country page can show two boxes: "Fakta om Vietnam" (capital, language, currency, time difference, visa and entry, best time to go, plugs, health, plus any extra lines you add) and "Sådan kommer du til Vietnam" (one row per way to get there: from which airport, with which airline or other transport, direct or with stops, via where, and roughly how many hours).
- **"Vil du vide mere om Vietnam?" on every post in the country's category.** At the end of each post: "Gå til siden Rejser til Vietnam. Her finder du også faktabokse om de fleste relevante rejsefakta, inklusive sådan kommer du til Vietnam." Sub-categories count too, so a post filed under Hanoi links to the Vietnam page.
- **Ten languages.** All headings and labels are ready in Danish, English, German, French, Spanish, Italian, Swedish, Norwegian, Portuguese and Finnish. A translation made with LMG Translator shows the boxes in its own language automatically.
- **Departure airports per site.** traveltalk.dk starts with Copenhagen, Billund, Aalborg, Oslo, Stockholm and Helsinki. traveltalk.travel starts with Heathrow, Charles de Gaulle, Frankfurt, Schiphol, Madrid, Fiumicino, Munich, Zurich and Copenhagen. Both lists can be changed.
- **An overview** of all country pages, with how many facts and routes each has and when the routes were last checked.

### What you do differently

- **To make a page a country page:** open the page, scroll to the **Faktabokse** panel below the editor, choose the country's category under **Country category**, fill in the facts and routes, set the two "last checked" dates, and update the page.
- **Routes come from the airline's own route map or timetable,** never from memory or from AI. Set **Routes last checked** to the day you checked. Readers see that date with "always check with the carrier".
- **To hide the "Vil du vide mere" box on one post:** tick **Hide the "Vil du vide mere om …?" box** in the post's Faktabokse panel.
- **On a translation of a country page** the Faktabokse panel asks only for the wording in that language (country name, fact texts, notes). Leave a field empty to show the original's text.
- **Settings and overview:** Settings → LMG Faktabokse. There you choose the departure airports, whether the boxes go after the text (standard), before it, or only where you write [lmg_faktabokse], and whether posts show the "Vil du vide mere" box.

### Good to know

- Nothing shows until a country page has its category chosen. Installing the plugin changes no page by itself.
- The route box only shows when it has at least one row. The fact box only shows when at least one fact is filled in.
- A post shows the "Vil du vide mere" box only when the country page is published. On translations it shows only when the country page has a published translation in the same language, so a German reader is never sent to a Danish page.
- If two pages have the same country category, posts link to the published one, and the overview shows a warning.
- Fact texts, extra lines and notes are written in the site's language. On a translation they show in the original language until someone fills in the translation's own wording. Airport names come from the departure list and are the same in every language.
- If you move route rows around on the original, a translated note can end up on the wrong row. Check translated notes after reordering.
- traveltalk.dk and traveltalk.travel are separate sites. Country pages on .travel need their own facts and routes, from .travel's own departure airports.
- Partner lines, the "Rejs med en specialist" line, view and click counting and partner reports come from the companion plugin LMG Fly There. It places itself right after the "Sådan kommer du til" box. LMG Faktabokse works on its own without it.
- Tested on a test WordPress site with Danish and English and German translations. The plugin was not tested on traveltalk.dk or traveltalk.travel, or with the live LMG Translator, Rank Math or the site's theme. Saving in the panel was tested on the server side, and the panel's buttons were tested in a browser. A full save from the block editor was not tested.

### Older content

- **Not affected.** No existing page or post changes until a country page has its category chosen. From then on, published posts in that category show the "Vil du vide mere" box automatically, older posts included. No catch-up is needed.
