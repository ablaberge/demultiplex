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
- Seemingly successfully generated output for the assignment! Run details below:
    - Took ~50 minutes to run with the slurm settings in runDemux.sh
    - Empty error log: /projects/bgmp/alaberge/demultiplex/Assignment-the-third/LOG/demux_36906348.err
    - Output log: /projects/bgmp/alaberge/demultiplex/Assignment-the-third/LOG/demux_36906348.out
        ```
        30783962 read-pairs had unknown index-pairs.
        707740 read-pairs had hopped index-pairs.
        331755033 read-pairs matched!
        ```
    - Uncompressed output files are ~184 Gb total

  
| Sample | Percentage of Matched Reads | Index     |
|--------|-----------------------------|-----------|
| 1      | 2.44736%                     | GTAGCGTA  |
| 2      | 1.68949%                     | CGATCGAT  |
| 3      | 1.98553%                     | GATCAAGG  |
| 4      | 2.67427%                     | AACAGCGA  |
| 6      | 3.20406%                     | TAGCCATG  |
| 7      | 1.5267%                      | CGGTAATC  |
| 8      | 10.5428%                     | CTCTGGAT  |
| 10     | 23.0181%                     | TACCGGAT  |
| 11     | 5.22435%                     | CTAGCTCA  |
| 14     | 1.2634%                      | CACTTCAC  |
| 15     | 2.23555%                     | GCTACTCT  |
| 16     | 2.39419%                     | ACGATCAG  |
| 17     | 3.37125%                     | TATGGCAC  |
| 19     | 4.74236%                     | TGTTCCGT  |
| 21     | 2.66169%                     | GTCCTAAG  |
| 22     | 1.1615%                      | TCGACAAG  |
| 23     | 12.6883%                     | TCTTCGAC  |
| 24     | 3.04065%                     | ATCATGCG  |
| 27     | 2.07611%                     | ATCGTGGT  |
| 28     | 3.53922%                     | TCGAGAGT  |
| 29     | 1.38999%                     | TCGGATTC  |
| 31     | 1.09752%                     | GATCTTGC  |
| 32     | 3.41119%                     | AGAGTCCA  |
| 34     | 2.61433%                     | AGGATAGC  |
