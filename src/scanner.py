#!/usr/bin/env python3
import os
import sys
import argparse
from detector import scan_file_for_secrets

def main():
    parser = argparse.ArgumentParser(description="🛡️ Automated Git Secret Scanner CLI")
    parser.add_argument("path", nargs="?", default=".", help="Target path to scan")
    args = parser.parse_args()

    all_findings = []
    if os.path.isfile(args.path):
        all_findings.extend(scan_file_for_secrets(args.path))
    elif os.path.isdir(args.path):
        for root, _, files in os.walk(args.path):
            if '.git' in root:
                continue
            for file in files:
                all_findings.extend(scan_file_for_secrets(os.path.join(root, file)))

    if all_findings:
        print("\n❌ CRITICAL: Hardcoded secrets detected!")
        print("=" * 60)
        for leak in all_findings:
            print(f"📍 File: {leak['file']} (Line {leak['line']})")
            print(f"   Type:  {leak['type']}")
            print(f"   Match: {leak['snippet']}")
            print("-" * 60)
        sys.exit(1)
    else:
        print("\n✅ Clean bill of health! No hardcoded secrets found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
