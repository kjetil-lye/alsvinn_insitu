#fdasfdas ! /usr/bin/env python3
# # fdasgfs encoding: utf-8
import datetime
import os
import subprocess


dryrun = False
wtime ="1"
nnodes = "1"
dim ="3"

ns = ["64","128","256"]
cases = ["direct_no_io", "cat_pvti", "cat_png"]
xmlcases = ["no_io", "catalyst", "catalyst_pngs"]

basedir = "/scratch/snx3000/rhohl/alsvinn_insitu/"
#basedir = "/users/rhohl/alsvinn_insitu/" #/cluster/home/hohlr/alsvinn_insitu/" #/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu" #"
alsvinn = "/users/rhohl/alsvinn/build/alsuqcli/alsuqcli" # "/cluster/home/hohlr/alsvinn/build/alsuqcli/alsuqcli"


for n in ns:
    for i in range(0,len(cases)):
        c = cases[i] 
        xmlname = basedir+"benchmarkDaint/inputfiles_"+dim+"d_1samples/benchmark_"+xmlcases[i]+"_"+n+".xml"
        if(int(nnodes)>1):
        	xmlname = basedir+"benchmarkDaint/inputfiles_"+dim+"d_"+nnodes+"samples/benchmark_"+xmlcases[i]+"_"+n+".xml"
	jobname = xmlcases[i]+"_"+n+"_"+dim+"d_"+nnodes
	newfolder = "build_"+c+"_"+n+"_"+dim+ "d_"+nnodes
	if(not dryrun):
		subprocess.check_call(["mkdir", newfolder], cwd =basedir)
	newfolder = basedir+newfolder
 	if(not dryrun and (c == "cat_png" or c== "cat_pvti")):       
		subprocess.check_call(["cmake", "-DOPENGL_opengl_LIBRARY=/opt/cray/nvidia/default/lib64/libOpenGL.so", "-DTBB_INCLUDE_DIR=/opt/intel/compilers_and_libraries/linux/tbb/include", "-DTBB_LIBRARY_RELEASE=/opt/intel/compilers_and_libraries/linux/tbb/lib/intel64/gcc4.7/libtbb.so", ".."], cwd = newfolder)
        	subprocess.check_call(["make"], cwd = newfolder)
	print ' xml file :'
	print xmlname
        print 'in folder :'
	print newfolder
	print 'alsvinn:'
	print alsvinn
	if(not dryrun):
		subprocess.check_call(["cp", xmlname, "."], cwd = newfolder)
		subprocess.check_call(["cp",  basedir+"benchmarkDaint/inputfiles_"+dim+"d_"+nnodes+"samples/kelvinhelmholtz_3d_tube.py" , "."], cwd = newfolder)
        totcommand = alsvinn+ " " + xmlname 
        if(int(nnodes)>1):
		totcommand = alsvinn+ " --multi-sample "+nnodes+" " + xmlname 
        subprocess.check_call(["python3", "submit_command_on_daint.py", "-w", newfolder,  "--command" ,totcommand, "--name", jobname,"--wait_time", wtime,"--nodes", nnodes,  "--dry_run"])
       
	if(not dryrun):
		subprocess.check_call(["python3", "submit_command_on_daint.py", "-w", newfolder,  "--command" ,totcommand, "--name", jobname,"--wait_time", wtime,"--nodes", nnodes]) #, "--dry_run"])
