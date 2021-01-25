This is an example of using **glvdna** to represent the low complexity data from the CAMI challenge
# Installation
1- Clone the ```glvdna``` repository: ```git clone https://github.com/padriba/glvdna.git``` \

# Training the model

- Downlaod the fasta file from this [link](https://dl.dropbox.com/s/h1p92jngrp15mop/low.fasta?dl=1)
- Create an ```input``` folder in your home directory, and copy ```low.fasta``` in the ```input``` folder

```sh
    cd glvdna/glove/ 
    
    python3 train_glvdna.py --inputs ~/input/
 ```
# Embedding representation of CAMI dataset
```sh
    cd glvdna/glove/ 
    mv  output_vectors.txt example/
    cd example/
    python3 vectorise.py
 ```
this will creat a file named```output_vectorisation.tsv```. This file contains the embedding representation the low complexity dataset.

# k-means custering and plotting
```sh
python3 replace_seq_ids_by_taxa_ids.py
python3 output_by_rank.py species
python3 clustering_k_means.py

```

