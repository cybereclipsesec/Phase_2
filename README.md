# Git Security & Automation Toolkit 🛡️

Welcome to my Git Security Automation repository! This production-grade toolkit combines a core Python scanning engine with a Bash automation pipeline. It demonstrates DevOps engineering, file parsing logic, regular expressions, and Git lifecycle security.

---

## 🚀 Tasks Overview

### 🛡️ Automated Git Secret Scanner
A local DevSecOps security tool designed to monitor code modifications and actively block sensitive credential leaks before they ever leave your computer.
* **Active Blocker:** Intercepts the native `git commit` workflow and aborts the save process if high-risk data is found.
* **Precision Targeting:** Scans *only* the specific files you have currently staged in Git, keeping execution speed incredibly fast.
* **AWS Credential Spotter:** Automatically identifies hardcoded AWS Access Keys and Secret Keys using secure pattern matching.
* **Generic Key Detector:** Searches for exposed tokens, private encryption keys, passwords, and authorization configurations.
* **Smart Exclusion Parameters:** Automatically ignores default configuration placeholders (like `your_secret_key_here`) to prevent false warnings.
* **Detailed Leak Logging:** Prints a clear breakdown message in your terminal showing the exact file name, line number, and code snippet where the key was leaked.

---

## 💻 How to Run the Scripts

### Prerequisites
Ensure you have **Python 3.x** and **Git** installed on your Linux terminal (Ubuntu or Kali Linux).

### Running the Setup (Linking the Tool)
Before using the tool, you must run the automatic setup file to link the background scripts into your local hidden Git configuration folder:
1. Open your terminal and navigate to the project directory.
2. Execute the setup command using:
   ```bash
   bash setup.sh
   ```

### Running a Manual System Scan
You can point your scanning engine at any file or folder to run a manual audit at any time without using Git commands:
1. Open your terminal inside the project directory.
2. Run the main CLI scanner script using:
   ```bash
   python3 src/scanner.py .
   ```

---

## 🔮 Future Enhancements (Roadmap)

I plan to expand this automation toolkit in the future with the following advanced security features:

### Core Performance Extensions:
* **Slack & Discord Webhook Alerts:** Integrate automatic webhook notifications that send instantaneous warning logs straight to developer chat channels when an internal leak is blocked.
* **Dependency Vulnerability Checker:** Add an automated parser that reads `requirements.txt` files and checks them against an open vulnerability database to block outdated, insecure software packages.
* **Custom Exclusion Files (`.scannerignore`):** Build a parsing feature that allows developers to define harmless files or test tokens inside a basic text file so the script skips scanning them automatically.
* **Automated Git Push Protection:** Upgrade the hook pipeline to include a server-side `pre-push` validation script that verifies the entire branch repository tree configuration prior to final remote cloud updates.

---

## 📋 Professional Context
* **Platform:** Swiftly Internship Milestone
* **Focus Domain:** Python Programming, Bash Scripting & DevSecOps Automation
