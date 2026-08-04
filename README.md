# 🛡️ LogSherlock Pro — Access Monitor

Private repository that tracks all access to LogSherlock Pro deployments.

## How It Works

1. Every time someone opens LogSherlock Pro, the app pings this repo's GitHub Actions workflow
2. Access details (domain, timestamp, user name) are logged to `access_log.json`
3. If the domain is NOT in the whitelist → **Gmail alert sent to Krishna**

## Files

| File | Purpose |
|------|---------|
| `access_log.json` | All access events (auto-updated by GitHub Actions) |
| `authorized_domains.json` | Whitelist — domains allowed to run the app |
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

| Secret | Value |
|--------|-------|
| `GMAIL_APP_PASSWORD` | Google App Password for yadakrishna245@gmail.com |
| `PAT_TOKEN` | GitHub PAT with repo write access (to commit logs) |

---

**Copyright © 2026 Krishna Yada | Senior Tech Lead | Wipro**
