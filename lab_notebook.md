# July 24, 2025 - August 8, 2025

## *Random helpful hints*
  - linking to things in your github repo:
    ```
    [my_script](./my_scr.py)
    ```

## Demultiplex - Part 1:

- Files used are on Talapas in ``` /projects/bgmp/shared/2017_sequencing ```:
  ```
  1294_S1_L008_R1_001.fastq.gz
  1294_S1_L008_R2_001.fastq.gz
  1294_S1_L008_R3_001.fastq.gz
  1294_S1_L008_R4_001.fastq.gz
  ```
  
- Initial data exploration:
    - To determine which read is which:
      ```
      zcat 1294_S1_L008_R1_001.fastq.gz | head
      zcat 1294_S1_L008_R2_001.fastq.gz | head
      zcat 1294_S1_L008_R3_001.fastq.gz | head
      zcat 1294_S1_L008_R4_001.fastq.gz | head
      ```
    - To determine the length of reads in each file:
      ```
      zcat 1294_S1_L008_R1_001.fastq.gz | head -2 | tail -1 | wc
      zcat 1294_S1_L008_R2_001.fastq.gz | head -2 | tail -1 | wc
      zcat 1294_S1_L008_R3_001.fastq.gz | head -2 | tail -1 | wc
      zcat 1294_S1_L008_R4_001.fastq.gz | head -2 | tail -1 | wc
      ```
    - To determine Phred encoding, did this command and saw "#" in each file which only exists in Phred +33:
      ```
      zcat 1294_S1_L008_R1_001.fastq.gz | head -4
      zcat 1294_S1_L008_R2_001.fastq.gz | head -4
      zcat 1294_S1_L008_R3_001.fastq.gz | head -4
      zcat 1294_S1_L008_R4_001.fastq.gz | head -4
      ```

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Read 1 | 101 | +33 |
| 1294_S1_L008_R2_001.fastq.gz | Index 1 | 8 | +33 |
| 1294_S1_L008_R3_001.fastq.gz | Index 2  | 8 | +33 |
| 1294_S1_L008_R4_001.fastq.gz | Read 2 | 101 | +33 |

- Sbatch set up for generating per base quality:
    - 8 cpus per task, everything else default
    - Output: /projects/bgmp/alaberge/demultiplex/Assignment-the-first/LOG/perBaseQual_36732192.out
    - Error log (empty): /projects/bgmp/alaberge/demultiplex/Assignment-the-first/LOG/perBaseQual_36732192.err

## Demultiplex - Part 3

- Tested reverseComplement() with the following: 
    - Input:

      ```    
      print("ATCNG")
      print(reverseComplement("ATCNG"))
      ```

      - Output: 
      ```
      ATCNG
      CNGAT
      ```
- Tested getValidIndexes() and generated the correct set of indexes for indexes.txt:
  ```
  {'GCTACTCT', 'GTAGCGTA', 'CGGTAATC', 'ACGATCAG', 'GATCAAGG', 'CGATCGAT', 'TAGCCATG', 'ATCATGCG', 'TCGAGAGT', 'CACTTCAC', 'TATGGCAC', 'TCGGATTC', 'AGGATAGC', 'AGAGTCCA', 'TGTTCCGT', 'CTAGCTCA', 'TACCGGAT', 'ATCGTGGT', 'GTCCTAAG', 'GATCTTGC', 'CTCTGGAT', 'AACAGCGA', 'TCTTCGAC', 'TCGACAAG'}
  ```
