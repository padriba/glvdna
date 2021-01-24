This is an example of using **glvdna** to represent the low complexity data from the CAMI challenge
# Installation
1- Clone the ```glvdna``` repository: ```git clone https://github.com/padriba/glvdna.git``` \

# Training the model

```sh
    cd glvdna/glove/ 
    
    python3 train_glvdna.py --inputs example/input/
 ```
# Embedding representation of CAMI dataset
```sh
    cd glvdna/glove/ 
    mv  output_vectors.txt example/
    cd example/
    python3 vectorise.py
 ```
