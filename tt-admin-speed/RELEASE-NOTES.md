# TT Admin Speed Fix – release notes

## 1.2 – 7 November 2026

### New
- The plugin no longer switches off application passwords. That setting is what stopped LMG Translator from saving translations on traveltalk.travel ("HTTP 401: Sorry, you are not allowed to do that").
- Everything else stays as before: fewer background checks in wp-admin, no slow WordPress.org news box on the dashboard, and the old blog-ping job that held the server up for about 46 seconds each time stays switched off.

### What you do differently
- Nothing day to day. Under Users → Profile you will now see an "Application Passwords" section again. Leave the existing ones alone; the Translator bridge uses one.

### Good to know
- The plugin now lives in its own folder. Install it as described in the handover: deactivate and delete 1.1 first, then upload 1.2. If both are active at once nothing breaks, but the settings run twice.
- Tested: the code loads without errors. Not tested on a live site before handover.

### Older content
- Not affected. The plugin changes how wp-admin behaves, not posts or pages.
