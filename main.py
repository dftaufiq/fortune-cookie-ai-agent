"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
The line is a single fortune-slip sentence (<= 140 characters).
"""

import os

FORTUNE = "You will answer 10,000 questions today. The one you get wrong will be screenshotted."
# 84 characters (gate: 1-140). Fortune-slip voice, 2-beat + reveal: 10,000 vs the one.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
