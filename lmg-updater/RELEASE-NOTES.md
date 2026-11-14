# LMG Updater – release notes

For G and the editors. Newest first.

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
