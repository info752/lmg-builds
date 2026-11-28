# LeisureIntel – release notes

## 3.7.2 – 28 Nov 2026

**New**
- The publishing rhythm check (LeisureIntel → Publiceringsrytme, and the "Underpublicering" / "Stagnations-varsel" alerts) now counts translations made with LMG Translator, not only articles. traveltalk.travel, which mostly publishes translations, is no longer flagged as quiet when it isn't.

**What you do differently**
- Nothing.

**Good to know**
- The weekly analysis (Monday) already sees translations: it works from Google Search Console pages, so a new translation shows up once Google has data for it.
- The weekly content audit still reads articles only, on purpose: translations are checked by LMG Translator's own correction step, and auditing them here would add AI cost per language.
- Built on the exact copy running on traveltalk.dk (3.7.0) with only these changes; checked that every file the plugin loads is in the zip. Tested on traveltalk.travel first.
- 3.7.1 (27 Nov) was withdrawn: it was built from an incomplete copy and stopped traveltalk.travel from loading. Never install 3.7.1.

**Older content**
- Applies automatically: the rhythm numbers are recounted within 6 hours of installing, or at once with "Opdatér nu".
