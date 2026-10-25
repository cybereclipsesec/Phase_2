import re
import os

SECRET_PATTERNS = {
    "AWS Access Key ID": r"([^A-Z0-9]|^)(AKIA[A-Z0-9]{16})([^A-Z0-9]|$)",
    "AWS Secret Access Key": r"([^A-Za-z0-9+/]|^)([A-Za-z0-9+/]{40})([^A-Za-z0-9+/]|$)",
    "Generic API Key / Secret": r"(?i)(key|secret|password|token)[ \t]*[:=][ \t]*['\"]([A-Za-z0-9_\.\-\~\+\/]{16,})['\"]",
    "Private Key": r"-----BEGIN [A-Z]+ PRIVATE KEY-----"
}

def scan_file_for_secrets(file_path):
    findings = []
    if not os.path.isfile(file_path) or os.path.basename(file_path).endswith(('.png', '.jpg', '.pdf', '.pyc', '.git')):
        return findings
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                for name, pattern in SECRET_PATTERNS.items():
                    match = re.search(pattern, line)
                    if match:
                        secret_value = match.group(2) if match.lastindex and match.lastindex >= 2 else match.group(0)
                        if any(placeholder in secret_value.lower() for placeholder in ["your_", "my_", "placeholder", "todo"]):
                            continue
                        findings.append({
                            "file": file_path,
                            "line": line_num,
                            "type": name,
                            "snippet": line.strip()[:60]
                        })
    except Exception as e:
        print(f"[-] Error reading {file_path}: {str(e)}")
    return findings
