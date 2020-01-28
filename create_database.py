from Definitions import *
import ROOT
import os
import stat
import glob

def create_script(cmsswpath,samplesname,rootfile,year):
    print samplename
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'src\neval `scram runtime -sh`\n'
    #script+='mkdir '+OutputDirectoryForMEMDatabase+samplename+'\n'
    script+='python '+cmsswpath+'src/MEMDataBase/MEMDataBase/test/createDataBaseFromTree_spring17.py '+OutputDirectoryForMEMDatabase+year+samplename+' '+samplename.replace("_","").replace("-","")+' '+rootfile
    if not os.path.exists("scripts_database"+year):
      os.makedirs("scripts_database"+year)
    filename='scripts_database/'+year+samplename+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)

year = "/2018/"
    
rootfiles=glob.glob(OutputDirectoryForMEMTrees+year+'*.root')
samplenames=[samplename.replace(OutputDirectoryForMEMTrees+year,"").replace(".root","") for samplename in rootfiles]
#print rootfiles
#print samplenames
#print samplenames

# raw_input()
for rootfile,samplename in zip(rootfiles,samplenames):
    print samplename,rootfile
    if not os.path.exists(OutputDirectoryForMEMDatabase+year+"/"+samplename):
      os.makedirs(OutputDirectoryForMEMDatabase+year+"/"+samplename)
    create_script(cmsswpath,samplename,rootfile,year)
    
