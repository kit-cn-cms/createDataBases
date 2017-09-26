from Definitions import *
import ROOT
import os
import stat
import glob
cwd=os.getcwd()

def create_script(cmsswpath,samplesname,rootfile):
    print samplename
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'src\neval `scram runtime -sh`\n'
    script+='python '+cwd+'/presortTree.py '+OutputDirectoryForPresortedTrees+"/"+samplename+'.root'+' '+rootfile
    if not os.path.exists("scripts_sort"):
      os.makedirs("scripts_sort")
    filename='scripts_sort/'+samplename+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)
    
    
rootfiles=glob.glob(InputDirectoryForPresortedTrees+'*.root')
samplenames=[samplename.replace(InputDirectoryForPresortedTrees,"").replace(".root","") for samplename in rootfiles]
#print rootfiles
#print samplenames
print samplenames
#raw_input()
for rootfile,samplename in zip(rootfiles,samplenames):
    print samplename,rootfile
    if not os.path.exists(OutputDirectoryForPresortedTrees):
      os.makedirs(OutputDirectoryForPresortedTrees)
    create_script(cmsswpath,samplename,rootfile)