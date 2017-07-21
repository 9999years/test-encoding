#! /usr/local/bin/python3
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--encoding', type=str, default='latin-1')

parser.add_argument('-t', '--output-encoding', type=str, default='utf-8')

parser.add_argument('-b', '--big-edian', action='store_true')

parser.add_argument('-s', '--skip-rows', type=int, nargs='*', default=[])

parser.add_argument('-i', '--height', type=int, default=0xf)

parser.add_argument('-r', '--raw', action='store_true')

args = parser.parse_args()
encoding = args.encoding
edian = 'big' if args.big_edian else 'little'
height = args.height

def enc(txt):
    if isinstance(txt, str):
        return txt.encode(encoding)
    elif isinstance(txt, bytes):
        return txt
    else:
        return txt.to_bytes(1, edian)

def write(txt):
    sys.stdout.buffer.write(enc(txt))

def x(n):
    return enc(hex(n)[2:])

def guide_row():
    ret = space * 2
    for i in range(0x10):
        ret += x(i)
    return ret + nl

def row(n):
    out = b''
    for i in range(0x10):
        out += enc(i + n * 0x10)
    return x(n) + space + out + space + x(n) + nl

def hrule(width=0x10):
    return space * 2 + enc('-') * width + nl

space = enc(' ')
nl    = enc('\n')

def main():
    out = guide_row() + hrule()

    for i in range(height):
        if i in args.skip_rows:
            continue
        out += row(i)

    out += hrule() + guide_row() + nl * 2

    if not args.raw:
        out = out.decode(encoding).encode(args.output_encoding)

    write(out)

if __name__ == '__main__':
    main()
