import os
import sys
import subprocess
import ConfigParser
import glob

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]



user = "swieland"
year = "2018
print "hadding following user: ", user

path = "/pnfs/desy.de/cms/tier2/store/user/{USER}/mem/ttH_MEM_LEG_{year}_v2/CRAB_UserFiles/".format(USER=user, year=year)
print path

samplepaths = glob.glob(path+"crab*")
cmd = "hadd {outFile} {files} "
manual = []
for sample in samplepaths:
    print("#"*50)
    print("hadding file for {}".format(sample))
    rFiles = glob.glob(sample+"/*/*/*.root")
    outName = sample.rsplit("/")[-1].replace("crab_MEM_ttH_MEM_LEG_"+year+"_","").replace("_0","")
    print("found {n} ROOT files for sample {outName}".format(n=len(rFiles), outName=outName))
    print("#"*50)
    # if len(rFiles) >=500:
        # manual.append(outName)
    for i, ch in enumerate(chunks(rFiles,500)):
        manual.append(outName)
        print(len(ch)) 
        cmd = "hadd {outFile} {files} ".format(files=" ".join(ch), outFile=year+"/"+outName+"_{}.root".format(i))
        # print(cmd)
        subprocess.call(cmd, shell=True)
        print("-"*50)

print("#"*50)
print("Following files sampled need to be hadded in a second step:")
for m in manual:
    print m
print("#"*50)

#for m in manual:
 #   cmd = "hadd " + year + "/" + m +".root " + year + "/" + m +"_*"
  #  subprocess.call(cmd, shell=True)
   # cmd = "rm " + year + "/" + m +"_*.root"
    #subprocess.call(cmd, shell=True)
    

