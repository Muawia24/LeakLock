# 🔒 LeakLock
**Stop secrets before they reach GitHub.**

LeakLock is a lightweight security tool that **scans your code in real time and blocks commits containing API keys, tokens, or passwords**.  
It integrates with Git via a pre-commit hook, so secrets never leave your machine.

---

## ✨ Features
- 🛡️ **Pre-commit protection** — blocks commits with secrets automatically.  
- 🔍 **Multi-pattern detection** — supports AWS, GitHub, Slack, GCP, and more.  
- 📊 **Entropy-based scanning** — detects unknown/novel secrets beyond regex rules.  
- ⚡ **Cross-platform** — works on Linux, macOS, and Windows (via Git Bash/WSL).  
- 🔗 **CI/CD ready** — can run in GitHub Actions, GitLab CI, or any pipeline.  
- 🧠 (Optional) **LLM-powered detection** — reduce false positives and detect unknown formats.  

---

## 🚀 Installation
Install from PyPI:

```bash
pip install leaklock
```

Or install from source:

```bash
git clone https://github.com/your-username/leaklock.git
cd leaklock
pip install -e .
```

##⚡ Quick Start
Initialize LeakLock in your repo

```bash
leaklock install
```

This adds a Git pre-commit hook.
Make a commit

```bash
git add .
git commit -m "test commit"
```
If secrets are found → ❌ commit is blocked with a warning.

If clean → ✅ commit goes through.

🔑 Example Output
```bash
❌ Commit blocked by LeakLock (secrets detected):

- AWS Access Key ID detected in app/config.py:23
- Slack Token detected in utils/slack.py:10

Fix or remove these values before committing.
```

## ⚙️ Configuration

LeakLock can be configured via a .leaklock.yml file:

```yaml
ignore_patterns:
  - "tests/*"
  - "*.md"

allowlist:
  - "DUMMY_KEY_12345"
```


🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature/new-scan)

Submit a PR

📜 License
MIT License © 2025 LeakLock Contributors