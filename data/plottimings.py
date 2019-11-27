import json

import os
import subprocess
import sys
import matplotlib.pyplot as plt


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

files = sys.argv[1:]

timingsarray = {}
filename = sys.argv[1]
with open(filename, "r") as json_file:
    data = json.load(json_file)
    for key, value in data['Timing'].items():
        timingsarray[key] = []


for i in range(1,len(sys.argv)):
    filename = sys.argv[i]
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        for key, value in data['Timing'].items():
            print( key," ", value)
            timingsarray[key].append(value)


print(timingsarray)
ranks = [i for i in range(0,len(timingsarray['total']))]
for key, value in timingsarray.items():
    plt.plot(ranks, value, label=key)

plt.legend()
plt.show()
