#!/bin/bash
#Converts the plink file into VCF
#Need to have plink
#argv[1] in bfile
#argv[2] output

plink --allow-extra-chr --allow-no-sex --bfile ${1} --keep-allele-order --out ${2} --recode vcf
