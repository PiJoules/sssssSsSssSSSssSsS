#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script for generating the encoding.
"""

from __future__ import print_function

import sys
import string
import itertools
import json


def main():
    encoding = {
        "p": "sss",
        "y": "ssS",
        "t": "sSs",
        "h": "sSS",
        "o": "Sss",
        "n": "SsS",
    }
    chars = set(string.ascii_uppercase +
                string.ascii_lowercase +
                string.digits)
    chars -= set(encoding)

    products = set(map(lambda x: "".join(x),
                       itertools.product("sS5$", repeat=3)))
    products -= set(encoding.values())

    for c in chars:
        assert c not in encoding
        encoding[c] = products.pop()

    print(json.dumps(encoding, indent=4))

    return 0


if __name__ == "__main__":
    sys.exit(main())
