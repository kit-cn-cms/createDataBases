from Definitions import *
import ROOT
import os
import stat
import glob
import sys
cwd=os.getcwd()

def create_script(cmsswpath,samplesname,rootfile,year):
    print samplename
    print year
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'src\neval `scram runtime -sh`\n'
    script+='python '+cwd+'/presortTree.py '+OutputDirectoryForPresortedTrees+year+"/"+samplename+'.root'+' '+rootfile
    if not os.path.exists("scripts_sort"+year):
      os.makedirs("scripts_sort"+year)
    filename="scripts_sort"+year+samplename+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)
    
year = "/2016/"
rootfiles=glob.glob(InputDirectoryForPresortedTrees+year+'*.root')
samplenames=[samplename.replace(InputDirectoryForPresortedTrees+year,"").replace(".root","") for samplename in rootfiles]
#print rootfiles
#print samplenames
print samplenames
#raw_input()
for rootfile,samplename in zip(rootfiles,samplenames):
    print samplename,rootfile
    if not os.path.exists(OutputDirectoryForPresortedTrees+year):
      os.makedirs(OutputDirectoryForPresortedTrees+year)
    create_script(cmsswpath,samplename,rootfile,year)