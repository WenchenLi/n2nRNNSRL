#!/usr/bin/env bash
mkdir -p train_dir

python main.py -mode train --train_data data/conll05st-release/test-set-wsj.txt --dev_data data/conll05st-release/test-set-wsj.txt --test_data data/conll05st-release/test-set-brown.txt --init_emb data/senna/senna.txt --lr1 .001 --unit gru --layer 4 --hidden 128 --reg 0.0005 --save True --model train_dir/Layer-4_Dim-128_Batch-8_Hidden-128_Reg-0.000500_Epoch-2.pkl.gz  > train_dir/train.log