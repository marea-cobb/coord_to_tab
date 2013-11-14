__author__ = 'mareac'

import re
import csv



def readFile():
    header = True
    f = open('/Users/mareac/Desktop/Scaffolds.LmjF.coords', 'r')
    new_file = open('/Users/mareac/Desktop/new_file.csv', 'wb')
    writer = csv.writer(new_file)
    for line in f:
        if header:
            # Checks for the header line.
            if line.startswith('='):
                print 'Switched past header'
                header = False
            else:
                header_line = re.split("\[(.*?)]", line)
                header_line2 = map(str.strip, header_line)
                header_line3 = filter(None, header_line2)
                for x in header_line3:
                    if x == '|':
                        header_line3.remove(x)
                writer.writerow(header_line3)
        else:
            header_line = line.split()
            for x in header_line:
                if x == '|':
                    header_line.remove(x)
            writer.writerow(header_line)
            pass


def main():
    readFile()



main()