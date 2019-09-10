#fdasfdas ! /usr/bin/env python3
# # fdasgfs encoding: utf-8


import datetime
import os
import subprocess


nnodes = "1"
ns = ["64"] #,"256", "512", "1024" ]
cases = ["direct_no_io", "direct_io", "cat_pvti", "cat_png"]
xmlcases = ["no_io", "io", "catalyst", "catalyst_pngs"]


basedir = "/users/rhohl/alsvinn_insitu" #/cluster/home/hohlr/alsvinn_insitu/" #/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu" #"
alsvinn = "/users/rhohl/alsvinn/build/alsuqcli" # "/cluster/home/hohlr/alsvinn/build/alsuqcli/alsuqcli"

subprocess.check_call(["rm", "-rf", "build_*"], cwd =basedir)

for n in ns:
    for i in range(0,len(cases)):
        c = cases[i]
        xmlname = basedir+"benchmarkDaint/benchmark_"+xmlcases[i]+"_"+n+".xml"
        newfolder = "build_"+c+"_"+n
        subprocess.check_call(["mkdir", newfolder], cwd =basedir)
        newfolder = basedir+newfolder
        subprocess.check_call(["cmake", ".."], cwd = newfolder)
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
    subprocess.check_call(["python3", "submit_command_on_daint.py", "-w", ".",  "--command" ,alsvinn, "--name", xmlname,"--wait_time", "1","--nodes", nnodes, "--dry_run"])
