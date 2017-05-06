#n2nSRL
deep learning approach(s) on Semantic Role Labeling 

## Semantic Role Labeler with Recurrent Neural Networks

### run
```bash
# you can ignore the gzip warning
chmod +x *.sh
./prepare_data.sh
./run.sh
```

This repo contains Theano implementations of the models described in the following paper:
- [End-to-end Learning of Semantic Role Labeling Using Recurrent Neural Networks](http://www.aclweb.org/anthology/P15-1109), ACL 2015

The model gives about F1 = 78.00 on the dev & test set in the following hyperparameter setting:
- word embedding=SENNA, unit=GRU, hidden dimension=128, L2 regularization=0.0005, layers=4

### Data
- CoNLL-2005 Shared Task (http://www.cs.upc.edu/~srlconll/)
- Word Embedding: SENNA (http://ronan.collobert.com/senna/)

#reference
- [Zhou, Jie and Wei Xu. “End-to-end learning of semantic role labeling using recurrent neural networks.” ACL (2015).](http://www.aclweb.org/anthology/P15-1109)

- [Marcheggiani, Diego et al. “A Simple and Accurate Syntax-Agnostic Neural Model for Dependency-based Semantic Role Labeling.” CoRR abs/1701.02593 (2017): n. pag.](https://arxiv.org/pdf/1701.02593.pdf)

