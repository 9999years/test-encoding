#! /usr/local/bin/python3 -u

import testencoding as enc
import argparse

parser = argparse.ArgumentParser()

# https://stackoverflow.com/a/25513044/5719760
def aint(x):
    return int(x, 0)

parser.add_argument('pages', type=str, nargs='+')

def parse_range(txt):
    dash = txt.index('-')
    start = txt[:dash]
    end = txt[dash + 1:]

    start = 0x00 if start == '' else aint(start)
    end   = 0xff if end   == '' else aint(end)

    return [x for x in range(start, end + 1)]

def gen_pages(args):
    pages = []
    for a in args.pages:
        if '-' in a:
            # parse as a range
            pages.extend(parse_range(a))
        else:
            # parse as an int
            pages.append(aint(a))
    return pages

pages = gen_pages(parser.parse_args())

msg = b''

# first 0x00..0x7f are identical across all codepages
skips = [x for x in range(8)]

prefix = enc.enc('  codepage 0x')

rule = enc.enc('+') * 32

for i in pages:
    msg += (
        prefix
        + enc.x(i)
        + enc.enc(f' = {i}')
        + enc.nl
        + b'\x1b\x74'
        + enc.enc(i)
    )
    enc.write(msg)
    enc.cp(raw=True, skip_rows=skips)
    msg = rule + enc.nl

enc.write(enc.nl * 3)
