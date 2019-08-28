
import operator
import matplotlib

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta


walltime= []
walltimefile= open("walltimehuman.out", "r")
for x in walltimefile:
    s = x.replace('"','')
    s = s.replace(',','')
    walltime.append(s[-9:-1])
walltimefile.close()


names= []
sizes= []
sizesfile= open("foldersizes.out", "r")
for x in sizesfile:
    s = x.replace('"','')
    s = s.replace(',','')
    iend = s.find('b')-1
    sizes.append(s[0:iend])
    names.append(s[iend+1:-1])
sizesfile.close()

print(names)

n = [0 for i in range(0,len(names))]
type = [0 for i in range(0,len(names))]
datasize = [0 for i in range(0,len(names))]

if(len(walltime) != len(sizes)):
    print( 'ERR: sizes not the same: datasizes is of size: ', len(sizes), ' and walltimes is of size: ', len(walltime))

ntot = len(sizes)

#normalize datasizes (makefile etc)
noiosizeidx = 0
for i in range(0,len(names)):
    if(names[i].find('no_io')!=-1):
        noiosizeidx = i
        break
NOIOSIZE = int(sizes[noiosizeidx])

for i in range(0,len(sizes)):
    datasize[i] = int(sizes[i])- NOIOSIZE
    #sort for plotting
    n[i] = int(names[i][-4:].replace('_',''))
    type[i] = names[i][:-4].replace('_',' ').replace('build','').replace('direct io', 'netcdf writer').replace('direct no io', 'no output')

print(type)

data = [list(a) for a in zip( type, n, datasize, walltime)]
data.sort(key = operator.itemgetter(0,1))

nns=3
ntypes = 4

f = plt.figure()
ax = f.add_subplot(1,2,1)
ax2 = f.add_subplot(1,2,2)

for i in range(0,ntypes):
    subdata = data[(i*nns):((i+1)*nns)][:]

    #ax.plot([1,1], data[i][1],data[i][2], label=data[i][0])
    datetime_object = [0 for x in range(0, nns)]
    subn = [0 for x in range(0, nns)]
    subsize = [0 for x in range(0, nns)]

    for ti in range(0,nns):
        subn[ti] = subdata[ti][1]
        subsize[ti] = subdata[ti][2]
        datetime_object[ti] =  datetime.strptime(subdata[ti][3], '%H:%M:%S')

    time = [t for t in mdates.date2num(datetime_object)]
    ax.plot(subn, time, label=subdata[0][0])
    ax.yaxis_date()
    ax.yaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
    ax.set_xticks(subn)
    ax2.plot(subn ,subsize, label=subdata[0][0])
    ax2.set_xticks(subn)


ax.legend()
ax.set_ylabel('Walltime in HH:MM:SS')
ax.set_xlabel('Grid Size')
ax.set_title('Grid Size vs Walltime')
ax2.legend()
ax2.set_ylabel('Size in [KB]')
ax2.set_xlabel('Grid Size')
ax2.set_title('Grid Size vs Storage Size')
plt.show()
