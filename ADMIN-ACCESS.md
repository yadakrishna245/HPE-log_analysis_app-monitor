# 🔐 LogSherlock Pro — Admin Dashboard Access

> **PRIVATE** — This file is in the private monitor repo only. Never share with team.

---

## 🌐 Access Links

| Environment | Admin Dashboard URL |
|-------------|-------------------|
| **Local (your laptop)** | `http://localhost:8888/admin` |
| **Direct file** | Open `admin-dashboard/admin-dashboard.html` in browser |
| **AWS CloudFront** | Not deployed (kept private) |

---

## 🔑 Login Credentials

| Field | Value |
|-------|-------|
| **Username** | `krishna` |
| **Password** | `Krishna@8688#$` |
| **Reset Email** | `yadakrishna245@gmail.com` |

---

## 📊 What You Can Do

### Tab 1: Overview
- Total users, active licenses, expired, revenue stats
- 7-day activity chart
- Quick actions

### Tab 2: License Management
- See ALL activated users in a table
- User name, key, activation date, last seen, days remaining
- Reset any key (transfer to new machine)
- Copy keys

### Tab 3: Generate Keys
- Generate keys directly from browser
- 7/30/90/365 day options + Lifetime
- Bulk generate (up to 20 at once)
- Copy all to clipboard

### Tab 4: System Info
- App version, AWS stack info
- All endpoints and tables
- Feature count

### Tab 5: Settings
- Change admin password
- Export all data as CSV
- API key display

---

## 🖥️ API Endpoints (Admin Only)

```bash
# List ALL users
curl -X POST https://5bruz4e6hj.execute-api.us-east-1.amazonaws.com/prod/api/license/list-all \
  -H "Content-Type: application/json" \
  -d '{"admin_secret":"LSPRO2026KRISHNA"}'

# Check specific key
curl -X POST https://5bruz4e6hj.execute-api.us-east-1.amazonaws.com/prod/api/license/status \
  -H "Content-Type: application/json" \
  -d '{"license_key":"HTRO-0A25-5B44-00FJ","admin_secret":"LSPRO2026KRISHNA"}'

# Reset key (allow transfer)
curl -X POST https://5bruz4e6hj.execute-api.us-east-1.amazonaws.com/prod/api/license/reset \
  -H "Content-Type: application/json" \
  -d '{"license_key":"HTRO-0A25-5B44-00FJ","admin_secret":"LSPRO2026KRISHNA"}'
```

---

## 📁 Where Admin Files Live

| Location | What |
|----------|------|
| **This repo** (`HPE-log_analysis_app-monitor`) | `admin-dashboard/admin-dashboard.html` — the dashboard file |
| **Your laptop** | `LogSherlock-Pro-Local/Administration/admin-dashboard.html` — same file, served at /admin |
| **NOT in public repo** | ❌ Removed from `Log_analysis` repo and `.gitignore`d |
| **NOT in shared ZIP** | ❌ ZIP only has user-facing files |

---

## ⚠️ Security Notes

1. Admin dashboard is NOT accessible to your team
2. The `admin_secret` (`LSPRO2026KRISHNA`) is only in this private repo
3. Password hash is stored in the HTML (SHA-256) — not plain text
4. Even if someone finds the admin URL, they need the password
5. API endpoints require `admin_secret` — team can't query license data

---

## 💰 Pricing (For Reference)

| Plan | Duration | Command |
|------|----------|---------|
| Trial | 7 days | `.\Generate-License.ps1 -Days 7` |
| Monthly | 30 days | `.\Generate-License.ps1 -Days 30` |
| Quarterly | 90 days | `.\Generate-License.ps1 -Days 90` |
| Yearly | 365 days | `.\Generate-License.ps1 -Days 365` |
| Lifetime | Forever | `.\Generate-License.ps1 -Lifetime` |

---

© 2026 Krishna Yada. All Rights Reserved.
