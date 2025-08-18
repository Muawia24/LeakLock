import sys
from secret_scanner import scan_repo
from installer import install_hook

def main ():
    """
    Handles scan and install commands.
    """
    if sys.argv > 1 and sys.argv[1] == "install":
        install_hook()
        return
    
    print("🔍 Scanning staged files for secrets...")
    issues = scan_repo()

    if issues:
        print("Secrets detected:")
        for issue in issues:
            print("-", issue)

        sys.exit(1)
        
    else:
        print("No secrets found.")

        sys.exit(0)