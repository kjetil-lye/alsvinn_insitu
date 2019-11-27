import json
import os
import subprocess
import sys
import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

from operator import itemgetter
cm = plt.cm.get_cmap('RdYlBu', 100)
 

print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))


ehist1 = { "xyz" : "ooo", "x" : 0.0 , "y": 0.0, "z" : 0.0,  "time" : 0, "bins" : [0.0], "values": [1]}
ehist2 = { "xyz0" : "xyz0",  "x0" : 0.0 , "y0": 0.0, "z0" : 0.0, "xyz1" : "xyz1",  "x1" : 0.0 , "y1": 0.0, "z1" : 0.0,  "time" : 0, "bins0" : [],"bins1" : [], "values": []}

hists2 = []
hists1 = []
if( sys.argv[1] == "2"):

    for i in range(2,len(sys.argv)):
        filename = sys.argv[i]
        ehist2["xyz0"] = filename[8:22]
        ehist2["x0"] = float(filename[8:12])
        ehist2["y0"] = float(filename[13:17])
        ehist2["z0"] = float(filename[18:22])
        ehist2["xyz1"] = filename[25:39]
        ehist2["x1"] = float(filename[25:29])
        ehist2["y1"] = float(filename[30:34])
        ehist2["z1"] = float(filename[35:39])
        ehist2["time"] = float(filename[41:45])
     
        with open(filename, "r") as f:
            for cnt, line in enumerate(f):
                if(cnt == 0):
                    ehist2["bins0"] = json.loads(line[(line.find('=')+2):] ) 
                elif(cnt == 1):
                    ehist2["bins1"] = json.loads(line[(line.find('=')+2):] ) 
                elif(cnt == 2):
                    ehist2["values"] = json.loads(line[(line.find('=')+2):] ) 
                    
        hists2.append(ehist2.copy())
     
        #f.close()
    
    with open('notsortedtwoPointHist.json', 'w') as jf:
        json.dump(hists2, jf)
        
    sortedhist2 =  sorted(hists2, key=lambda x:  (x['xyz0'], x['xyz1']) )
   
        
    with open('twoPointHist.json', 'w') as jf:
        json.dump(sortedhist2, jf)
    
    oldxyz = sortedhist2[0]['xyz0']+ sortedhist2[0]['xyz1']

    n = len(sortedhist2[0]['bins0'])
    idx = 0
    lims  = 0
    for i in range(0,len(sortedhist2)):
      
       
        if(sortedhist2[i]['xyz0']+ sortedhist2[i]['xyz1'] != oldxyz or i> len(sortedhist2)-2):

            maxv0 = max(max(sortedhist2[idx:i], key=lambda x: max(x['bins0']))['bins0'])
            minv0 = min( min(sortedhist2[idx:i], key=lambda x: min(x['bins0']))['bins0'])
            maxv1 = max(max(sortedhist2[idx:i], key=lambda x: max(x['bins1']))['bins1'])
            minv1 = min( min(sortedhist2[idx:i], key=lambda x: min(x['bins1']))['bins1'])
   
            d0 =(maxv0-minv0)/float(n-1)
            d1 =(maxv1-minv1)/float(n-1)
            newbins0 = [minv0+x*d0 for x in range(0,n)]
            newbins1 = [minv1+x*d1 for x in range(0,n)]
            for j in range(idx,i):
                newvals = [0 for bla in range(0,len(sortedhist2[j]['values']))]
                newnewvals = [0 for bla in range(0,len(sortedhist2[j]['values']))]
               
                for bi in  range(0,n-1):
                    for nbi in  range(0,n-1):
                        if ( sortedhist2[j]['bins0'][bi] >= newbins0[nbi] and sortedhist2[j]['bins0'][bi+1] <= newbins0[nbi+1]): 
                            for v in range(0,len(sortedhist2[j]['values'] )-1):
                                if(v%(n-1) == bi):
                               #     print(v%(n-1), bi, v, n-1)
                                    
                                    newpos = v + (nbi-bi)-1
                                 #   print(bi, nbi, newpos, v)
                                    newvals[newpos] += sortedhist2[j]['values'][v]
                            break
                        elif(sortedhist2[j]['bins0'][bi] <= newbins0[nbi]  and sortedhist2[j]['bins0'][bi+1] <= newbins0[nbi+1]  ):
                            for v in range(0,len(sortedhist2[j]['values'] )-1):
                                if(v%(n-1) == bi):
                                    newpos = v + (nbi-bi)-1
                                    per = int(sortedhist2[j]['values'][v]*(newbins0[nbi]-sortedhist2[j]['bins0'][bi])/(sortedhist2[j]['bins0'][bi+1]-sortedhist2[j]['bins0'][bi]))
                                    newvals[newpos] += per
                                  #  print(len(newvals))
                                 #   print(bi, nbi, newpos, v)
                                    newvals[newpos+1] += (sortedhist2[j]['values'][v]-per)
                            break
                    if(bi>=n-1):
                        for v in range(0,len(sortedhist2[j]['values'] )-1):
                                if(v%(n-1) == n-1):
                                    newpos = v + (nbi-n+1)
                                    newvals[newpos] += sortedhist2[j]['values'][v+1]

            #    print(sum(sortedhist2[j]['values']))  
             #   print(sum(newvals))
            
                for bi in  range(0,n-1):
                    for nbi in  range(0,n-1):
                        if ( sortedhist2[j]['bins1'][bi] >= newbins1[nbi] and sortedhist2[j]['bins1'][bi+1] <= newbins1[nbi+1]): 
                            for v in range(0,len(sortedhist2[j]['values'] )):
                                if(v//(n-1)==bi):
                                    newpos = v + ((nbi-bi))*(n-1)
                                  #  print(bi, nbi,  v, newpos)
                                    newnewvals[newpos] += newvals[v]
                            break
                        elif(sortedhist2[j]['bins1'][bi] <= newbins1[nbi]  and sortedhist2[j]['bins1'][bi+1] <= newbins1[nbi+1]  ):
                            for v in range(0,len(sortedhist2[j]['values'] )):
                                if(v//(n-1)==bi):
                                    newpos = v + ((nbi-bi))*(n-1)
                                 #   print(bi, nbi, v, newpos)
                                    per = int(newvals[v]*(newbins1[nbi]-sortedhist2[j]['bins1'][bi])/(sortedhist2[j]['bins1'][bi+1]-sortedhist2[j]['bins1'][bi]))
                                    newnewvals[newpos] += per
                                    if(newpos +(n-1) <100):
                                        newnewvals[newpos+(n-1)] += (newvals[v]-per)
                                    else:
                                        newnewvals[newpos] += (newvals[v]-per)
                            break
                    if(bi>=n-1):
                        for v in range(0,len(sortedhist2[j]['values'] )):
                                if(v//(n-1)==n-1):
                                    newpos = v + ((nbi-n-1))*(n-1)
                                    newnewvals[newpos] += sortedhist2[j]['values'][v+(n-1)]
               

             
              #  print(sum(newnewvals)) 
                

              
                sortedhist2[j]['bins0'] = newbins0
                sortedhist2[j]['bins1'] = newbins1
                sortedhist2[j]['values'] = newnewvals
            idx = i
            oldxyz =sortedhist2[i]['xyz0']+ sortedhist2[i]['xyz1']

        for i in range(0,len(sortedhist2)):    
            lims = max( lims, max( sortedhist2[i]['values']))

              
    for i in range(0,len(sortedhist2)):
        N = len(sortedhist2[i]['values'])
        magn = 1
        xpos = [ magn*(sortedhist2[i]['bins0'][b+1]+sortedhist2[i]['bins0'][b])/2. for a in range(0, len(sortedhist2[i]['bins0'])-1) for b in range(0, len(sortedhist2[i]['bins0'])-1) ]
        ypos = [ magn*(sortedhist2[i]['bins1'][b+1]+sortedhist2[i]['bins1'][b])/2.for b in range(0, len(sortedhist2[i]['bins1'])-1) for a in range(0, len(sortedhist2[i]['bins1'])-1) ]
       
        print(N)
        _xx, _yy = np.meshgrid(sortedhist2[i]['bins0'],sortedhist2[i]['bins1'])
        dx = np.ones(N)*(sortedhist2[i]['bins0'][1]-sortedhist2[i]['bins0'][0])
        dy = np.ones(N)*(sortedhist2[i]['bins1'][1]-sortedhist2[i]['bins1'][0])

        zpos = np.zeros_like(dx)
        dz = sortedhist2[i]['values']

       
        fig = plt.figure()
        ax1 =  Axes3D(fig) #fig.add_subplot(111, projection='3d'):
        #for ix in range(0, len(xpos)):
        #plt.scatter(xpos, ypos, c=dz, cmap=cm)
         #   plt.show()
          
      #  ax1.scatter(xpos,ypos,dz)
        
        ax1.bar3d(xpos, ypos, zpos, dx[0], dy[0], dz, color=(0.416,0.447,0.4667, 0.9), shade=True)
        ax1.set_xlim3d(min(sortedhist2[i]['bins0'])+dx[0], magn*max(sortedhist2[i]['bins0'])+dx[0] )
        ax1.set_ylim3d(magn*min(sortedhist2[i]['bins1'])+dy[0], magn*max(sortedhist2[i]['bins1'])+dy[0] )
        ax1.set_zlim3d(0, lims )
      
        xl = "Density at point " +sortedhist2[i]['xyz0']
        yl = "Density at point " +sortedhist2[i]['xyz1']
        ax1.set_ylabel(yl,fontsize=8)
        ax1.set_xlabel(xl,fontsize=8)
        ax1.set_zlabel('Frequency',fontsize=8)
        ax1.set_xticks([round(x,2) for x in sortedhist2[i]['bins0']])
        ax1.set_yticks([round(x,2) for x in sortedhist2[i]['bins1']])
       # ax1.tick_params(direction='inout')
        #ax1.set_yticklabels([str(round(x,3)) for x in sortedhist2[i]['bins0']], rotation=45, ha='left')
        #ax1.set_xticklabels([str(round(x,3)) for x in sortedhist2[i]['bins1']], rotation=45, ha='right')

        tit =sortedhist2[i]['xyz0']+ sortedhist2[i]['xyz1']+'_'+str(int(sortedhist2[i]['time']*1000))
        print(tit)
        plt.title('['+str(sortedhist2[i]['x0'])+ ','+str(sortedhist2[i]['y0'])+ ','+str(sortedhist2[i]['z0'])+ '] x ['+str(sortedhist2[i]['x1'])+ ','+str(sortedhist2[i]['y1'])+ ','+str(sortedhist2[i]['z1'])+ '] at t='+str(sortedhist2[i]['time']),fontsize=12)
        nm = tit+'.png'
       
       # plt.colorbar()
        plt.savefig(nm)
        plt.close(fig)
       # plt.close()
      #  fig.show()

elif(sys.argv[1]=='1'):
    for ii in range(2,len(sys.argv)):
        filename = sys.argv[ii]
        ehist1["x"] = float(filename[8:12])
        ehist1["y"] = float(filename[13:17])
        ehist1["z"] = float(filename[18:22])
        ehist1["xyz"] = filename[8:22]
        ehist1["time"] = float(filename[24:28])

        with open(filename, "r") as f:
            for cnt, line in enumerate(f):
                if(cnt == 0):
                    ehist1["bins"] = json.loads(line[(line.find('=')+2):] ) 
                elif(cnt == 1):
                    ehist1["values"] = json.loads(line[(line.find('=')+2):] ) 
            
           # f.close()
       
        hists1.append(ehist1.copy())

  
    sortedhist1 =  sorted(hists1, key=itemgetter('xyz'))  
    
    with open('onePointHist.json', 'w') as jf:
        json.dump(sortedhist1, jf)
    
    oldxyz = sortedhist1[0]['xyz']
    n = len(sortedhist1[0]['bins'])
    idx = 0

    for i in range(0,len(sortedhist1)):
         
        if(sortedhist1[i]['xyz'] != oldxyz or i>= len(sortedhist1)-1):
    
            maxv = max(max(sortedhist1[idx:i], key=lambda x: max(x['bins']))['bins'])
            
            minv = min( min(sortedhist1[idx:i], key=lambda x: min(x['bins']))['bins'])
            dx =(maxv-minv)/float(n-1)
            newbins = [minv+x*dx for x in range(0,n)]
            for j in range(idx,i):
                newvals = [0 for bla in range(0,len(sortedhist1[j]['values']))]
               
                for bi in  range(0,n-1):
                    for nbi in  range(0,n-1):
                        if ( sortedhist1[j]['bins'][bi] >= newbins[nbi] and sortedhist1[j]['bins'][bi+1] <= newbins[nbi+1]): 
                            newvals[nbi] += sortedhist1[j]['values'][bi]
                            break
                        elif(sortedhist1[j]['bins'][bi] <= newbins[nbi]  and sortedhist1[j]['bins'][bi+1] <= newbins[nbi+1]  ):
                            per = int(sortedhist1[j]['values'][bi]*(newbins[nbi]-sortedhist1[j]['bins'][bi])/(sortedhist1[j]['bins'][bi+1]-sortedhist1[j]['bins'][bi]))
                            newvals[nbi] += per
                            newvals[nbi+1] += (sortedhist1[j]['values'][bi]-per)
                            break
                    if(bi>=n-2):
                        newvals[n-2] += sortedhist1[j]['values'][bi+1]
               
                if( sum(newvals) <100):
                    print(sortedhist1[j]['time'])
                    print(maxv)
                    print(minv)
                    print("new hist ")
                    print(newbins)
                    print(newvals)
                    print("old hist")
                    print(sortedhist1[j]['bins'])
                    print(sortedhist1[j]['values'])

                sortedhist1[j]['bins'] = newbins
                sortedhist1[j]['values'] = newvals
            idx = i
            oldxyz = sortedhist1[i]['xyz']

              
    for i in range(0,len(sortedhist1)):
        delta = sortedhist1[i]['bins'][1]-sortedhist1[i]['bins'][0]
        plt.bar([x+delta*0.5 for x in sortedhist1[i]['bins']] , sortedhist1[i]['values'], width = delta, color=(0.416,0.447,0.4667, 0.9))
        plt.xlim(min(sortedhist1[i]['bins'])+delta, max(sortedhist1[i]['bins'])+delta )
        plt.ylim(0, 100)
        plt.grid(axis='y', alpha=0.1)
        plt.xlabel('Value of Density',fontsize=8)
        plt.ylabel('Frequency',fontsize=8)
        plt.xticks([round(x,3) for x in sortedhist1[i]['bins']] , fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylabel('Frequency',fontsize=8)
        tit = sortedhist1[i]['xyz']+'_'+str(int(sortedhist1[i]['time']*1000))
        plt.title('Distribution Histogram at ['+str(sortedhist1[i]['x'])+ ','+str(sortedhist1[i]['y'])+ ','+str(sortedhist1[i]['z'])+ '] at t='+str(sortedhist1[i]['time']),fontsize=12)
        nm = tit+'.png'
        plt.savefig(nm)
        plt.close()
       # plt.show()
        

