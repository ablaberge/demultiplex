# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Read 1 | 101 | +33 |
| 1294_S1_L008_R2_001.fastq.gz | Index 1 | 8 | +33 |
| 1294_S1_L008_R3_001.fastq.gz | Index 2  | 8 | +33 |
| 1294_S1_L008_R4_001.fastq.gz | Read 2 | 101 | +33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. **YOUR ANSWER HERE**
    3. **YOUR ANSWER HERE**
    
## Part 2
1. Define the problem
   
    The algorithm that we are seeking to write is a demultiplexing algorithm for sequencing data. This means that our algorithm should read through a group of FASTQ files (four, one for each read), and seperate each sample's records into their own file. We will do this using the indexes contained in Read 2 and Read 3 files. Index pairs that do no match for any given record will be added to one of two "index hopped" FASTQs (based on R1/R4). Additonally, any reads with undetermined bases should be directed to an second pair of FASTQs. We should also report how many read pairs were classified as paired, index hopped, or undertermined at the end. One further goal is to report how many times each index was matched with another index (i.e. i2 was swapped with i10 a total for 4 times, i2 was matched with i2 1,000 times, etc.).
   
3. Describe output

    Output files:

        - read1.fq x 24
           <index>_read1.fq <-- naming covention 
        - read2.fq x 24
           <index>_read2.fq <-- naming covention  
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
7. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
