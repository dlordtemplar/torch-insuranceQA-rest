#!/bin/python


lines=[]

repl=dict()
with open("target.decomp.uniq.txt","r") as f:
     for line in f :
        line=line.strip()
        fields=line.split("\t")
        repl[int(fields[0])]=fields[1]
        
newfile=open("InsuranceQA.German.answers.inwords.new.decomp","w")

with open("InsuranceQA.German.answers.inwords.decomp","r") as f:
     for line in f :
        line=line.strip()
        fields=line.split("\t")
        if (int(fields[0]) in repl.keys()):
             print(fields[0])
             newfile.write(fields[0]+"\t"+repl[int(fields[0])]+"\n")
             #print(repl[int(fields[0])])
        else:
             newfile.write(line+"\n")

       

