# LMG .dk Image Bank – release notes

## 1.0.0 – 23 November 2026

### New
- The media window on traveltalk.travel has a new tab, **.dk image bank**, next to Upload files and Media Library. It works when you add media to a post, when you set a featured image, and in the block editor's image blocks.
- The tab opens with the newest images on traveltalk.dk. Type a word and press Search to find images by title, alt text or caption. **Show more** loads the next 40.
- Click an image to use it. It is copied into the .travel Media Library once, with its title, alt text, caption and credit, and then opens selected in the Media Library tab, so you click **Insert into post** or **Set featured image** as usual.
- Images that are already on .travel carry a green **Already on this site** label. Clicking one reuses the copy, so the same image is never copied twice. This also covers images LMG Translator copied when it translated an article.
- Title, alt text and caption are translated from Danish into the site's language with DeepL, when LMG Translator on .travel has a DeepL key. The Danish texts are kept with the image.
- **Media → .dk image bank** shows whether the connection to traveltalk.dk works, how many images it can see, and whether translation is available. Administrators can switch translation off there. These release notes are on the same page.

### What you do differently
- Before searching stock or uploading again, open the **.dk image bank** tab and search there.
- Search in Danish: the texts on .dk are mostly Danish ("Positano", "vinbar Rom", "fyrtårn").
- Check the alt text after inserting: it is translated without the article around it, so adjust it to the article where needed.

### Good to know
- Install on traveltalk.travel only. On traveltalk.dk the tab stays off.
- It uses the Translator bridge login when there is one, and otherwise the images traveltalk.dk shows publicly. No setup is needed.
- Licences: some .dk images come from paid stock (Depositphotos and others) where the licence may cover one website only. Check before using such an image on .travel. Unsplash and Pexels images are fine.
- The alt text goes into the language the site runs in (English on .travel). On a German translation, adjust it by hand.
- Search results are kept for 10 minutes, so an image uploaded to .dk a moment ago may take up to 10 minutes to appear.
- Not tested in a live WordPress yet: the tab, copying and the featured image flow were checked against the code and traveltalk.dk's real image data, but not clicked through on .travel. Please try it on one draft first.

### Older content
- Not affected. Nothing changes in existing posts or images. Images Translator copied earlier are recognised and reused from installation on.
