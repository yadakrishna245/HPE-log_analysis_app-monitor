# 🛡️ LogSherlock Pro — Access Monitor

Private repository that tracks all access to LogSherlock Pro deployments.

## How It Works

1. Every time someone opens LogSherlock Pro, the app pings this repo's GitHub Actions workflow
2. Access details (domain, timestamp, user name) are logged to `access_log.json`
3. If the domain is NOT in the whitelist → **Gmail alert sent to Krishna**

## 📌 When You Move to New AWS Account / New CloudFront URL

**Edit `authorized_domains.json`** and add the new domain:

```json
{
  "authorized_domains": [
    "d3tv1czat55yad.cloudfront.net",   ← current
    "NEW_CLOUDFRONT_ID.cloudfront.net", ← add new one here
    "localhost",
    "127.0.0.1"
  ]
}
```

**How to edit:**
1. Open: https://github.com/yadakrishna245/HPE-log_analysis_app-monitor/blob/main/authorized_domains.json
2. Click ✏️ pencil icon (Edit)
3. Add new domain to the list
4. Commit changes

> ⚠️ If you DON'T add the new domain, you'll get Gmail alerts for your own app!

## Also Update Lambda Token (if new AWS account)

When you deploy to a new AWS account, you need to set the GitHub token in the new Lambda:

```powershell
cd deploy/
sam deploy --parameter-overrides "GhMonitorToken=YOUR_GH_TOKEN_HERE"
```

Or set it manually in AWS Console:
- Lambda → Environment Variables → `GH_MONITOR_TOKEN` = your GitHub token

## Files

| File | Purpose |
|------|---------|
| `access_log.json` | All access events (auto-updated by GitHub Actions) |
| `authorized_domains.json` | ⭐ Whitelist — domains allowed to run the app |
| `.github/workflows/log_access.yml` | Workflow that processes pings and sends alerts |

## How to Block Someone

1. Check `access_log.json` for unauthorized domains
2. If you want to block a domain, it's already blocked (only whitelisted ones are allowed)
3. To allow a new domain (when you move AWS), edit `authorized_domains.json`

## Gmail Alert

When unauthorized access is detected, you'll receive an email at `yadakrishna245@gmail.com` with:
- Domain where app is running
- Timestamp (IST)
- User name (if available)

## GitHub Secrets Required

| Secret | Value | Status |
|--------|-------|--------|
| `GMAIL_APP_PASSWORD` | Google App Password for yadakrishna245@gmail.com | ✅ Added |
| `PAT_TOKEN` | GitHub PAT with repo write access (to commit logs) | ✅ Added |

---

**Copyright © 2026 Krishna Yada | Senior Tech Lead | Wipro**
