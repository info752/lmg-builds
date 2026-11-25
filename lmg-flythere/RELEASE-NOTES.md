# LMG Fly There – release notes

## 1.2.0 – 4 November 2026

### New
- **"Rejs med …" / "Travel with …".** The box on country pages now has one heading, "Rejs med … til Vietnam" on traveltalk.dk and "Travel with … to Vietnam" on traveltalk.travel. Under it, partners are grouped: Flyselskaber, Tog, Færger, Bus, Krydstogt, Rejsebureauer and "Andre måder at rejse på" (car hire and the like). Only groups with a partner are shown.
- **New partner types:** Rail, Cruise line, Ferry and Coach / bus, besides Airline, Travel agency / tour operator, Other and Tourist office. Tourist offices are contacts only and never show in the box.
- **Fly There → Import list.** Upload the partner list for the site (the "Rejs med" CSV for traveltalk.dk, the "Travel with" CSV for traveltalk.travel). Each row becomes a card with type, website and a first note in the contact log: region, hub, alliance and any remark, such as "check routes before pitching".
- Translated pages on traveltalk.travel show the heading and the group names in the page's language.

### What you do differently
- On each site, go to **Fly There → Import list**, choose that site's CSV file and press Import. The page tells you how many cards were made.
- Then open the partners you want in the box, tick "Show in the box", write the countries and add the link, as before.
- The wording of the heading and every group name can be changed under **Fly There → Settings**.

### Good to know
- **An import never puts anything on the site.** Every imported card starts on ladder step 0 without "Show in the box".
- Carriers that have stopped flying are imported as Declined and never show, even if someone ticks the box.
- Only rows for the site you are on are imported, so the wrong file does no harm: it imports nothing and says so.
- You can import the same list again. Rows are matched by name, and an existing card only gets fields that are empty on it. Nothing you have written is overwritten, except that a carrier the list marks as stopped is set to Declined.
- The hub in the note is the carrier's home base, not a checked route from Copenhagen or London. Routes still have to be checked before a line goes in the box.
- The settings wording from 1.0 and 1.1 ("Flyselskaber, der flyver dig til …" and "Rejs med en specialist") is replaced by the new heading and group names. If you had changed it, set it again under Settings.
- Tested on a test site with both lists (191 and 193 rows): import, re-import, wrong-site file, stopped carriers, and the grouped box in Danish, English and German. Not tested on the live sites.

### Older content
- Cards made with 1.0 or 1.1 keep their type and everything on them. Airlines and agencies already in the box now appear under "Flyselskaber" and "Rejsebureauer" in the new box. If a card has the same name as a row in the list, the import only fills in fields that are empty on it.

## 1.1.0 – 4 November 2026

### New
- **One contact list with LeisureRelate.** When LeisureRelate CRM runs on the same site, contact details are kept in LeisureRelate only. A Fly There card linked to a lead shows the contact person, email, phone and website from LeisureRelate, with a link to edit them there.
- **Fly There → Fetch from LeisureRelate**: search LeisureRelate by name or website and filter by lead type (it opens on Travel Agency). Tick the leads you want and press "Make Fly There cards for the ticked leads". Leads that already have a card show "Open card" instead.
- On a card that is not linked yet, you can pick the existing lead, or tick **"Not in LeisureRelate yet: create it there when I save"**. The lead is then created in LeisureRelate with the name, website and contact person from the card.
- **Status follows to LeisureRelate.** When you change the status on a linked card, the lead's stage in LeisureRelate moves too: Prospect → Lead, Contacted → Contacted, Replied → Engaged, Meeting / proposal → Proposal Sent, Active → Active Partner. Paused and Declined leave the stage as it is.
- The contact log on a linked card also shows the latest 10 entries from the lead's history in LeisureRelate.

### What you do differently
- Keep contact people, emails and phone numbers in LeisureRelate. Use Fly There for the box: countries, airports, link, line, dates, ladder step and the numbers.
- To bring existing leads in, use **Fly There → Fetch from LeisureRelate**, then open each new card and set the type, countries and link.
- New airline or agency that is not in LeisureRelate yet: add it in Fly There and tick "create it there when I save", or add it in LeisureRelate first and fetch it.

### Good to know
- LeisureRelate has no "airline" lead type. Airlines created from Fly There get the type Advertiser in LeisureRelate. Cards fetched from LeisureRelate get the type Travel agency (from Travel Agency), Tourist office (from Destination / Tourism Board) or Other; set Airline by hand on the card.
- Changing a stage in LeisureRelate does not change the status in Fly There. Change the status in Fly There and LeisureRelate follows.
- This only works when LeisureRelate is installed on the same WordPress site as Fly There. On a site without it, cards keep their own contact fields as in 1.0.0.
- Tested on a test site with a copy of the LeisureRelate tables from the repository version. The LeisureRelate on the live site may be newer than the repository; if the fetch page or the contact details look empty, tell Claude.

### Older content
- Cards made with 1.0.0 that were already linked to a lead now show the contact details from LeisureRelate; the details typed into the card are kept but no longer shown. Check that the lead in LeisureRelate has the contact person.
- Cards that are not linked are not affected.

## 1.0.0 – 4 November 2026

### New
- A new menu in wp-admin, **Fly There**, for airline and travel agency partners on country pages.
- **Partners** is the contact tool. Each airline, travel agency or tourist office gets a card with the contact person, email, phone, website, the ladder step (0 Listed, 1 Media contact, 2 Founding partner, 3 Campaign, 4 Annual), a status (Prospect, Contacted, Replied, Meeting, Active, Paused, Declined), the next step with a date, and the agreed price.
- Each card has a **contact log**. Write a note and press Update, and it is saved with the date and your name. Status changes are logged by themselves.
- If LeisureRelate CRM runs on the same site, a card can be linked to a LeisureRelate lead. Notes and status changes are then also written to the lead's history.
- **The box.** On country pages, under "Sådan kommer du til [land]", partners now show in two groups: airlines ("Flyselskaber, der flyver dig til Vietnam") and travel agencies ("Rejs med en specialist"). Paid partners (ladder step 2 and up) come first, with their logo and the label "Partner". Free partners show as a plain line.
- **Counting.** A view is counted when a reader has the box on screen for one second. A click is counted when a reader follows a partner's link. Search engines, bots and logged-in staff are not counted. No cookies are used, so no consent banner is needed.
- Partner links get tracking tags, so the partner sees our visits in their own statistics as "flythere".
- **Fly There → Report** shows the pipeline (how many partners at each status and ladder step), the next steps due within 7 days, and the month's views, clicks and click rate per partner, per country and per language. A CSV download is there too.
- **Partner report**: one page per partner and month that you can print or save as PDF and send to the partner.
- **Fly There → Settings**: departure airports for the site (traveltalk.dk starts with CPH, OSL, ARN, HEL; traveltalk.travel with LHR, CDG, FRA, AMS, MAD, FCO, MUC, ZRH) and the wording in the box.

### What you do differently
- Add a partner under **Fly There → Partners → Add partner**. Fill in the contact part first. The box part can wait until they are listed or have paid.
- To show a partner in the box, tick **Show in the box**, write the countries (the country category slugs, for example "vietnam, japan"), tick the departure airports, add the link and one short line.
- Set the **To** date when a paid period ends. The line goes away by itself after that date.
- At the start of each month, open **Fly There → Report**, pick last month, and send each paying partner their partner report.
- Use the next step date on each card. Overdue steps show in red in the partner list and on the Report page.

### Good to know
- The box appears where LMG Faktabokse places it, under "Sådan kommer du til [land]". Until that plugin is installed, put the shortcode `[lmg_flythere country="vietnam"]` on a country page by hand.
- On translated pages on traveltalk.travel, the headings and buttons are shown in the page's language (English, German, French, Spanish, Italian, Portuguese, Swedish, Norwegian and Finnish). The partner's own line is shown as written, in one language.
- Departure airports: if LMG Faktabokse is active, its airport list is used, so you only keep it in one place.
- Tested on a test site with WordPress 6.8 and PHP 8.3: the box, the hidden partners (paused, expired, wrong airport), view and click counting, bot filtering, the redirect, the admin pages, the log and the LeisureRelate link. Not tested on traveltalk.dk or .travel, with LiteSpeed cache, or together with LMG Faktabokse and LMG Translator.
- Watch the first days: if the Report page shows no views at all while the box is visible, the cache or a security plugin may be blocking the counting address. Tell Claude.

### Older content
- Not affected. Nothing changes on existing pages until you add a partner and tick "Show in the box". Counting starts from installation; there are no older numbers.
