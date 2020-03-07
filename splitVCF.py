#!/usr/bin/env/python
#Will split a vcf file based on their CHR
#argv[1] vcf file 
#argv[2] output dir
import sys

def main():
    print('START')
    chrom = ""
    ofile = ""
    header = "" 
    ifile = open(sys.argv[1], "r") 
    for line in ifile:
        #sline = line.split('\t') #No need to split I hope (can save time)  
        temp = line[0] + line[1]
        if (chrom != temp): #Check if chromosone has changed 
            print("Starting on chromosone: " + temp)
            if(ofile != ""): #Can't  close an unopen file first time
                file.close()
            elif(line[0] == "#"): #Get header 
                header = header + line
                continue
            chrom = temp
            ofile = sys.argv[2] + "chr" + chrom + ".vcf"
            file = open(ofile, "w")
            file.write(header) #Add header to each file
        file.write(line) #Write current line

    print('END')
if __name__ == '__main__':
    main()
