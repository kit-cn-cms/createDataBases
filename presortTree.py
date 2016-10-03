import ROOT
import sys
from array import array
ROOT.gROOT.SetBatch(True)
ROOT.gDirectory.cd('PyROOT:/')

ids=[]
eventnumbers=[]

#Path with write access where the database should be stored
# Iternal identifier for sample
# e.g. ttbarInlusive
# or ttHbbJESUP
# DO NOT USE UNDERSCORES _ IN THIS NAME
outname=sys.argv[1]

#List of input ntuples containing the MEMs
listOfInputTrees=sys.argv[2:]

event=array("l",[0])

intree=ROOT.TChain("tree")
for intreefilename in listOfInputTrees:
  print "adding ", intreefilename, " to chain"
  intree.Add(intreefilename)
  
intree.SetBranchAddress("event",event)
nEntries=intree.GetEntries()
for ievt in range(nEntries):
  intree.GetEntry(ievt)
  #print ievt, event
  ids.append(ievt)
  eventnumbers.append(event[0])
  
print "nEvents ", len(ids), len(eventnumbers)

zipped=zip(ids,eventnumbers)
#print zipped[0][0],zipped[0][1]
#print zipped[-1][0],zipped[-1][1]

#print zipped
sortedzipped=sorted(zipped, key=lambda x : x[1])
print "nEvents ", len(sortedzipped[0]), len(sortedzipped[1])
#print sortedzipped
#print sortedzipped[0][0],sortedzipped[0][1]
#print sortedzipped[-1][0],sortedzipped[-1][1]
#print sortedzipped
outf=ROOT.TFile(outname,"RECREATE")
outtree=intree.CloneTree(0)
outtree.SetAutoFlush()
done=0
for ievt, eventnum in sortedzipped:
  done+=1
  if done%1000==0:
    print done
  #print ievt, eventnum
  intree.GetEntry(ievt)
  outtree.Fill()
  #exit(0)

outtree.AutoSave()
outf.Close()


