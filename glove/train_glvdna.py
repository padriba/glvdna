import configargparse
from configparser import ConfigParser
from build_corpus_from_scratch import buid_corpus
import os







def main():
    argp = configargparse.get_argument_parser()
    argp.add_argument('--vocab-file', help="File containing vocabulary (truncated unigram counts, produced by 'vocab_count');", default='output_vocab.txt')
    argp.add_argument('--save-file', help="Filename, excluding extension, for word vector output;", default='output_vectors')
    argp.add_argument('--memory', help="Soft limit for memory consumption, in GB -- based on simple heuristic, so not extremely accurate;",type=float, default=4.0)
    argp.add_argument('--vocab-min-count', help='Lower limit such that words which occur fewer than <int> times are discarded.', type=int, default=5)
    argp.add_argument('--vect-size', help='Dimension of word vector representations (excluding bias term);', type=int, default=50)
    argp.add_argument('--max-iter', help='Number of training iterations;', type=int, default=15)

    argp.add_argument('--window-size', help='Number of context words to the left (and to the right, if symmetric = 1);', type=int, default=15)
    argp.add_argument('--num-threads', help="Number of threads;",type=int, default=8)  
    argp.add_argument('--inputs', help='FASTA files', default=None)
    argp.add_argument('--k-low', help='k-mer start range (inclusive)', type=int, default=7)
    argp.add_argument('--k-high', help='k-mer end range (inclusive)', type=int, default=8)
    args = argp.parse_args()


    if(not args.inputs):
       print("--inputs parameter is mandatory.")
    else:
            #buid corpus
            print("Build corpus .....")
            buid_corpus(args.k_low,args.k_high,args.inputs)
            print("End .....")
            
            print("Training model .....")
            #train glove model
            config_file = open("demo_custome.sh", "r")
            list_of_lines = config_file.readlines()
            for k in range (0,len(list_of_lines)): 
                if list_of_lines[k].startswith("VOCAB_FILE="):
                      list_of_lines[k] ="VOCAB_FILE="+ args.vocab_file+"\n" 

                if list_of_lines[k].startswith("SAVE_FILE="):
                      list_of_lines[k] ="SAVE_FILE="+ args.save_file+"\n"  

                if list_of_lines[k].startswith("MEMORY="):
                      list_of_lines[k] ="MEMORY="+ str(args.memory)+"\n" 

                if list_of_lines[k].startswith("VOCAB_MIN_COUNT="):
                      list_of_lines[k] ="VOCAB_MIN_COUNT="+ str(args.vocab_min_count)+"\n"
         
                if list_of_lines[k].startswith("VECTOR_SIZE="):
                      list_of_lines[k] ="VECTOR_SIZE="+ str(args.vect_size)+"\n" 

                if list_of_lines[k].startswith("MAX_ITER="):
                      list_of_lines[k] ="MAX_ITER="+ str(args.max_iter)+"\n"

                if list_of_lines[k].startswith("WINDOW_SIZE="):
                      list_of_lines[k] ="WINDOW_SIZE="+ str(args.window_size)+"\n"

                if list_of_lines[k].startswith("NUM_THREADS="):
                      list_of_lines[k] ="NUM_THREADS="+ str(args.num_threads)+"\n"

            config_file = open("demo_custome.sh", "w")
            config_file.writelines(list_of_lines)
            config_file.close()
            
            #must be tested for different OS
            os.system("sh demo_custome.sh")







if __name__ == '__main__':
    main()
