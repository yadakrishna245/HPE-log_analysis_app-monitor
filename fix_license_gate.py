"""Replace the license gate in index.html with hard block version."""
import os

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'HPE-Log_analysis', 'templates', 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_block = r"""// LICENSE HARD BLOCK - No license = No app. Must enter Name + Email + Mobile + Key.
(function _licenseGate() {
    var savedKey = localStorage.getItem('ls_license_key');
    var cacheValid = localStorage.getItem('ls_license_valid');
    var cacheTime = parseInt(localStorage.getItem('ls_license_checked') || '0');
    var userReg = localStorage.getItem('ls_user_registration');
    var now = Date.now();
    // If validated in last 6 hours AND registered, allow
    if (savedKey && cacheValid === 'true' && userReg && (now - cacheTime) < 6*3600000) return;
    // HARD BLOCK - wipe page and show license form
    document.documentElement.innerHTML = '<head><meta charset="utf-8"><title>LogSherlock Pro - License Required</title></head><body style="margin:0;background:#0a0a1a;font-family:-apple-system,BlinkMacSystemFont,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:20px;box-sizing:border-box;"><div style="background:#12122b;border:2px solid #01a982;border-radius:20px;padding:40px 36px;max-width:440px;width:100%;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.8);"><div style="font-size:42px;margin-bottom:8px;">&#x1F510;</div><h2 style="color:#fff;margin:0 0 4px;font-size:22px;">LogSherlock Pro</h2><p style="color:#01a982;margin:0 0 20px;font-size:12px;font-weight:600;letter-spacing:0.5px;">LICENSED SOFTWARE — ACTIVATION REQUIRED</p><div style="text-align:left;margin-bottom:14px;"><label style="color:#aaa;font-size:11px;font-weight:600;display:block;margin-bottom:4px;">FULL NAME *</label><input id="_lic_name" type="text" placeholder="e.g., Rahul Sharma" style="width:100%;padding:10px 14px;border-radius:8px;border:1px solid #333;background:#0a0a1a;color:#fff;font-size:13px;box-sizing:border-box;outline:none;"/></div><div style="text-align:left;margin-bottom:14px;"><label style="color:#aaa;font-size:11px;font-weight:600;display:block;margin-bottom:4px;">EMAIL ADDRESS *</label><input id="_lic_email" type="email" placeholder="e.g., rahul@company.com" style="width:100%;padding:10px 14px;border-radius:8px;border:1px solid #333;background:#0a0a1a;color:#fff;font-size:13px;box-sizing:border-box;outline:none;"/></div><div style="text-align:left;margin-bottom:14px;"><label style="color:#aaa;font-size:11px;font-weight:600;display:block;margin-bottom:4px;">MOBILE NUMBER *</label><input id="_lic_mobile" type="tel" placeholder="e.g., 9876543210" style="width:100%;padding:10px 14px;border-radius:8px;border:1px solid #333;background:#0a0a1a;color:#fff;font-size:13px;box-sizing:border-box;outline:none;"/></div><div style="text-align:left;margin-bottom:20px;"><label style="color:#aaa;font-size:11px;font-weight:600;display:block;margin-bottom:4px;">LICENSE KEY *</label><input id="_lic_key" type="text" placeholder="LS-XXXX-XXXX-XXXX-XXXX" style="width:100%;padding:10px 14px;border-radius:8px;border:1px solid #333;background:#0a0a1a;color:#fff;font-family:monospace;font-size:14px;text-align:center;box-sizing:border-box;outline:none;letter-spacing:1px;"/></div><div id="_lic_error" style="color:#ef4444;font-size:12px;margin-bottom:12px;display:none;padding:8px;background:rgba(239,68,68,0.1);border-radius:6px;"></div><button id="_lic_btn" onclick="_doActivate()" style="width:100%;padding:14px;border-radius:10px;border:none;background:#01a982;color:#fff;font-size:15px;font-weight:700;cursor:pointer;">&#x1F511; Activate License</button><div style="margin-top:20px;padding-top:16px;border-top:1px solid #222;"><p style="color:#666;font-size:11px;margin:0 0 8px;">Don\'t have a license key? Contact:</p><p style="color:#fff;font-size:12px;margin:0;font-weight:500;">Krishna Yada | Senior Tech Lead | Wipro<br><span style="color:#01a982;">yadakrishna245@gmail.com</span></p></div><div style="margin-top:16px;font-size:9px;color:#444;">Copyright 2026 Krishna Yada. All Rights Reserved.</div></div></body>';
    // Add activation script
    var s = document.createElement('script');
    s.textContent = 'function _doActivate(){var n=document.getElementById("_lic_name").value.trim();var e=document.getElementById("_lic_email").value.trim();var m=document.getElementById("_lic_mobile").value.trim();var k=(document.getElementById("_lic_key").value||"").trim().toUpperCase();var err=document.getElementById("_lic_error");var btn=document.getElementById("_lic_btn");if(!n||n.length<2){err.textContent="Please enter your full name.";err.style.display="block";return;}if(!e||e.indexOf("@")<0||e.indexOf(".")<0){err.textContent="Please enter a valid email address.";err.style.display="block";return;}if(!m||m.replace(/[^0-9]/g,"").length<10){err.textContent="Please enter valid mobile number (min 10 digits).";err.style.display="block";return;}if(!k||k.indexOf("LS-")!==0){err.textContent="Invalid license key. Must start with LS-";err.style.display="block";return;}btn.disabled=true;btn.textContent="Validating...";err.style.display="none";fetch("/api/license/validate",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({key:k,domain:location.hostname})}).then(function(r){return r.json();}).then(function(data){if(data.valid){localStorage.setItem("ls_license_key",k);localStorage.setItem("ls_license_valid","true");localStorage.setItem("ls_license_checked",String(Date.now()));localStorage.setItem("ls_user_registration",JSON.stringify({name:n,email:e,mobile:m,activated_at:new Date().toISOString()}));localStorage.setItem("ls_username",n);location.reload();}else{btn.disabled=false;btn.textContent="Activate License";err.textContent=data.reason||"Invalid or expired license key.";err.style.display="block";}}).catch(function(){btn.disabled=false;btn.textContent="Activate License";err.textContent="Cannot reach license server. Check internet.";err.style.display="block";});}document.addEventListener("keydown",function(ev){if(ev.key==="Enter")_doActivate();});';
    document.body.appendChild(s);
    throw new Error('LICENSE_BLOCK');
})();
// END LICENSE GATE
"""

# Replace lines 1224 to 1427 (0-indexed, inclusive)
result = lines[:1224] + [new_block + '\n'] + lines[1427:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f"Done! Replaced lines 1225-1428 with hard block license gate.")
print(f"Total lines: {len(lines)} -> {len(result)}")
