# LMG Link Repair – release notes

For G and the editors. Newest first.

## 1.1.0 – 27 Nov 2026

### New
- **Orphan posts are linked in one click.** Tools → Link repair → 3. Orphan posts: tick posts and press "Link ticked posts", or press "Link all". Each post is added to a short list at the end of its hub's text, under a heading in the site's language (Læs også, Read more and so on). The list is created once per hub and extended later. Nothing is removed.
- **"Check first" column.** Rows that shouldn't be linked automatically are marked in red and have no tick box: a post with the same name as its hub (such as Vinsnak and /vinsnak/, a possible duplicate), a hub that is only a category archive with no page text, or a hub that isn't published. You decide on those.
- **Undo hub links** puts every hub back exactly as it was.
- The CSV now has a "check_first" column.

### What you do differently
- Dashboard → Updates → LMG Link Repair → Update. Then 3. Orphan posts → Link all.

### Good to know
- Linked posts disappear from the list straight away. Rank Math's own count updates the next time the hub is saved in the editor.
- Translations of the hub don't get the list. It sits in the original only.
- Tested outside WordPress (syntax and the list-building logic). Not yet tested inside WordPress itself.

## 1.0.2 – 27 Nov 2026

### Safer
- **Old language addresses can never hit a live translation.** Three guards now apply before any 410: the address must already be a 404; its language must not be in the keep list (now also ja, zh, ko) or be any language Translator has used on this site; and its last part must not match a published post, page or translation.
- The tab shows the protected languages for this site.
- Runs after every other plugin has had its chance (LMG DK Language Redirects still redirects /de/, /en/ and so on first).
- The 410 page names the site instead of always saying traveltalk.dk.

### What you do differently
- Dashboard → Updates → LMG Link Repair → Update. The switch stays off until you turn it on.

## 1.0.1 – 27 Nov 2026

### Fixed
- **Every button gave "Det link, du fulgte, er udløbet".** The security code in the button links was escaped twice, so WordPress never received it. Scan, Apply, Undo and the CSV downloads now work.

### What you do differently
- Dashboard → Updates → LMG Link Repair → Update (or upload the zip again). Then Tools → Link repair → Start scan.

### Good to know
- Tested outside WordPress (syntax). Not yet tested inside WordPress itself.

## 1.0.0 – 27 Nov 2026

Covers recovery steps 1 to 3 from the Traffic playbook. Install it under Plugins → Add new → Upload, activate it, then open **Tools → Link repair**. It changes nothing until you press a button.

## 1. Links that detour
- **Start scan** reads every published post and page. It runs in batches, so the server isn't overloaded.
- The preview lists each link that costs a redirect: an old address, non-www, http or a missing slash. Next to it is the live address it will point to.
- **Apply** fixes all of them. Only the link address changes; the post date and text stay as they are, and Translator isn't triggered. Afterwards the LiteSpeed cache is purged.
- **Undo all** puts back the original text of every changed post.
- Dead links are only listed. Download them as CSV and decide for each one.

## 2. Old language addresses
- Old GTranslate addresses such as `/lt/…` and `/tr/…` are logged. The switch starts **off**, so it only logs at first.
- Switched on, they answer 410 Gone. Codes in the keep list (da, en, de, fr, es, it, nl, pt, pl, sv, se, no, nb, fi) are never touched, because they belong to Translator and LMG DK Language Redirects.
- Suggestion: leave it off for a week, read the log, then switch it on.

## 3. Orphan posts
- This lists published posts that nothing links to, using Rank Math's link counter, together with the country hub they should be linked from. You can download the list as CSV.
- The links themselves are written into the hub text. Send me the CSV and I'll draft the hub sections.

## Afterwards
In Rank Math → Link Genius, run the link audit again. Detours and broken links should drop to under 50.

### Good to know
- Install once by hand on each site (Plugins → Add New → Upload). After that, new versions arrive through Dashboard → Updates like the other LMG plugins.
- Tested outside WordPress (syntax and link logic). Not yet tested inside WordPress itself.
