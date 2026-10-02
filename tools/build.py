"""Build the playbook page: inline the workbook data into src/playbook.html.

Usage: python3 tools/build.py "Diamond Pet foods - Revised.xlsx"
Writes diamond-playbook.html at the repo root.
"""
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = subprocess.run([sys.executable, str(root / "tools/extract_data.py"), sys.argv[1]],
                      check=True, capture_output=True, text=True).stdout
data = json.dumps(json.loads(data), separators=(",", ":")).replace("</", "<\\/")
page = (root / "src/playbook.html").read_text().replace("/*DATA*/", data)
(root / "diamond-playbook.html").write_text(page)
print("wrote diamond-playbook.html", len(page), "bytes")
