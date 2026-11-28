# When a plugin update breaks a site

Written after 27–28 Nov 2026: LeisureIntel 3.7.1 took traveltalk.travel down for about 17 hours. The build was made from a repository copy that was missing 3 files the live version had.

## 1. Before anything is released (stops this from happening)
- **Build from the live copy, never from the repository alone.** Start from Tools → LMG Updates → "Download a copy" on a site that runs the current version. Apply the change to that copy. The repository can lag behind what is live.
- **Run `python3 tools/check_zip.py <zip>` on every zip before it goes on the list.** It fails if any `require`/`include` points to a file that is not in the zip.
- **Release to one site first, and keep the others waiting.** List only one site under `sites`. Load its wp-admin and one uncached page (`/?x=1`). Only after that, add the other sites.

## 2. If a site shows "critical error" after an update
Speed matters most: switch the broken plugin off first, and fix it afterwards.

**SSH (from Gunnar's Mac, key at `~/code/leisuretalk/traveltalk_key`).**
Hosts and users are in github.com-new `scripts/sunday_status.sh`. User `u537990900_<siteid>`, host `72.62.144.236`, port `65002`, WordPress in `~/websites/<siteid>/public_html`.

| site | site id |
|---|---|
| traveltalk.dk | NwRtxbUOb |
| traveltalk.travel | 70B78Ztwh |
| winetalk.dk | dLpKk6Kvn |
| worldsporttalk.com | x29BxCXCn |
| think-smarter.net | SbtnD7ML6 |

1. **Host key.** Hostinger's server presents changing host keys (seen 28 Nov), and Claude's safety rules on the Mac won't accept a new key on their own. Gunnar runs this once in Terminal and answers `yes`:
   `ssh -p 65002 -i ~/code/leisuretalk/traveltalk_key u537990900_<siteid>@72.62.144.236 exit`
   If it says "REMOTE HOST IDENTIFICATION HAS CHANGED", run this first, then the line above:
   `ssh-keygen -R "[72.62.144.236]:65002"`
2. **Check before changing anything.** `grep Version wp-content/plugins/<plugin>/<plugin>.php` should show the broken version.
3. **Move it aside, never delete it.** `mv wp-content/plugins/<plugin> ~/<plugin>-broken-<version>-<date>`
   Check that `https://<site>/wp-login.php` now answers 200.
4. **Restore the last good version.** Get it via "Download a copy" from a site that still runs it, then `scp` it up, `unzip` it into `wp-content/plugins/` and run `wp plugin activate <plugin>`. Check `wp-login.php` and `/?x=1` again.
5. **Pull the broken version off the list.** In `manifest.json`, set the entry back to the old version, remove the zip and merge. Then tell Gunnar which other sites already installed it.

**No SSH.** Use hPanel → the site → File Manager → `public_html/wp-content/plugins` and rename the folder. The hosting is under the tech person's Hostinger account, not Gunnar's.
