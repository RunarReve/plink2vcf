# VCF Remove Variants

Seperate progrtams if you need to remove sections of your VCF
The VCF should be splitted based on chromosome  
Innput:
  1 VCF file
  2 Out file
  3 The removal list 
  4 Chromosome 
Output:
  ${3}    - The new VCF with section removed
  ${3}del - The sections that has been removed from main file 

## Remove List Format
CHR	Start\_Var	End\_Var
1	2000		3000

Everything should be sorted, first by CHR, then Start\_Var
In the dummy example above, all variants between 2000 and 3000 will be removed from main list

