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
    - To determine Phred encoding, did this command and saw "#" which only exists in Phred +33:
      ```
      zcat 1294_S1_L008_R1_001.fastq.gz | head -4
      ```

 | File    | Data | Read Length |
| -------- | ------- | ------- | 
| 1294_S1_L008_R1_001.fastq.gz  | Read 1    | 101
| 1294_S1_L008_R4_001.fastq.gz | Read 2     | 101
| 1294_S1_L008_R2_001.fastq.gz    | Index 1    | 8
| 1294_S1_L008_R3_001.fastq.gz    | Index 2    | 8




