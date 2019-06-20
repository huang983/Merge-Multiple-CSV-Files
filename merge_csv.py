import glob
import pandas as pd

all_files = glob.glob("*.csv")

fout = open('Training/merged.csv','a')
for f in all_files:
    file = open(f)
    for line in file:
        fout.write(line)

fout.close()