#! /bin/bash


#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --job-name=demux_today            #optional: job name
#SBATCH --output=LOG/demux_%j.out       #optional: file to store stdout from job, %j adds the assigned jobID
#SBATCH --error=LOG/demux_%j.err        #optional: file to store stderr from job, %j adds the assigned jobID

./demux.py -r1 "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz" \
    -r2 "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz" \
    -r3 "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz" \
    -r4 "/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz" \
    -i "/projects/bgmp/shared/2017_sequencing/indexes.txt" \
    -o "/projects/bgmp/alaberge/demultiplex/Assignment-the-third/output/"

# ./demux.py -r1 "/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R1.fq.gz" \
#     -r2 "/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R2.fq.gz" \
#     -r3 "//projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R3.fq.gz" \
#     -r4 "/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_R4.fq.gz" \
#     -i "/projects/bgmp/alaberge/demultiplex/TEST-input_FASTQ/test_indexes.txt" \
#     -o "/projects/bgmp/alaberge/demultiplex/Assignment-the-third/output/"