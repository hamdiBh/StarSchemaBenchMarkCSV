import csv
import linecache
import  sys
sys.stdout = open("ssbRaw.csv", "wt")


f = open("lineorder.csv", 'rt')
csvfile= open('eggs.csv', 'wt')

spamwriter = csv.writer(csvfile,quoting=csv.QUOTE_NONE)
try:
    reader = csv.reader(f,delimiter=',', quotechar='"')
    for row in reader:
        x= int (row[2])
        y = int(row[3])

        row[2]= linecache.getline('customer.csv', x-1).replace(",\n","")
        row[3]= linecache.getline('part.csv', y-1).replace(",\n","")
        print(", ".join(str(elt) for elt in row))

finally:
    f.close()