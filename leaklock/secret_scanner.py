import re
import math
import sys
import subprocess
from typing import List


PATTERNS = {
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"gh[pousr]_[A-Za-z0-9]{36}",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9-]{10,48}",
}


def get_staged_files() -> List[str]:
    """
    Get the list of staged files in the Git repository.

    Uses `git diff --cached --name-only -z` to retrieve all files staged
    for commit, separated by null characters.

    Returns:
        List[str]: A list of staged file paths as UTF-8 strings.
    """

    out = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "-z"], text=False
    )

    return [p.decode("utf-8") for p in out.split(b"\x00") if p ]


def read_staged_files(path: str) -> str:
    """
    Read the contents of a staged file.

    Uses `git show :<path>` to fetch the staged version of the file.

    Args:
        path (str): Path of the file to read from the Git index.

    Returns:
        str: The file contents as a string. Returns an empty string
             if the file cannot be read (e.g., if it was deleted).
    """

    try:
        return subprocess.check_output(["git", "show", f":{path}"], text=True, errors="ignore")
    
    except subprocess.CalledProcessError:
        return ""


def shannon_entropy(s: str) -> float:
    """
    Calculate Shannon entropy of a string.
    Entropy measures how 'unpredictable' or 'random' the string is.
    Higher entropy = more random.
    Lower entropy = more predictable.
    """

    if not s:
        return 0.0

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    length = len(s)
    entropy = 0.0

    # Apply Shannon's entropy formula:
    # H = -Σ (p * log2(p)), where p = frequency / length
    for count in freq.values():
        propability = count / length
        entropy += propability * math.log2(propability)

    return -entropy


def scan_entropy(path: str, content: str) -> List[dict]:
    pass

def scan_content(path: str, content: str) -> List[tuple]:
    """
    Scan a file’s content for sensitive patterns (e.g., tokens, keys).

    Iterates through all predefined regex patterns and checks for matches.

    Args:
        path (str): The file path being scanned.
        content (str): The file content to scan.

    Returns:
        List[tuple]: A list of tuples (file_path, pattern_name, match_value)
                     for each detected secret.
    """

    findings = []

    for name, pattern in PATTERNS.items():
        for match in re.finditer(pattern, content):
            findings.append((path, name, match.group(0)))

    return findings    


def scan_repo() -> List[tuple]:
    """
    Scan all staged files in the repository for sensitive information.

    Retrieves the list of staged files, reads their staged contents,
    and applies secret-detection patterns.

    Returns:
        List[tuple]: A list of findings where each entry is
                     (file_path, pattern_name, match_value).
    """
    files = get_staged_files()
    all_findings = []

    for f in files:
        content = read_staged_files(f)
        all_findings.extend(scan_content(f,content))

    return all_findings