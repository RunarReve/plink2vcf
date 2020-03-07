# plink2vcf
Small workflow I used to turn plink files (.bam, .fam, .bim) to vcf files.

## plink2vcf.sh
The main script that converts
Innput:
  1: bfile to convert (like any other plink command) 
  2: output 

## splitVCF.sh
Sometimes it can be easier to work with VCF if they are separated by chromosome 
Innput:
  1  VCF to split
  2  output directory (will output as ${2}CHR@.vcf
All outputs with single digits chromosome will have a white space in it's name, due to speed

## VCFrmVar
Remove variants from a splitted vcf 

