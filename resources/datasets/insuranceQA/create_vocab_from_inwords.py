#!/bin/python
import re
from nltk.tokenize import word_tokenize

# This script will 
#      seperate 'full-stop/period' as another word (identifying new lines) in the text
#      lowercase the character after 'full-stop/period' - The words with Capital letters otherwise are considered as another word
#      tokenize the rest of the sentence

def tok(sent):
    '''
    sent=re.sub(r'([a-zA-Z0-9])([?!.]) ([A-Z])',r'\1 \2 \3',sent) #newline
    sent=re.sub(r' ([?!.]) ([A-Z])',lambda m: m.group(0).lower(),sent) # lower case the word after newline
    sent=re.sub(r'([a-zA-Z0-9])([.?!])$',r'\1 \2',sent) # last line
    sent=re.sub(r'([a-zA-Z0-9])([,]) ([a-z])',r'\1 \2 \3',sent) #commas
    '''
    sent=" ".join(word_tokenize(sent)) # Using ready made tokenizer
    sent=sent.lower() # lowercase everything
    return sent 

vocab=[]

# For all the tokenized corpus, fetch the vocabulary
for File in ["InsuranceQA.German.test.500.inwords.decomp","InsuranceQA.German.valid.500.inwords.decomp","InsuranceQA.German.train.500.inwords.decomp","./InsuranceQA.German.answers.inwords.decomp"]:
  print("making vocabulary from "+File+" ..")
  with open(File,"r") as f:
    for line in f:
      line=line.strip()
      fields=line.split("\t")
      for word in fields[1].split():
          if word not in vocab:
              vocab.append(word)

vfile=open("./vocabulary","w")
for idx in range(len(vocab)):
   vfile.write("idx_"+str(idx+1)+"\t"+vocab[idx]+"\n")  

