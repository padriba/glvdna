from Bio import SeqIO
from ete3 import NCBITaxa
ncbi = NCBITaxa()
import numpy as np
import csv
import re
import time

   

def save_file(seqid,vectors):
  #print('save:',seqid)
  with open('output_vectorisation.tsv', 'a') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow([seqid,vectors])



##ids = []
##f = open("low.txt", "r")
##for x in f:
##   ids.append(int(x))
##
##print (ncbi.get_rank(ids))



with open("output_vectors.txt", 'r') as f:
        vectors = {}
        for line in f:
            vals = line.rstrip().split(' ')
            vectors[vals[0]] = [float(x) for x in vals[1:]]
#print(vectors)
for seq_record in SeqIO.parse("input/low.fasta", "fasta"):
##      if(seq_record.id in corected_sequences):
##            full_sequence = corected_sequences[seq_record.id]
##      else:
##            full_sequence = re.sub('[^GATC]',"",str(seq_record.seq.ungap(' ')).upper()) 
##            corected_sequences[seq_record.id] = full_sequence
   #print(seq_record.id)
   sumvect = np.zeros((50,),dtype=int)
   kmer = 8
   step = 8
   word_co = 0
   print('for seqid',seq_record.id)
  # start_time = time.time()
   sequence_segment = re.sub('[^GATC]',"",str(seq_record.seq.ungap(' ')).upper())
   for i in range(0, len(sequence_segment)-8+1, step):
      v= vectors[sequence_segment[i: i + kmer]] 
      sumvect = np.sum([sumvect,v],axis=0)
      word_co += 1
   sumvect = sumvect/word_co
##   print("--- %s vecterisation time ---" % (time.time() - start_time))
##   start_time = time.time()
   save_file(seq_record.id,sumvect)
##   print("--- %s saving time time ---" % (time.time() - start_time))
