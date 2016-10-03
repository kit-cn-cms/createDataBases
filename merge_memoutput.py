from Definitions import *
import ROOT
import os
import stat
import glob
from subprocess import call

for sample in Samples:
  #print Samples
  array=glob.glob(OutputDirectoryForMEMTrees+sample[0]+'_*.root')
  print array
  if not (len(array)>0):
    print "not found"
    print sample
    Samples.remove(sample)
    
    
print Samples
    
for sample in Samples:
  string_add = "hadd "+OutputDirectoryForMEMTrees+sample[0].replace("_","")+".root "+OutputDirectoryForMEMTrees+sample[0]+'_*.root'
  string_mkdir = "mkdir "+OutputDirectoryForMEMDatabase+sample[0].replace("_","")
  #string_del = "rm "+OutputDirectoryForMEMTrees+sample[0]+'_*.root'
  #print string_del
  call(string_add,shell=True)
  #call(string_del,shell=True)
  call(string_mkdir,shell=True)