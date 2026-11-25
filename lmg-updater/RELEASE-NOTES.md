# LMG Updater – release notes

For G and the editors. Newest first.

## 1.2.0 – 25 Nov 2026

### New
- **The list now covers all our plugins, not four.** Tools → LMG Updates has two tables: plugins that are **updated through the list**, and plugins that are **watched only** (the list knows which version should run, but holds no build yet). A watched plugin is never offered as an update; it only shows where it runs and in which version.
- **"🔼 newer than the list".** When a site runs a newer version than the list says, the cell turns orange. That is what happened with LMG Translator (the list said 2.17.19 while every site ran 2.21.1): the list was behind, not the sites.
- **Single-file plugins can be updated too.** These are plugins that are one file, not a folder. WordPress's own update would move them into a new folder and switch them off, so "Update all now" installs them itself. It keeps a copy of the old file first. Tools → LMG Updates → "Copies kept from single-file updates" has a **Put this version back** button for each one.
- **A build always lands in the plugin's own folder.** If a build's folder is named differently from the folder the plugin is installed in, it is unpacked into the installed folder, so the plugin stays switched on.
- **"Our plugins on this site".** At the bottom of Tools → LMG Updates: every Leisure Media Group plugin on this site, its version, whether it is in the list, and **Download a copy**. The copy is the plugin exactly as it is installed, as a zip. Send it to Claude when a plugin with no reliable copy (LeisureIntel, LeisureRelate, Brevo Bridge) is to get its next version.
- **"Update all now" in the yellow notice** now handles both kinds: single-file plugins first, then WordPress's usual update screen for the rest.

### What you do differently
1. On each site with the Updater (traveltalk.dk, traveltalk.travel, winetalk.dk, worldsporttalk.com): press **Update all now** in the yellow notice, or Dashboard → Updates → LMG Updater → Update.
2. On think-smarter.net, which has no Updater yet: Plugins → Add New → Upload Plugin → choose the zip → Install → Activate. From then on it updates like the others.
3. Look at Tools → LMG Updates once all sites run 1.2.0. Orange 🔼 cells mean the list is behind; tell Claude.

### Good to know
- **Nothing installs by itself.** As before, a person presses the button.
- Until a site runs 1.2.0, the table shows "? older Updater there" for the new rows of that site, and "Issues" says which sites still run an older Updater.
- A plugin in the list that is not on a site shows "not here". The Updater never installs a plugin that is not already there.
- The public status address still shows only the plugins in the list and their versions; nothing else.
- "Download a copy" is for administrators only and gives only our own plugins.
- **Tested:** on a test WordPress 6.9 site: a folder plugin updated through Dashboard → Updates; a single-file plugin updated through "Update all now", the old file kept and put back with the button; a build with a differently named folder landed in the installed folder and stayed active; a wrong fingerprint was refused; "newer than the list" and "watched only" showed as described; Download a copy gave a working zip. **Not tested on the live sites**, and not behind Hostinger's LiteSpeed server.

### Older content
- **Not affected.** Plugins already installed keep running; the Updater only offers newer versions from the list.

## 1.1.2 – 14 Nov 2026

### New
- **Tools → LMG Updates links to every site.** Each site's name at the top of the table opens that site's Dashboard → Updates in a new tab, and every "⏳ update waiting" does the same. Includes 1.1.1.

### What you do differently
- From the table on any one site, click the site name to go and update it.

### Good to know
- Tested: the code loads without errors. **Not tested on the live sites.**

### Older content
- **Not affected.**

## 1.1.1 – 14 Nov 2026

### New
- **New versions show at once.** GitHub's public file address kept serving the old list for more than 20 minutes after a new version was put in, so "Update all now" installed the previous version (2.17.8 instead of 2.17.9). The Updater now reads the list through GitHub's own interface, which answers within a minute; if that is busy it falls back to the old address.

### What you do differently
- Nothing.

### Good to know
- Tested: the new address returned the current list (2.17.9) while the old one still returned 2.17.8. The code loads without errors. **Not tested on the live sites.**

### Older content
- **Not affected.**

## 1.1.0 – 14 Nov 2026

### New
- **A notice at the top of every wp-admin page** when an update is waiting on that site: "LMG: 2 update(s) waiting – LMG Translator 2.17.6 → 2.17.7 · LMG Leisure Family 1.1 → 1.3" with one button, **Update all now**. No searching under Dashboard → Updates (G, 14 Nov: "I still need to know here").
- **The site notices a new list within 10 minutes** and tells WordPress at once, so the update shows straight away instead of after up to half a day. This is why LMG Leisure Family 1.3 did not show on worldsporttalk.com: the site still had the list from before WST was added.
- **"Read the list again"** also reads every site's status afresh, so old "no answer" lines disappear.

### What you do differently
- When Claude says something is in the list: open wp-admin on each site, press **Update all now** in the yellow notice. That is all.

### Good to know
- Tested on a test WordPress 6.5 in a real browser: the notice showed "LMG: 1 update(s) waiting", Update all now updated the plugin and it stayed active. **Not tested on the live sites.**

### Older content
- **Not affected.**

## 1.0.1 – 14 Nov 2026

### New
- The status address each site gives (which versions it runs) is never cached any more. On traveltalk.dk the page cache kept an old, empty answer, so the status read from outside showed nothing.

### What you do differently
- Nothing new: Dashboard → Updates → LMG Updater → Update, on each site.

### Good to know
- Tested: the code loads without errors. **Not tested on the live sites.**

### Older content
- **Not affected.**

## 1.0.0 – 14 Nov 2026

### New
- **Updates for our own plugins from one list.** Claude keeps one list of which version of each Leisure Media Group plugin should run on which site. When a new version is in the list, it shows under **Dashboard → Updates** on each site it is meant for, like any other WordPress update, with its release notes under "View version details". You press **Update**; no zip, no upload.
- **Nothing installs by itself.** A person presses Update on each site (house rule: no unattended changes to a live site).
- **Safe downloads.** Every version in the list carries a fingerprint. If a download does not match it, the update is refused and the problem is reported.
- **Tools → LMG Updates**: one table, plugin by plugin and site by site – ✅ runs the version in the list · ⏳ update waiting · ⚠️ not installed, inactive or no answer – plus a list of problems. Claude can read the same status, so you do not have to report back after an update.

### What you do differently
1. Install LMG Updater once on each site (traveltalk.dk, traveltalk.travel, winetalk.dk, worldsporttalk.com): Plugins → Add New → Upload → Activate. This is the last plugin you upload by hand.
2. When Claude says a new version is in the list: on each site, Dashboard → Updates (or Tools → LMG Updates → "Read the list again" if it does not show yet) → tick → Update.
3. Tools → LMG Updates shows where it is done.

### Good to know
- The list lives in the public repository info752/lmg-builds, which holds only finished plugin builds (no content, no briefs, no keys).
- Each site shows only the plugins and versions in the list at its own public address /wp-json/lmg-updater/v1/status – no other data.
- Single-file plugins (LeisureSocial) are not handled yet; they keep the manual upload.
- WordPress looks for updates about twice a day; "Read the list again" makes it look at once.
- Tested on a test WordPress 6.5: a new version was offered, installed through the Dashboard update route and stayed active; a download with the wrong fingerprint was refused and reported; the status address and the Tools page work. **Not tested on the live sites.**

### Older content
- **Not affected.** Plugins already installed keep running; the Updater only offers newer versions from the list.
