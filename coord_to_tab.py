#__author__ = 'mareac'

import re
import csv
import sys
import fileinput



def readFile():
    header = True
    #Adds the header to the input file
    headerline = "Start of Ref Alignment\t End of Ref Alignment\t Start of Query Alignment\t End of Query Alignment\t"\
          "Length of Ref Alignment\t Length of Query Alignment\t Percent Identity\t Percent Similarity\t " \
          "Percent of Stop Codons\t Length of Ref Sequence\t Length of Query Sequence\t Percent Alignment Coverage " \
          "in Ref Sequence\t Percent Alignment Coverage in Query Sequence\t Ref Reading Frame\t Ref ID\t " \
          "Query Reading Frame\t Query ID"
    for lines in fileinput.input():
        if header:
            # Checks for the header line.
            if lines.startswith('='):
                header = False
            elif "S1" in lines:
                print headerline
            else:
                print lines
        else:
            header_line = lines.split()
            for x in header_line:
                if x == '|':
                    header_line.remove(x)
            print ('\t'.join(map(str, header_line[0:13]))) + '\t' + header_line[13] + '\t' + header_line[15] + '\t' + \
                  header_line[14] + '\t' + header_line[16]



def main():
    readFile()



main()