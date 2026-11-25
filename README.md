# lmg-builds

Finished plugin builds for Leisure Media Group sites, read by LMG Updater. Builds only: no content, briefs or keys.

`manifest.json` lists which version of each plugin should run on which site, with a SHA-256 fingerprint per zip.

Since 25 Nov 2026 (LMG Updater 1.2.0) the list holds every Leisure Media Group plugin. Entries with a zip and fingerprint are offered as updates; entries without a zip are watched only (Tools → LMG Updates shows where they run, nothing is offered). Keys starting with `name:` are found on each site by the plugin's name.

Rule: every build handed to G goes into this list in the same turn, so the list is never behind the sites.
