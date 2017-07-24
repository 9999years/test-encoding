#! /usr/local/bin/python3 -u

import testencoding as enc
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('start', type=int, default=0x0)
parser.add_argument('end',   type=int, default=0xff)

args = parser.parse_args()

msg = b''

# first 0x00..0x7f are identical across all codepages
skips = [x for x in range(8)]

prefix = enc.enc('  codepage ')

rule = enc.enc('+') * 32

for i in range(args.start, args.end):
	msg += prefix + enc.x(i) + enc.nl + b'\x1b\x74' + enc.enc(i)
	enc.write(msg)
	enc.cp(raw=True, skip_rows=skips)
	msg = rule + enc.nl

enc.write(enc.nl * 3)
