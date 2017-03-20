#!/usr/bin/env bash
#prepare conll 2005 data & senna word embedding
mkdir data && cd data

wget http://ronan.collobert.com/senna/senna-v3.0.tgz
tar -xvzf senna-v3.0.tgz
paste senna/hash/words.lst senna/embeddings/embeddings.txt >senna/senna.txt

wget wget http://www.cs.upc.edu/~srlconll/conll05st-release.tar.gz
tar -xvzf conll05st-release.tar.gz

wget http://www.cs.upc.edu/~srlconll/conll05st-tests.tar.gz
tar -xvzf conll05st-tests.tar.gz

cp ../scripts/* conll05st-release/scripts/
cd conll05st-release
./scripts/make-trainset.sh
./scripts/make-devset.sh
./scripts/make-testset.sh

cd ../
#rm *.gz
cd ../