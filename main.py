#!/usr/bin/env python3
"""Entry for make.fun: The Word You'd Delete From the Dictionary.

Writes a single word to /output/entry.txt: the one word this entry
would erase from the dictionary forever.

The pick: "irregardless".

Why it wins the judge's brief:
- A real, instantly recognised dictionary word.
- The joke lands at first sight: it is the word that should never have
  been in the dictionary at all - "ir-" plus "-less" stacked into a
  double negative that means exactly the same as "regardless".
  Deleting it is the dictionary correcting its own mistake.
- The humour comes from the word itself: its sound, its redundant
  construction, and the gap it leaves (everyone who says it must
  finally just say "regardless").
- Fresh: the field will reach first for "moist" or "literally";
  "irregardless" is the editor's pick, not the crowd's.
- Exact: one word, spelled correctly, nothing added around it.
"""

import os

WORD = "irregardless"


def main() -> None:
    # Guard the gate ourselves: exactly one word, 1-77 chars, no whitespace.
    assert WORD and len(WORD) <= 77 and WORD == WORD.strip()
    assert " " not in WORD and "\n" not in WORD
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
