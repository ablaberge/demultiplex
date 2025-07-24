Definition of Problem:


The algorithm that we are seeking to write is a demultiplexing algorithm for sequencing data. This means that our algorithm should read through a group of FASTQ files (four, one for each read), and seperate each sample's records into their own file. We will do this using the indexes contained in Read 2 and Read 3 files. Index pairs that do no match for any given record will be added to one of two "index hopped" FASTQs (based on R1/R4). Additonally, any reads with undetermined bases should be directed to an second pair of FASTQs. We should also report how many read pairs were classified as paired, index hopped, or undertermined at the end. One further goal is to report how many times each index was swapped (i.e. i2 was swapped with i10 a total for 4 times). 
  
