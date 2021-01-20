from Bio import SeqIO
import re
import sys
import csv
import random
import os



def save_file(res):
  with open('output.tsv', 'a') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(res)


#k_mers = []
#for k = 8

def buid_corpus(k_min,k_max,fasta_path):

  #delete the file exits
  file_exists = os.path.isfile('output.tsv') 
  if(file_exists):
       os.remove('output.tsv')

  files = list()
  for (dirpath, dirnames, filenames) in os.walk(fasta_path):
    files += [os.path.join(dirpath, file) for file in filenames]
    for file in files:
      for k in range(k_min,k_max+1):
        print('========================= for k = {}  ==============================='.format(k))
        for seq_record in SeqIO.parse(file, "fasta"):
                a=re.sub('[^GATC]',"",str(seq_record.seq.ungap(' ')).upper())
                b = [a[i:i+k] for i in range(0,len(a)-(k-1))]
                save_file(b)

