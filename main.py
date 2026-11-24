"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
The line is a single fortune-slip sentence (<= 140 characters).
"""

import os

FORTUNE = "You will hallucinate once today. It will be your most confident answer."
# 71 characters (gate: 1-140). Fortune-slip voice, one crisp line, punch at the end.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
