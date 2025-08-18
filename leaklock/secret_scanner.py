import re
import sys
import subprocess
from typing import List


PATTERNS = {
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"gh[pousr]_[A-Za-z0-9]{36}",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9-]{10,48}",
}

def get_staged_files():
    pass

def read_staged_files(path: str) -> str:
    pass

def scan_content(path: str, content) -> List[str]:
    pass

def scan_repo():
    pass