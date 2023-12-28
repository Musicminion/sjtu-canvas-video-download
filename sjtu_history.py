import json
import os
import sys


history = []

history_filename = os.path.join(
    os.path.dirname(sys.argv[0]), "history.json"
)

try:
    with open(history_filename, encoding="utf-8") as f:
        history = json.load(f)
except Exception:
    pass


def save_history():
    with open(history_filename, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
