#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║  LogSherlock Pro — License Key Generator                     ║
║  Author: Krishna Yada | Senior Tech Lead | Wipro             ║
║                                                              ║
║  Usage:                                                      ║
║    python generate_license.py                                ║
║    python generate_license.py --domain abc.cloudfront.net    ║
║    python generate_license.py --domain abc.cloudfront.net --name "John" --days 30  ║
║                                                              ║
║  Works on: Windows (PowerShell/CMD) | Linux | Mac            ║
╚══════════════════════════════════════════════════════════════╝
"""

import json
import hashlib
import secrets
import os
import sys
from datetime import datetime, timedelta

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ─── CONFIG ──────────────────────────────────────────────────
LICENSES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'licenses.json')
SECRET_SALT = "KY_LOGSHERLOCK_2026_WIPRO_SENIOR_TECH_LEAD"

def generate_key():
    """Generate a random license key."""
    random_hex = secrets.token_hex(16)
    hash_val = hashlib.sha256(f"{random_hex}:{SECRET_SALT}:{datetime.now().isoformat()}".encode()).hexdigest()[:16].upper()
    return f"LS-{hash_val[:4]}-{hash_val[4:8]}-{hash_val[8:12]}-{hash_val[12:16]}"

def load_licenses():
    """Load existing licenses."""
    if os.path.exists(LICENSES_FILE):
        with open(LICENSES_FILE, 'r') as f:
            return json.load(f)
    return {"licenses": [], "secret_salt": SECRET_SALT, "trial_days": 7, "last_updated": ""}

def save_licenses(data):
    """Save licenses back to file."""
    data['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    with open(LICENSES_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def list_licenses(data):
    """Display all active licenses."""
    print("\n┌─────────────────────────────────────────────────────────────────────┐")
    print("│  ACTIVE LICENSES                                                     │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    active = [l for l in data['licenses'] if l.get('active', False)]
    if not active:
        print("│  No active licenses found.                                          │")
    for lic in active:
        status = "✅" if lic.get('expires_at', '') >= datetime.now().strftime('%Y-%m-%d') else "⚠️ EXPIRED"
        print(f"│  {status} {lic['key']}")
        print(f"│     Domain: {lic.get('domain', '*')} | To: {lic.get('issued_to', '?')} | Expires: {lic.get('expires_at', '?')}")
        print("│")
    print(f"│  Total: {len(active)} active license(s)")
    print("└─────────────────────────────────────────────────────────────────────┘\n")

def revoke_license(data, key):
    """Revoke a license by key."""
    for lic in data['licenses']:
        if lic['key'] == key:
            lic['active'] = False
            lic['revoked_at'] = datetime.now().strftime('%Y-%m-%d')
            save_licenses(data)
            print(f"\n🚫 License REVOKED: {key}")
            print(f"   Was issued to: {lic.get('issued_to', '?')} | Domain: {lic.get('domain', '?')}")
            return True
    print(f"\n❌ License not found: {key}")
    return False

def interactive_mode():
    """Interactive menu for license management."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║        🔑 LogSherlock Pro — License Manager                  ║
║        © 2026 Krishna Yada | Senior Tech Lead | Wipro        ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    data = load_licenses()
    
    while True:
        print("\n┌─── MENU ────────────────────────────────┐")
        print("│  1. Generate new license key             │")
        print("│  2. List all active licenses             │")
        print("│  3. Revoke a license                     │")
        print("│  4. Exit                                 │")
        print("└──────────────────────────────────────────┘")
        
        choice = input("\n  Enter choice (1-4): ").strip()
        
        if choice == '1':
            print("\n─── GENERATE NEW LICENSE ───")
            domain = input("  Domain (e.g., abc.cloudfront.net) [* for any]: ").strip() or '*'
            name = input("  Issued to (person/team name): ").strip() or 'Unknown'
            days_str = input("  Valid for how many days? [365]: ").strip() or '365'
            
            try:
                days = int(days_str)
            except ValueError:
                days = 365
            
            lic_type = input("  Type (standard/extended/master) [standard]: ").strip() or 'standard'
            
            key = generate_key()
            expires = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
            
            new_license = {
                "key": key,
                "domain": domain,
                "issued_to": name,
                "issued_at": datetime.now().strftime('%Y-%m-%d'),
                "expires_at": expires,
                "type": lic_type,
                "active": True
            }
            
            data['licenses'].append(new_license)
            save_licenses(data)
            
            print(f"""
╔══════════════════════════════════════════════════════════════╗
║  ✅ LICENSE GENERATED SUCCESSFULLY!                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🔑 Key:        {key}              ║
║  🌐 Domain:     {domain:<40}   ║
║  👤 Issued to:  {name:<40}   ║
║  📅 Expires:    {expires:<40}   ║
║  📋 Type:       {lic_type:<40}   ║
║                                                              ║
║  Share this key with the user. They enter it in              ║
║  LogSherlock Pro → Settings (trial banner → Enter Key)       ║
╚══════════════════════════════════════════════════════════════╝
            """)
        
        elif choice == '2':
            list_licenses(data)
        
        elif choice == '3':
            key = input("\n  Enter license key to revoke: ").strip().upper()
            if key:
                confirm = input(f"  Are you sure you want to revoke {key}? (y/n): ").strip().lower()
                if confirm == 'y':
                    revoke_license(data, key)
                else:
                    print("  Cancelled.")
        
        elif choice == '4':
            print("\n  👋 Bye! — Krishna Yada\n")
            break
        
        else:
            print("  ❌ Invalid choice. Try 1-4.")

def cli_mode():
    """Command-line argument mode for quick generation."""
    import argparse
    parser = argparse.ArgumentParser(description='LogSherlock Pro License Generator')
    parser.add_argument('days', nargs='?', type=int, default=7, help='Validity in days (default: 7)')
    parser.add_argument('--domain', '-d', default='d3tv1czat55yad.cloudfront.net', help='Domain (default: your CloudFront)')
    parser.add_argument('--name', '-n', default='', help='Person/team name (optional)')
    parser.add_argument('--type', '-t', choices=['standard', 'extended', 'master'], default='standard', help='License type')
    parser.add_argument('--list', '-l', action='store_true', help='List all active licenses')
    parser.add_argument('--revoke', '-r', help='Revoke a license key')
    
    args = parser.parse_args()
    data = load_licenses()
    
    if args.list:
        list_licenses(data)
        return
    
    if args.revoke:
        revoke_license(data, args.revoke.upper())
        return
    
    # Generate
    key = generate_key()
    expires = (datetime.now() + timedelta(days=args.days)).strftime('%Y-%m-%d')
    
    new_license = {
        "key": key,
        "domain": args.domain,
        "issued_to": args.name or 'User',
        "issued_at": datetime.now().strftime('%Y-%m-%d'),
        "expires_at": expires,
        "type": args.type,
        "active": True
    }
    
    data['licenses'].append(new_license)
    save_licenses(data)
    
    print(f"\n  KEY: {key}")
    print(f"  Expires: {expires} ({args.days} days)")
    print(f"")


if __name__ == '__main__':
    if '--interactive' in sys.argv or '-i' in sys.argv:
        sys.argv = [a for a in sys.argv if a not in ('--interactive', '-i')]
        interactive_mode()
    else:
        cli_mode()
