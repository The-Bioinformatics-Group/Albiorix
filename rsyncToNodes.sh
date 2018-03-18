#!/bin/bash

# Actinopterygia
rsync -hav Actinopterygia root@compute-0-1:/db/
rsync -hav Actinopterygia root@compute-0-3:/db/
rsync -hav Actinopterygia root@compute-0-5:/db/
rsync -hav Actinopterygia root@compute-0-7:/db/
#rsync -hav Actinopterygia root@compute-0-8:/db/
#rsync -hav Actinopterygia root@compute-0-9:/db/

# nt
rsync -hav nt.* root@compute-0-1:/db/
rsync -hav nt.* root@compute-0-3:/db/
rsync -hav nt.* root@compute-0-5:/db/
rsync -hav nt.* root@compute-0-7:/db/
rsync -hav nt.* root@compute-0-8:/db/
rsync -hav nt.* root@compute-0-9:/db/

# nr
rsync -hav nr.* root@compute-0-1:/db/
rsync -hav nr.* root@compute-0-3:/db/
rsync -hav nr.* root@compute-0-5:/db/
rsync -hav nr.* root@compute-0-7:/db/
rsync -hav nr.* root@compute-0-8:/db/
rsync -hav nr.* root@compute-0-9:/db/

# Prokka
rsync -hav prokka root@compute-0-1:/db/
rsync -hav prokka root@compute-0-3:/db/
rsync -hav prokka root@compute-0-5:/db/
rsync -hav prokka root@compute-0-7:/db/
rsync -hav prokka root@compute-0-8:/db/
rsync -hav prokka root@compute-0-9:/db/

# trinotate
rsync -hav trinotatedbs root@compute-0-1:/db/
rsync -hav trinotatedbs root@compute-0-3:/db/
rsync -hav trinotatedbs root@compute-0-5:/db/
rsync -hav trinotatedbs root@compute-0-7:/db/

# inhouse genome sequences
rsync -hav inhouse root@compute-0-1:/db/
rsync -hav inhouse root@compute-0-3:/db/
rsync -hav inhouse root@compute-0-5:/db/
rsync -hav inhouse root@compute-0-7:/db/

# BUSCO
rsync -hav busco_dbs root@compute-0-1:/db/
rsync -hav busco_dbs root@compute-0-3:/db/
rsync -hav busco_dbs root@compute-0-5:/db/
rsync -hav busco_dbs root@compute-0-7:/db/
rsync -hav busco_dbs root@compute-0-8:/db/
rsync -hav busco_dbs root@compute-0-9:/db/

# maker
rsync -hav makerdbs root@compute-0-1:/db/
rsync -hav makerdbs root@compute-0-3:/db/
rsync -hav makerdbs root@compute-0-5:/db/
rsync -hav makerdbs root@compute-0-7:/db/
#rsync -hav makerdbs root@compute-0-8:/db/
#rsync -hav makerdbs root@compute-0-9:/db/

# Bowtie2
rsync -hav bowtie2 root@compute-0-1:/db/
rsync -hav bowtie2 root@compute-0-3:/db/
rsync -hav bowtie2 root@compute-0-5:/db/
rsync -hav bowtie2 root@compute-0-7:/db/

# Kraken
rsync -hav kraken root@compute-0-1:/db/
rsync -hav kraken root@compute-0-3:/db/
rsync -hav kraken root@compute-0-5:/db/
rsync -hav kraken root@compute-0-7:/db/

# taxonomy
rsync -hav taxonomy root@compute-0-1:/db/
rsync -hav taxonomy root@compute-0-3:/db/
rsync -hav taxonomy root@compute-0-5:/db/
rsync -hav taxonomy root@compute-0-7:/db/
rsync -hav taxonomy root@compute-0-8:/db/
rsync -hav taxonomy root@compute-0-9:/db/
