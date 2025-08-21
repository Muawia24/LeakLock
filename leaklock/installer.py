import os
import platform
from pathlib import Path


HOOK_SCRIPT_SH = """
#!/bin/sh

# LeakLock pre-commit hook
leaklock
RESULT=$?
if [ $RESULT -ne 0 ]; then
    echo "❌ Commit blocked by API Key Guardian (secrets detected)."
    exit 1
fi

exit 0
"""

HOOK_SCRIPT_BAT = """@echo off
REM API Key Guardian pre-commit hook (Windows)
leaklock
IF %ERRORLEVEL% NEQ 0 (
  echo ❌ Commit blocked by API Key Guardian (secrets detected).
  EXIT /B 1
)
EXIT /B 0
"""

def install_hook():
    git_hooks = Path(".git/hooks")

    if not git_hooks.exists():
        print("⚠️  No .git directory found. Run this inside a Git repo.")
        return
    
    hook_path = git_hooks / "pre-commit"

    if "windows" in platform.system().lower():
        hook_path.write_text(HOOK_SCRIPT_BAT)
    else:
        hook_path.write_text(HOOK_SCRIPT_SH)
        os.chmod(hook_path, 0o775)
    
    print(f"✅ Installed pre-commit hook at {hook_path}")