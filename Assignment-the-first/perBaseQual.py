#!/usr/bin/env python

import bioinfo
import matplotlib.pyplot as plt
import gzip

output: str = "/projects/bgmp/alaberge/demultiplex/Assignment-the-first/output" 


def populate_list(file: str, readLength: int) -> tuple[dict, int]:
    """Populates a list with the sum of all quality scores in each corresponding read position"""
    qualList: dict = {} # key = read pos, value = summed qual scores @ that pos 
    line_num = 0
    with gzip.open(file,"rt", encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line_num % 4 == 3:
                for pos,char in enumerate(line):
                    if pos in qualList:
                        qualList[pos] += bioinfo.convert_phred(char)
                    else:
                        qualList[pos] = bioinfo.convert_phred(char)
            line_num += 1
    print(line_num-1)
    return qualList,line_num

def makeQualDist(file:str, readLength:int):
    qualList, numLines = populate_list(file, readLength)
    print("# Base Pair\tMean Quality Score")
    for key in qualList:
        qualList[key] = qualList[key]/numLines*4
        print(f"{key}\t{qualList[key]:.2f}")
    plt.scatter(list(qualList.keys()),list(qualList.values()))
    plt.xlabel("Position in Read")
    plt.ylabel("Mean Quality Score")
    filename = file.split('/')[len(file.split('/'))-1]
    plt.title(f"Mean Quality Scores of Reads in {filename}")
    plt.savefig(f"{output}/{filename}_qual.png")
    plt.cla()

# makeQualDist("/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R1.fq", 101)
# makeQualDist("/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R2.fq", 8)
# makeQualDist("/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz", 101)
makeQualDist("/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz", 8)
makeQualDist("/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz", 8)
makeQualDist("/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz", 101)
