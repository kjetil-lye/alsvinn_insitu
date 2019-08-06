#! /usr/bin/env python3
# encoding: utf-8


import datetime
import os
import subprocess


print("hello")


def todays_scratch_directory():
    scratch = "/".join(["${SCRATCH}", datetime.date.today().isoformat()])
    scratch = os.path.expandvars(scratch)
    latest = os.path.expandvars("${SCRATCH}" + "/latest")

    if os.path.islink(latest):
        os.unlink(latest)
    os.symlink(scratch, latest)

    return scratch


def write_xml


ncores = "8"
ns = ["128", "512", "1024", "2048"]
cases = ["direct_no_io", "direct_io", "cat_pvti", "cat_png"]
xmlcases = ["no_io", "io", "catalyst", "catalyst_pngs"]


basedir = "/cluster/home/hohlr/alsvinn_insitu/" #/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu" #"
alsvinn = "/cluster/home/hohlr/alsvinn/build/alsuqcli/alsuqcli"

subprocess.check_call(["rm", "-rf", "b_*"], cwd =basedir)

for n in ns:
    for i in range(0,len(cases)):
        c = cases[i]
        xmlname = basedir+"benchmarkSmall/benchmark_"+xmlcases[i]+"_"+ns+".xml"
        newfolder = "b_"+c+"_"+n
        subprocess.check_call(["mkdir", newfolder], cwd =basedir)
        newfolder = basedir+"/"+newfolder
        subprocess.check_call(["cmake", ".."], cwd = newfolder)
        subprocess.check_call(["make"], cwd = newfolder)
        subprocess.check_call(["OMP_NUM_THREADS=",ncores,"bsub", "-n","-W", "4:00", ncores, alsvinn, xmlname], cwd = newfolder)
