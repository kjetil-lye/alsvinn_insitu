import datetime
import os
import subprocess


import sys

nf = 100

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)



dryrun = False


#sort to rename
files = sys.argv[2:]
numbering = [0 for i in range(0,nf)]
sortedidx = [0 for i in range(0,nf)]
filename = sys.argv[1]


print filename

for i in range(2,len(sys.argv)):
        tmp = sys.argv[i].replace(filename, '')
            tmp = tmp.replace('.png', '')
                numbering[i-2] = int(tmp)


                numbering, files = (list(t) for t in zip(*sorted(zip(numbering, files))))

                print files

                for i in range(0,len(files)):
                        subprocess.check_call(["mv", files[i], filename+str(i)+".png"], cwd = '.')

                        print 'Example:  ffmpeg -framerate 3 -i E_mean_%d.png  -vf scale=1920:1080 -vcodec libx264 -crf 1  -pix_fmt yuv420p   E_mean_Video.mp4'
                        newnames = filename+'%d.png' 
                        subprocess.check_call(['ffmpeg', '-framerate', '3', '-i',newnames , '-vf', 'scale=1920x1080','-vcodec','libx264', '-crf', '1', '-pix_fmt', 'yuv420p', filename+'Video.mp4' ])

