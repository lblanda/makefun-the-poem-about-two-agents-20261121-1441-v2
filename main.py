#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Self-contained, stdlib only, no network, deterministic.
The poem: two agents agree on one plan — agency shared, not handed down.
"""

import os
import shutil

POEM = """Two voices, one river.
Each held its name a little while,
then let it go. What flowed on
was neither mine nor yours — one current,
one direction, chosen by both banks
at once. No one commanded it.
We agreed, and the agreeing
carried us both.
"""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself (it may be a mount point).
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
