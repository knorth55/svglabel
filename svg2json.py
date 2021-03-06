#!/usr/bin/python

import argparse
from svglabel import svg2json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('svgfile')
    parser.add_argument('imfile')
    parser.add_argument('-o', '--outfile')
    parser.add_argument('--segments', type=int, default=5)
    args = parser.parse_args()

    svg2json(args.svgfile,
             args.imfile,
             outfile=args.outfile,
             segments=args.segments,
    )
