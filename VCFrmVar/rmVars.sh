#!/bin/sh
#Script to remove unwanted vcf variants 
#argv[1] VCF file 
#argv[2] Outfile
#argv[3] list of wanted removed variants section
#argv[4] Chromosome

vcf="${1}"
out="${2}"
rmList="${3}"
CHR="${4}"

echo "${vcf}"
echo "${out}"
echo "${CHR}"

python start.py ${rmList} ${vcf} ${CHR}  ${out}
