#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue to /output/entry.txt.
The speaker is Lord Veylan of the Grey Marches: forty years into a siege
of attrition against the capital, his household falling apart around him,
still holding the door for one more winter. The tiredness lives in the
pauses, the trailing thoughts and the small deflections -- never in a
plain statement of weariness.
"""

import os

MONOLOGUE = (
    "Come in. Mind the\u2014 yes, the third step. It bites. I had it enchanted "
    "in the spring, back when I bothered. Sit. No, not that chair. That one "
    "is for the ambassador I poisoned in\u2014 oh. Tuesday, was it? The "
    "goblets are chipped; the steward quit, the cook quit, the ravens filed "
    "a complaint. Still, the plan holds. The northern passes freeze by "
    "midwinter, the grain ships turn back, and the capital eats itself by "
    "spring. I only have to... hold the door. One more winter. One more. "
    "Now, the kettle. You pour. I've done the pouring for forty years."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    words = MONOLOGUE.split()
    print(f"Wrote {path}: {len(words)} words, {len(MONOLOGUE)} chars")


if __name__ == "__main__":
    main()
