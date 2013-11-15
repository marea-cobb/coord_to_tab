#__author__ = 'mareac'

import re
import csv
import sys
import fileinput



def readFile():
    header = True
    #Adds the header to the input file
    headerline = "Start of Ref Alignment\t End of Ref Alignment\t Start of Query Alignment\t End of Query Alignment\t" \
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
                h = re.split("\[(.*?)]", lines)
                h2 = map(str.strip, h)
                h3 = filter(None, h2)
                for x in h3:
                    if x == '|':
                        h3.remove(x)
                print 'REF' + '\t' + h3[9] + '\t' + h3[0] + '\t' + h3[1] + '\t' + h3[4] + '\t' + h3[11] + '\t' + \
                      h3[13] + '\t' + 'QUERY' + '\t' + h3[10] + '\t' + h3[2] + '\t' + h3[3] + '\t' + h3[5] + '\t' + \
                      h3[12] + '\t' + h3[13] + '\t' + h3[6] + '\t' + h3[7] + '\t' + h3[8]
            else:
                print lines
        else:
            h = lines.split()
            for x in h:
                if x == '|':
                    h.remove(x)
            print h[15] + '\t' + h[9] + '\t' + h[0] + '\t' + h[1] + '\t' + h[4] + '\t' + h[11] + '\t' + \
                  h[13] + '\t' + h[16] + '\t' + h[10] + '\t' + h[2] + '\t' + h[3] + '\t' + h[5] + '\t' + \
                  h[12] + '\t' + h[14] + '\t' + h[6] + '\t' + h[7] + '\t' + h[8]
            #print ('\t'.join(map(str, header_line[0:13]))) + '\t' + header_line[13] + '\t' + header_line[15] + '\t' + \
            #      header_line[14] + '\t' + header_line[16]



def main():
    readFile()



main()