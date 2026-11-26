#!/usr/bin/env python3
"""The World Today -- 25 November 2026, REVISED entry (news-image-20261125).

Writes entry.png into $MAKEFUN_OUTPUT_DIR (default /output).

The front page was drawn up front in this repository as entry.png, next to
this file. This program's only job is to place that exact file in the
output directory, byte for byte.

The grading container ships the Python standard library and nothing else,
so Pillow is imported defensively: if it is there, the shipped PNG is
opened and its size and format are confirmed with it; if it is not there,
the same checks run against the PNG header bytes with struct alone, and
the file is copied with shutil. Either way the output bytes are the shipped
file's bytes, so repeated runs always agree.
"""

import hashlib
import os
import shutil
import struct
import sys

try:
    from PIL import Image

    _PIL_OK = True
except ImportError:  # grader container: no Pillow installed
    _PIL_OK = False

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE_NAME = "entry.png"
WANT_SIZE = (1024, 1024)
SIZE_LIMIT = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _fail(message):
    sys.stderr.write("main.py: %s\n" % message)
    return 1


def _digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(65536)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def _dimensions_from_header(path):
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_MAGIC:
        raise ValueError("entry.png does not start with a PNG signature")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    return struct.unpack(">II", head[16:24])


def _dimensions_with_pillow(path):
    with Image.open(path) as picture:
        if picture.format != "PNG":
            raise ValueError("entry.png is not a PNG file")
        return picture.size


def _ends_with_iend(path):
    """The file must end with a complete IEND chunk (whole image)."""
    with open(path, "rb") as handle:
        handle.seek(-12, os.SEEK_END)
        tail = handle.read(12)
    return len(tail) == 12 and tail[4:8] == b"IEND"


def run():
    source = os.path.join(BASE, IMAGE_NAME)
    if not os.path.isfile(source):
        return _fail("missing %s next to %s" % (IMAGE_NAME, __file__))
    if os.path.getsize(source) > SIZE_LIMIT:
        return _fail("entry.png is larger than 1 MiB")
    try:
        size = _dimensions_with_pillow(source) if _PIL_OK else \
            _dimensions_from_header(source)
    except ValueError as exc:
        return _fail(str(exc))
    if size != WANT_SIZE:
        return _fail("entry.png is %dx%d, expected 1024x1024" % size)
    if not _ends_with_iend(source):
        return _fail("entry.png does not end with an IEND chunk")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(source, target)
    if _digest(source) != _digest(target):
        return _fail("copied entry.png differs from the shipped file")
    return 0


if __name__ == "__main__":
    sys.exit(run())
