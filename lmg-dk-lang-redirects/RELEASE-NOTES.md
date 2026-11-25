# LMG DK Language Redirects – release notes

For editors and reviewers on traveltalk.dk. Newest first.

## 1.1.0 – 10 Nov 2026

### New
- **Swedish, Norwegian and Finnish stay on traveltalk.dk.** The front pages /sv/, /no/ and /fi/ and the translations under them are no longer sent to traveltalk.travel. This ends the loop where traveltalk.dk sent /sv/ to traveltalk.travel and traveltalk.travel sent it back.
- **Old Nordic addresses go to the right front page on traveltalk.dk.** /se/ goes to /sv/, /nb/ goes to /no/, and the old Nordic pages (for example /no/med-fly/ or /fi/tiella/) go to that language's front page on traveltalk.dk instead of traveltalk.travel.
- English, German and the other languages are sent to traveltalk.travel as before.

### What you do differently
- Nothing. Install it over the existing plugin (Plugins → Add New → Upload → Replace current), then purge LiteSpeed.
- Do not tick "Redirect these now" under Tools → Language redirects. The Swedish, Norwegian and Finnish lines are no longer listed there; the English and German ones still are.

### Good to know
- Tested: the code loads without errors, and a local test of the addresses above gave the expected targets. Not tested on the live site.
- Check after installing: https://www.traveltalk.dk/sv/ and https://www.traveltalk.dk/no/ open on traveltalk.dk; https://www.traveltalk.dk/en/ still goes to traveltalk.travel.
- Version 1.0.0 was not in the repository before today; it was copied from the live site first, so the change can be seen line by line.

### Older content
- Applies automatically from installation on. Nothing to run.
