#fdasfdas ! /usr/bin/env python3
# # fdasgfs encoding: utf-8
import datetime
import os
import subprocess

wtime ="24"
nnodes = "1"
ns = ["1024", "2048"] #,"256", "512", "1024" ]
#cases = ["cat_pvti"]
#cases = ["direct_no_io", "direct_io", "cat_pvti", "cat_png"]
cases = ["cat_pvti", "cat_png"]
xmlcases=["catalyst", "catalyst_pngs"]
#xmlcases = ["no_io", "io", "catalyst", "catalyst_pngs"]

#basedir = "/scratch/snx3000/rhohl/alsvinn_insitu/"
basedir = "/users/rhohl/alsvinn_insitu/" #/cluster/home/hohlr/alsvinn_insitu/" #/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu" #"
alsvinn = "/users/rhohl/alsvinn/build/alsuqcli/alsuqcli" # "/cluster/home/hohlr/alsvinn/build/alsuqcli/alsuqcli"

#subprocess.check_call(["rm", "-rf", "build_*"], cwd =basedir)

for n in ns:
    for i in range(0,len(cases)):
        c = cases[i]
        xmlname = basedir+"benchmarkDaint/inputfiles_2d_1sample/benchmark_"+xmlcases[i]+"_"+n+".xml"
        jobname = xmlcases[i]+"_"+n+"_"+nnodes
	newfolder = "build_"+c+"_"+n
        subprocess.check_call(["mkdir", newfolder], cwd =basedir)
        newfolder = basedir+newfolder
 	if(c == "cat_png" or c== "cat_pvti"):       
		subprocess.check_call(["cmake", "-DOPENGL_opengl_LIBRARY=/opt/cray/nvidia/default/lib64/libOpenGL.so", "-DTBB_INCLUDE_DIR=/opt/intel/compilers_and_libraries/linux/tbb/include", "-DTBB_LIBRARY_RELEASE=/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.7/libtbb.so", ".."], cwd = newfolder)
        	subprocess.check_call(["make"], cwd = newfolder)
	print ' xml file :'
	print xmlname
        print 'in folder :'
	print newfolder
	print 'alsvinn:'
	print alsvinn
	subprocess.check_call(["cp", xmlname, "."], cwd = newfolder)
	# subprocess.check_call(["OMP_NUM_THREADS=",ncores,"bsub", "-n",ncores, "-W", "4:00", alsvinn, xmlname], cwd = newfolder)
#	subprocess.check_call(["bsub", "-n",nnodes, "-W", "4:00", alsvinn, xmlname], cwd = newfolder)
        totcommand = alsvinn+ " " + xmlname 
        subprocess.check_call(["python3", "submit_command_on_daint.py", "-w", newfolder,  "--command" ,totcommand, "--name", jobname,"--wait_time", wtime,"--nodes", nnodes,  "--dry_run"])
        subprocess.check_call(["python3", "submit_command_on_daint.py", "-w", newfolder,  "--command" ,totcommand, "--name", jobname,"--wait_time", wtime,"--nodes", nnodes]) #, "--dry_run"])
