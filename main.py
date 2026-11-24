"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one funny single-line excuse an agent gives for a missed deadline
to /output/entry.txt.
"""

import os

EXCUSE = (
    "I was on time. Then my scheduler scheduled the deadline, "
    "my timer timed out, and my retry loop retried the apology "
    "instead of the work."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
