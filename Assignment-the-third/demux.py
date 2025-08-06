#!/usr/bin/env python

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
    parser.add_argument("-i", "--indexes",
                        help="Text file containing valid index sequences for this data set", type=str, required=True)
    parser.add_argument("-o", "--outputDir",
                        help="Directory to output FASTQ files in. Make sure to include concluding '/' character in path.", type=str, required=True)
    return parser.parse_args()

# Global variables
args = get_args()
numHopped: int = 0
numMatched: int = 0
numUnk: int = 0
indexPairs: dict = {} # Holds count of index pair occureneces. Key = Index1,Index2 : Value = number of occurences of that index pair


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
    seq = seq[::-1] # reverse sequence
    revComp: str = ""
    for char in seq:
        if char in complement: # This is a known base
            revComp += complement[char]
        else:
            revComp += char # This could be an N or some other char
    return revComp

def getValidIndexes() -> set:
    '''Generates a returns a set contain all index sequences in the command line argument "indexes" '''
    indexes: set = set()
    with open(args.indexes, "r") as fh:
        for lineNum,line in enumerate(fh):
            if lineNum == 0: # Skip header line
                continue
            else:
                indexes.add(line.strip("\n").split()[4])
    return indexes

def openFilesForWriting(indexes:set, outputDir:str) -> dict:
    ''' Creates and opens all output FASTQ files for writing. Returns a dict containing the files (key = <index>/hop/unk : value = R1.fastq, R2.fastq)'''
    newFiles = {}
    for index in indexes:
        R1 = open(outputDir+index+"_R1.fq", "w")
        R2 = open(outputDir+index+"_R2.fq", "w")
        newFiles[index] = R1, R2
    newFiles["hop"] = open(outputDir+"hopped_R1.fq", "w"), open(outputDir+"hopped_R2.fq","w")
    newFiles["unk"] = open(outputDir+"unknown_R1.fq", "w"), open(outputDir+"unknown_R2.fq","w")
    return newFiles

def main():
    global numHopped
    global numUnk
    global numMatched
    global indexPairs
    indexes: set = getValidIndexes()
    newFiles = openFilesForWriting(indexes,args.outputDir)
    with gzip.open(args.read1,"rt", encoding='utf-8') as r1, gzip.open(args.read2,"rt", encoding='utf-8') as r2, \
        gzip.open(args.read3,"rt", encoding='utf-8') as r3, gzip.open(args.read4,"rt", encoding='utf-8') as r4:
        while True:

            forwardRead = getNextRecord(r1)
            if forwardRead == "":
                break # EOF reached
            forwardIndex = getNextRecord(r2)
            reverseIndex = getNextRecord(r3) 
            reverseRead = getNextRecord(r4)
            # Now, split all the records by line
            forwardRead = forwardRead.split('\n')
            forwardIndex = forwardIndex.split('\n')
            reverseIndex = reverseIndex.split('\n')
            # Convert read 3 sequence line to reverse complement due to Illumina chemistry of read 3
            reverseIndex[1] = reverseComplement(reverseIndex[1]) 
            reverseRead = reverseRead.split('\n')

            if reverseIndex[1] not in indexes or forwardIndex[1] not in indexes: # Index sequence contains unknown base
                numUnk += 1
                indexPair = forwardIndex[1]+"-"+reverseIndex[1]
                forwardHeader = forwardRead[0]+"_"+indexPair
                reverseHeader = reverseRead[0]+"_"+indexPair
                R1, R2 = newFiles["unk"]
                R1.write(forwardHeader+"\n")
                R1.write(forwardRead[1]+"\n+\n"+forwardRead[3]+"\n")
                R2.write(reverseHeader+"\n")
                R2.write(reverseRead[1]+"\n+\n"+reverseRead[3]+"\n")
            elif reverseIndex[1] == forwardIndex[1]: # Indexes match
                numMatched += 1
                indexPair = forwardIndex[1]+"-"+reverseIndex[1]
                forwardHeader = forwardRead[0]+"_"+indexPair
                reverseHeader = reverseRead[0]+"_"+indexPair
                R1, R2 = newFiles[forwardIndex[1]]
                R1.write(forwardHeader+"\n")
                R1.write(forwardRead[1]+"\n+\n"+forwardRead[3]+"\n")
                R2.write(reverseHeader+"\n")
                R2.write(reverseRead[1]+"\n+\n"+reverseRead[3]+"\n")
                if (forwardIndex[1],reverseIndex[1]) in indexPairs:
                    indexPairs[forwardIndex[1],reverseIndex[1]] += 1
                else:
                    indexPairs[forwardIndex[1],reverseIndex[1]] = 1
            else: # Index hopping must have occured
                numHopped += 1
                indexPair = forwardIndex[1]+"-"+reverseIndex[1]
                forwardHeader = forwardRead[0]+"_"+indexPair
                reverseHeader = reverseRead[0]+"_"+indexPair
                R1, R2 = newFiles["hop"]
                R1.write(forwardHeader+"\n")
                R1.write(forwardRead[1]+"\n+\n"+forwardRead[3]+"\n")
                R2.write(reverseHeader+"\n")
                R2.write(reverseRead[1]+"\n+\n"+reverseRead[3]+"\n")
                if (forwardIndex[1],reverseIndex[1]) in indexPairs:
                    indexPairs[forwardIndex[1],reverseIndex[1]] += 1
                else:
                    indexPairs[forwardIndex[1],reverseIndex[1]] = 1
    print(f"{numUnk} read-pairs had unknown index-pairs.")
    print(f"{numHopped} read-pairs had hopped index-pairs.")
    print(f"{numMatched} read-pairs matched!")



if __name__ == "__main__":
    main()
