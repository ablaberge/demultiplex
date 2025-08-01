#! /bin/bash


#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp                  #REQUIRED: which partition to use
#SBATCH --cpus-per-task=8                 #optional: number of cpus, default is 1
#SBATCH --job-name=perBaseQual_today            #optional: job name
#SBATCH --output=LOG/perBaseQual_%j.out       #optional: file to store stdout from job, %j adds the assigned jobID
#SBATCH --error=LOG/perBaseQual_%j.err        #optional: file to store stderr from job, %j adds the assigned jobID

./perBaseQual.py