#!/bin/python
#python program to remove variants between list of two values (eg. 123	321)
#argv[1] filter file 
#argv[2] vcf file 
#argv[3] chromosome
#argv[4] outfile
import sys


def main():
   between=[[]] 
   #Load in between line
   for line in open(sys.argv[1], 'r'):
      sline = line.split()
      if (sys.argv[3] == sline[0]):
         between.append([int(sline[1]), int(sline[2])])
   i=1
   iTop= len(between)
   outfile = open(sys.argv[4], "w")
   removed = open(sys.argv[4]+"del", "w")
   
   for line in open(sys.argv[2], 'r'): 
      if (i >= iTop): #If pass the betweener list, then no need to check if its inbetween
         outfile.write(line)
         continue
      if (line[0] == '#'): #Print out the header 
         outfile.write(line)
         continue
      sline = line.split()
      if (int(sline[1]) > between[i][0] ): #If the first betweener
         removed.write(line)
         if (int(sline[1]) > between[i][1]): #If it has gone out of the range of betweener
            print (str(i)+'/'+str(iTop)+'\t'+str(between[i])) #For progress, print something 
            i += 1 
            outfile.write(line)
            continue 
      outfile.write(line)
 

if __name__ == "__main__":
   main()
