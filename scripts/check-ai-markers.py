#!/usr/bin/env python3
"""commit-msg hook: reject commits carrying AI-tool attribution markers."""
import re
import sys

# Literal markers only -- attribution trailers, tool self-references,
# disclaimers. Prose style/tone isn't reliably regex-detectable, so this
# is a backstop for mechanical leaks, not a style checker.
PATTERNS = [
    r"co-authored-by:.*(claude|anthropic|copilot|chatgpt|openai|gpt-\d|gemini|cursor|codeium|cody|tabnine|windsurf)",
    r"generated (with|by|using)\s+(claude|copilot|chatgpt|gpt|gemini|cursor|\bai\b)",
    r"\bas an ai\b",
    r"\[(claude code|chatgpt|github copilot|cursor)\]",
    r"\U0001F916",  # robot emoji
]


def main() -> int:
    msg = open(sys.argv[1]).read().lower()
    for pattern in PATTERNS:
        if re.search(pattern, msg, re.IGNORECASE):
            print("\nCOMMIT REJECTED: AI-tool marker in commit message.")
            print(f"Matched pattern: {pattern}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
