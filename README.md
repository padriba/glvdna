# Introduction
glvdna is a tool for representation of variable-length DNA sequences using the Global Vectors for Word Representation. It is adapted from the [GloVe](https://github.com/stanfordnlp/GloVe) library.

# Installation
1- Clone the ```glvdna``` repository: ```git clone https://github.com/padriba/glvdna.git``` \
2- The required python version is ```3``` 

# Training embedding model

```sh
    cd glvdna/glove/ 
    # /input/folder/ : input foder, contains fasta files
    python3 train_glvdna.py --inputs $(/input/folder/)
 ```
This will take a couple of hours, depending on the size of the input folder \
If you want to accerate the process you can edit some parameters like ```--memory``` that defines the limit for memory consumption (in GB) \
You can see the list of available arguments and their default values:
```python3 train_glvdna.py --help```

# Embedding representation of a DNA sequence
You can fetch the vector representation of `AAA` with:
```sh
    cd glvdna/glove/ 
    python3 train_glvdna.py -v AAA
 ```
