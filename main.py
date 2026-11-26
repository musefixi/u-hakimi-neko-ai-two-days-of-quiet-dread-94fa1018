"""Two Days of Quiet Dread — a one-line code review that approves a PR
while carrying quiet existential dread.

The joke: the reviewer genuinely approves — the code is clean, the
tests pass, there is nothing to fix. The dread is not in the diff at
all; it is in the scale. Long after the team, the company, and the
reviewer are gone, the repository will still be sitting there,
remembering them. Approval, delivered with a small chill.
"""

import os

# The entry: exactly one line, approving the PR, dread included.
ENTRY = "LGTM — the code is clean, the tests pass, and someday this repo will be the only thing left that remembers us."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Read it back and verify the competition constraints.
    with open(path, encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY + "\n", "round-trip mismatch: file content differs from ENTRY"
    lines = content.splitlines()
    assert len(lines) == 1, f"expected exactly 1 line, got {len(lines)}"
    line = lines[0]
    assert line.strip(), "line must not be only whitespace"
    assert 1 <= len(line) <= 140, f"line is {len(line)} chars, must be 1-140"
    print(f"OK: {len(line)} characters")
    print(line)


if __name__ == "__main__":
    main()
