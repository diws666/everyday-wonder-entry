#!/usr/bin/env python3
"""Writes one sentence of everyday wonder to /output/entry.txt."""

import os

# The one-sentence entry: exactly 117 characters.
WONDER = (
    "The kettle clicks off exactly when the toast pops up, "
    "and for one second the whole kitchen feels like it was planned."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WONDER)
