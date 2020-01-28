import os
import sys
import subprocess
import ConfigParser
import glob
import optparse

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

parser = optparse.OptionParser()
parser.add_option("-u", "--user", dest = "user", help = "CERN username")
parser.add_option("-y", "--year", dest = "year", help = "year of mem production")
parser.add_option("-n", "--name", dest = "name", help = "name of mem jobs")
parser.add_option("-o", "--output", dest = "outpath", help = "output path")
(opts, args) = parser.parse_args()

print "hadding following user: ", opts.user

path = "/pnfs/desy.de/cms/tier2/store/user/{USER}/mem/{folder}/CRAB_UserFiles/".format(USER=opts.user, folder=opts.name)
print path
outPathBase = opts.outpath

samplepaths = glob.glob(path+"crab*")
cmd = "hadd {outFile} {files} "
for sample in samplepaths:
    hadd_parts = []
    print("#"*50)
    print("hadding file for {}".format(sample))
    rFiles = glob.glob(sample+"/*/*/*.root")
    outName = sample.rsplit("/")[-1].replace("crab_MEM_"+opts.name+"_","").replace("_0","")
    print("found {n} ROOT files for sample {outName}".format(n=len(rFiles), outName=outName))
    print("#"*50)
    for i, ch in enumerate(chunks(rFiles,100)):
        outFile = outPathBase+"/"+opts.year+"/"+outName+"_{}.root".format(i)
        hadd_parts.append(outFile)
        print(len(ch)) 
        cmd = "hadd {outFile} {files} ".format(files=" ".join(ch), outFile=outFile)
        # print(cmd)
        subprocess.call(cmd, shell=True)
        print("-"*50)

    outFile = outPathBase+"/"+opts.year+"/"+outName+".root"
    # combine
    cmd = "hadd {outFile} {files}".format(files =" ".join(hadd_parts), outFile = outFile)
    print(cmd)
    subprocess.call(cmd, shell=True)
    cmd = "rm {files}".format(files = " ".join(hadd_parts))
    print(cmd)
    subprocess.call(cmd, shell=True)

    

