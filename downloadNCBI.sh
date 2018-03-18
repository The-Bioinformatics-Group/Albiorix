#!/bin/bash

#wget -c ftp://ftp.ncbi.nlm.nih.gov/blast/db/nr*
#wget -c ftp://ftp.ncbi.nlm.nih.gov/blast/db/nt*

update_blastdb.pl --decompress nt
update_blastdb.pl --decompress nr
