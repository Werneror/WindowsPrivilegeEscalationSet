"""
Title: echo_translate.py
Date: September 30, 2019
Author: Werner <me@werner.wiki>
Homepage: https://blog.werner.wiki/
Verify: Windows 10, FreeBSD 9, Debian 4.17.8

Use the echo command and copy and paste to transfer the text file.

Usage:
    python echo_translate.py <input.txt> <output_path> [<command>]
"""

import os
import sys

def print_usage():
    print("""Usage:
    python echo_translate.py <input.txt> <output_path> [<command>]
    """)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()
    elif not os.path.exists(sys.argv[1]):
        print("The file `{}` does not exists.".format(sys.argv[1]))
    else:
        with open(sys.argv[1]) as f:
            for i in f:
                print(r'echo "{}" >> {}'.format(i.replace('"', r'\"').replace('\n', '').replace('\r', ''), sys.argv[2]))
        if len(sys.argv) > 3:
            print(' '.join(sys.argv[3:]))

