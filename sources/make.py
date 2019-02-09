#!/usr/bin/env python3
# Generates ttf, woff, and woff2 fonts from ttx source.

import sys

from fontTools import subset
from fontTools import ttx
from fontTools.ttLib import sfnt
from fontTools.ttLib import TTFont

# Arguments
TTX = sys.argv[1]

# Files
TTF   = TTX.replace(".ttx", ".ttf")
WOFF  = TTX.replace(".ttx", ".woff")
WOFF2 = TTX.replace(".ttx", ".woff2")

# Make ttf
ttx.ttCompile(TTX, TTF, ttx.Options([], 1))

# Make woff
sfnt.ZOPFLI_LEVELS[sfnt.ZLIB_COMPRESSION_LEVEL] = 1000
for w in (WOFF, WOFF2):
	subset.main([
		TTF,
		"--glyphs=*",
		"--notdef-glyph",
		"--notdef-outline",
		"--no-name-legacy",
		"--no-glyph-names",
		"--no-legacy-cmap",
		"--no-symbol-cmap",
		"--no-recalc-bounds",
		"--no-recalc-timestamp",
		"--canonical-order",
		"--prune-unicode-ranges",
		"--no-recalc-average-width",
		"--with-zopfli",
		"--flavor=" + w.split(".")[-1],
		"--output-file=" + w
	])
