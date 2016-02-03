#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function

import sys
import subprocess
import tempfile

# Gener8ed using mapping.py
ENCODING = {
    "1": "55$",
    "0": "5sS",
    "3": "S5$",
    "2": "$SS",
    "5": "s$s",
    "4": "ss5",
    "7": "5SS",
    "6": "S5s",
    "9": "$Ss",
    "8": "$ss",
    "A": "S55",
    "C": "5S$",
    "B": "SSS",
    "E": "5$$",
    "D": "SS$",
    "G": "ss$",
    "F": "$5S",
    "I": "$S$",
    "H": "S$5",
    "K": "s5$",
    "J": "55S",
    "M": "s$S",
    "L": "$$s",
    "O": "5$5",
    "N": "5s5",
    "Q": "S$$",
    "P": "SS5",
    "S": "s55",
    "R": "55s",
    "U": "S5S",
    "T": "$s$",
    "W": "SSs",
    "V": "s$5",
    "Y": "S$S",
    "X": "5Ss",
    "Z": "$$5",
    "a": "$S5",
    "c": "5ss",
    "b": "$sS",
    "e": "s$$",
    "d": "$$S",
    "g": "5s$",
    "f": "s5S",
    "i": "sS$",
    "h": "sSS",
    "k": "555",
    "j": "5$S",
    "m": "$5s",
    "l": "5$s",
    "o": "Sss",
    "n": "SsS",
    "q": "S$s",
    "p": "sss",
    "s": "Ss5",
    "r": "$5$",
    "u": "5S5",
    "t": "sSs",
    "w": "sS5",
    "v": "s5s",
    "y": "ssS",
    "x": "$s5",
    "z": "Ss$"
}


def encode(s):
    """Encode a string."""
    return "".join(map(lambda x: ENCODING.get(x, x), s))


def encode_file(filename):
    """Encode a file. Return encoded text."""
    with open(filename, "r") as f:
        return "".join(map(lambda x: encode(x), f))


def decode(s):
    """Decode a string."""
    flipped = {v: k for k, v in ENCODING.iteritems()}
    result = ""
    i = 0
    while i < len(s) - 2:
        key = s[i:i + 3]
        if key in flipped:
            result += flipped.get(key)
            i += 3
        else:
            result += key
            i += 1
    return result


def decode_file(filename):
    """Decode a file. Return decoded text."""
    with open(filename, "r") as f:
        return "".join(map(lambda x: decode(x), f))


def get_args():
    """Parse cmd line args."""
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Run python code")
    parser.add_argument("filename", help="Python file to run.")
    parser.add_argument("--python-decode", default=False,
                        action="store_true",
                        help="Just decode the python file.")
    parser.add_argument("--python-encode", default=False,
                        action="store_true",
                        help="Just encode the python file.")

    return parser.parse_args()


def parse_args():
    args = sys.argv[1:]

    filename = args[0]
    args = args[1:]

    python_decode = "--python-decode" in args
    if python_decode:
        args.remove("--python-decode")

    python_encode = "--python-encode" in args
    if python_encode:
        args.remove("--python-encode")

    return {
        "filename": filename,
        "python_decode": python_decode,
        "python_encode": python_encode,
        "extra": args
    }


def main():
    # args = get_args()
    args = parse_args()
    print(args)
    filename = args["filename"]

    if args["python_decode"]:
        pass
    elif args["python_encode"]:
        pass
    else:
        decoded = decode_file(filename)
        with tempfile.NamedTemporaryFile(suffix=".py") as tmpf:
            tmpf.write(decoded)
            print(subprocess.check_output(
                  "python {} {}".format(tmpf.name, args["extra"]),
                  shell=True))

    return 0


if __name__ == "__main__":
    sys.exit(main())
