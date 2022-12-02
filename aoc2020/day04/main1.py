import numpy as np
import pdb

with open("data/test.txt", 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line[:-1])
    if line == '\n':
        print("new record")

pdb.set_trace()
