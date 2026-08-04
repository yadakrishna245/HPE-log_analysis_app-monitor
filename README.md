# 🛡️ LogSherlock Pro — Access Monitor & License Manager

Private repository that controls access to LogSherlock Pro deployments.

**Only Krishna Yada can generate license keys. Without a valid key, the app is 100% blocked.**

---

## 🔑 How to Generate a License Key (Step by Step)

### Option 1: Using the Python Script (Recommended)

**Step 1:** Clone this repo (if not already done)
```bash
git clone https://github.com/yadakrishna245/HPE-log_analysis_app-monitor.git
cd HPE-log_analysis_app-monitor
```

**Step 2:** Run the interactive license manager
```powershell
python generate_license.py
```

**Step 3:** Choose option `1` (Generate new license key)
```
┌─── MENU ────────────────────────────────┐
│  1. Generate new license key             │  ← Select this
│  2. List all active licenses             │
│  3. Revoke a license                     │
│  4. Exit                                 │
└──────────────────────────────────────────┘
```

**Step 4:** Fill in the details when prompted:
```
  Domain (e.g., abc.cloudfront.net) [* for any]: d3tv1czat55yad.cloudfront.net
  Issued to (person/team name): Rahul Sharma
  Valid for how many days? [365]: 30
  Type (standard/extended/master) [standard]: standard
```

**Step 5:** You'll get the key:
```
✅ LICENSE GENERATED SUCCESSFULLY!

🔑 Key:       LS-A3F2-9B1C-E7D4-5H8K
🌐 Domain:    d3tv1czat55yad.cloudfront.net
👤 Issued to: Rahul Sharma
📅 Expires:   2026-09-03
📋 Type:      standard
```

**Step 6:** Commit and push the updated `licenses.json`
```bash
git add licenses.json
git commit -m "license: New key for Rahul Sharma"
git push
```

**Step 7:** Share the key with the user. They enter it in the app's activation screen.

---

### Option 2: One-Liner Command (Quick)

```powershell
# Generate a key for someone
python generate_license.py --domain "d3tv1czat55yad.cloudfront.net" --name "Rahul Sharma" --days 30

# Then commit + push
git add licenses.json && git commit -m "license: Rahul Sharma" && git push
```

---

### Option 3: Via GitHub Actions (from browser)

1. Go to: https://github.com/yadakrishna245/HPE-log_analysis_app-monitor/actions
2. Click **"🔑 Generate License Key"** workflow
3. Click **"Run workflow"**
4. Fill in: Domain, Name, Days, Type
5. Click **"Run workflow"** button
6. Wait ~30 seconds — key is auto-generated, committed, and emailed to you

---

## 📋 Other Commands

### List all active licenses
```powershell
python generate_license.py --list
```

### Revoke a license (block someone)
```powershell
python generate_license.py --revoke "LS-A3F2-9B1C-E7D4-5H8K"
git add licenses.json && git commit -m "revoke: Rahul" && git push
```

### Via GitHub Actions (revoke from browser)
1. Actions → **"🚫 Revoke License"** → Run workflow → Enter key → Run

---

## 🔐 Master Keys (Never Expire)

These are your personal keys — they work forever on any domain:

| Key | Domain | Purpose |
|-----|--------|---------|
| `LS-MASTER-2026-KRISHNA-YADA` | d3tv1czat55yad.cloudfront.net | Your main deployment |
| `LS-MASTER-LOCALHOST-DEV` | localhost | Local development |

---

## 📌 When You Move to New AWS Account / New CloudFront URL

**Step 1:** Edit `authorized_domains.json` and add the new domain:

```json
{
  "authorized_domains": [
    "d3tv1czat55yad.cloudfront.net",
    "NEW_CLOUDFRONT_ID.cloudfront.net",
    "localhost",
    "127.0.0.1"
  ]
}
```

**Step 2:** Generate a new master key for the new domain:
```powershell
python generate_license.py --domain "NEW_CLOUDFRONT_ID.cloudfront.net" --name "Krishna Yada" --days 99999 --type master
```

**Step 3:** Deploy with the GitHub token:
```powershell
cd deploy/
sam deploy --parameter-overrides "GhMonitorToken=YOUR_GH_TOKEN"
```

---

## How It Works

```
User opens LogSherlock Pro
    ↓
App checks: Has license key in browser?
    ↓
├── NO → Show license activation screen (BLOCKED - can't use app)
├── YES → Validate key with /api/license/validate
│         ↓
│         Lambda fetches licenses.json from THIS repo
│         ↓
│         ├── Key found + active + not expired → ✅ App works
│         ├── Key not found or expired → ❌ BLOCKED
│         └── Server unreachable → ❌ BLOCKED
```

---

## Files

| File | Purpose |
|------|---------|
| `licenses.json` | ⭐ All license keys (active + revoked) |
| `authorized_domains.json` | Whitelist of allowed domains |
| `access_log.json` | Access tracking log |
| `generate_license.py` | 🐍 CLI tool to generate/list/revoke keys |
| `.github/workflows/log_access.yml` | Access monitoring + Gmail alerts |
| `.github/workflows/generate_license.yml` | Generate key from GitHub UI |
| `.github/workflows/revoke_license.yml` | Revoke key from GitHub UI |

---

## GitHub Secrets

| Secret | Status |
|--------|--------|
| `GMAIL_APP_PASSWORD` | ✅ Added |
| `PAT_TOKEN` | ✅ Added |

---

## Gmail Alerts

You receive email at `yadakrishna245@gmail.com` when:
- ⚠️ Someone accesses app from unauthorized domain
- 🔑 New license key is generated (via GitHub Actions)

---

**Copyright © 2026 Krishna Yada | Senior Tech Lead | Wipro**
