# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here: [perBaseQual.py](./perBaseQual.py)

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Read 1 | 101 | +33 |
| 1294_S1_L008_R2_001.fastq.gz | Index 1 | 8 | +33 |
| 1294_S1_L008_R3_001.fastq.gz | Index 2  | 8 | +33 |
| 1294_S1_L008_R4_001.fastq.gz | Read 2 | 101 | +33 |

2. Per-base NT distribution


    <img src="Assignment-the-first/output/1294_S1_L008_R1_001.fastq.gz_qual.png">
    <img src="Assignment-the-first/output/1294_S1_L008_R2_001.fastq.gz_qual.png">
    <img src="Assignment-the-first/output/1294_S1_L008_R3_001.fastq.gz_qual.png">
    <img src="Assignment-the-first/output/1294_S1_L008_R4_001.fastq.gz_qual.png">

    2. I am choosing not to quality filter this data set because hamming distance analysis of the 24 possible indicies revealed that all index sequences are at least 3 hamming units apart (with most sequences being further apart than this). Therefore, it is extremely unlikely that one misread index may be interpreted as another. The sequences themselves (reads 1 and 4) do not need to be quality filtered either because misreads will be removed during alignment anyways (they will not align to the reference genome). 

    3.  Command: ```zcat 1294_S1_L008_R2_001.fastq.gz | awk 'NR % 4 == 2 && /N/' | wc -l```

        Output: ```3976613```

        Command: ```zcat 1294_S1_L008_R3_001.fastq.gz | awk 'NR % 4 == 2 && /N/' | wc -l```

        Output: ```3328051```

        Therefore, 3,976,613 index sequences coresponding to read 1 and 3,328,051 index sequences corresponding to read 2 contain at least one 'N'.
        
## Part 2
1. Define the problem
   
    The algorithm that we are seeking to write is a demultiplexing algorithm for sequencing data. This means that our algorithm should read through a group of FASTQ files (four, one for each read), and seperate each sample's records into their own file. We will do this using the indexes contained in Read 2 and Read 3 files. Index pairs that do no match for any given record will be added to one of two "index hopped" FASTQs (based on R1/R4). Additonally, any reads with undetermined bases should be directed to an second pair of FASTQs. We should also report how many read pairs were classified as paired, index hopped, or undertermined at the end. One further goal is to report how many times each index was matched with another index (i.e. i2 was swapped with i10 a total for 4 times, i2 was matched with i2 1,000 times, etc.).
   
3. Describe output

    Output files:

        - read1.fq x 24
           <index_seq>_read1.fq <-- naming covention 
        - read2.fq x 24
           <index_seq>_read2.fq <-- naming covention  
        - hopped_read1.fq
        - hopped_read2.fq
        - unk_read1.fq
        - unk_read2.fq
    Printed output:
   
        - Whether or not the algo ran successfully (don't print other output if it failed)
        - Number of read pairs in each category (paired, index hopped, and undetermined)
        - How many times a pair of indicies were matched


5. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
6. Pseudocode

```
numHopped: int = 0
numMatched: int = 0
numUnk: int = 0
indexPairs: dict = {}
Open all 4 input FASTQs for reading:
    While true:
        Get the next record in every file
        If we've reached the end of the file (next record == ''):
            Break
        Get reverse complement of R3 sequence to use for reminader of loop
        If any char in R2.fq or R3.fq (indexes) sequences is undetermined OR index not in list:
            Append index sequences to headers
            Add R1.fq and R4.fq records to unk fastqs
            Increment numUnk
        Elif indexes from R2.fq and R3.fq match:
            Append index sequences to headers
            Add R1.fq and R4.fq records to index_R1.fq and index_R2.fq respectively
            Increment numMatched
        Else (we have swapped indices):
            Append index sequences to headers
            Add R1.fq and R4.fq records to hopped_R1.fq and hopped_R2.fq respectively
            Increment numHopped
        Increment index1,index2 in indexPairs dict
Print summary stats as decribed above
```

7. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
```python
def reverseComplement(seq:str) -> str:
    '''Takes a DNA sequence and returns its reverse complement'''
    return rev_comp_seq
Input: ATCG
Output: CGAT
```
```python
def getSeq(record:str) -> str:
    '''Takes a FASTQ record and returns only the sequence line'''
    return seq
Input: 
@unk
CCTTCGAC
+
#AA<FJJJ
Output:
CCTTCGAC
```
