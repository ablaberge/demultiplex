#!/usr/bin/env python

import bioinfo
import matplotlib.pyplot as plt
import gzip
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Program to demultiplex sequencing data given the four raw FASTQs.")
    parser.add_argument("-r1", "--read1",
                        help="Read 1 FASTQ file for analysis (should contain forward reads)", type=str, required=True)
    parser.add_argument("-r2", "--read2",
                        help="Read 2 FASTQ file for analysis (should contain index sequences for forward reads)", type=str, required=True)
    parser.add_argument("-r3", "--read3",
                        help="Read 3 FASTQ file for analysis (should contain index sequences for reverse reads)", type=str, required=True)
    parser.add_argument("-r4", "--read4",
                        help="Read 4 FASTQ file for analysis (should contain reverse reads)", type=str, required=True)
    return parser.parse_args()

args = get_args()

numHopped: int = 0
numMatched: int = 0
numUnk: int = 0
indexPairs: dict = {}

def main():
    with gzip.open(args.read1,"rt", encoding='utf-8') as r1, gzip.open(args.read2,"rt", encoding='utf-8') as r2, \
        gzip.open(args.read1,"rt", encoding='utf-8') as r3, gzip.open(args.read4,"rt", encoding='utf-8') as r4:
        while True:
            ForwardRead = getNextRecord(r1)
            if ForwardRead == "":
                break # EOF reached
            ForwardIndex = getNextRecord(r2)
            ReverseIndex = getNextRecord(r3) 
            ReverseRead = getNextRecord(r4)
            # Now, split all the records by line
            ForwardRead = ForwardRead.split('\n')
            ForwardIndex = ForwardIndex.split('\n')
            ReverseIndex = ReverseIndex.split('\n')
            # Convert read 3 sequence line to reverse complement due to Illumina chemistry of read 3
            ReverseIndex[1] = reverseComplement(ReverseIndex[1]) 
            ReverseRead = ReverseRead.split('\n')


def getNextRecord(file) -> str:
    '''Takes an already opened FASTQ file and returns the next record (next four lines)'''
    nextRecord:str = ""
    nextRecord += file.readline()
    nextRecord += file.readline()
    nextRecord += file.readline()
    nextRecord += file.readline()
    return nextRecord

        




def reverseComplement(seq:str) -> str:
    '''Takes a DNA sequence and returns its reverse complement'''
    complement: dict = {'A':'T', 'a':'t', 'T':'A', 't': 'a', 'C':'G', 'c':'g', 'G':'C', 'g':'c'}
    seq = seq[::-1] # Reverse sequence
    revComp: str = ""
    for char in seq:
        revComp =+ complement[char]
    return revComp


