import argparse
from app.core import main
from argparse import ArgumentParser
import sys
parser = ArgumentParser()
parser.add_argument("--inputfile", help="filename of the input file")
parser.add_argument("--outputfile", help="filename of the output file")
parser.add_argument("--bucketcount", help="buckercount number", type=int)
args = parser.parse_args()
main(inputfile = args.inputfile, outputfile = args.outputfile, bucketcount = args.bucketcount)