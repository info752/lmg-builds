# LMG Link Repair – release notes

For G and the editors. Newest first.

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
