__author__ = 'hiroki'

import theano
import numpy as np

theano.config.floatX = 'float32'
np.random.seed(0)


if __name__ == '__main__':
    import argparse
    import train
    import test
    import predict

    parser = argparse.ArgumentParser(description='Train/Test SRL tagger.')

    parser.add_argument('-mode', default='predict', help='train/test/predict')
    parser.add_argument('--train_data', default="data/conll05st-release/test-set-wsj.txt", help='path to training data')
    parser.add_argument('--dev_data',default="data/conll05st-release/test-set-wsj.txt",  help='path to dev data')
    parser.add_argument('--test_data', default="data/conll05st-release/test-set-brown.txt", help='path to test data')
    parser.add_argument('--predict_data', default="predict.txt", help='path to input to be predicted')

    # NN architecture
    parser.add_argument('--unit',  default='gru', help='Unit')
    parser.add_argument('--vocab',  type=int, default=100000000, help='vocabulary size')
    parser.add_argument('--emb',    type=int, default=32,        help='dimension of embeddings')
    parser.add_argument('--window', type=int, default=5,         help='window size for context')
    parser.add_argument('--hidden', type=int, default=128,        help='dimension of hidden layer')
    parser.add_argument('--layer',  type=int, default=4,         help='number of layers')

    # training options
    parser.add_argument('--save', type=bool, default=False, help='parameters to be saved or not')
    parser.add_argument('--init_emb', default="data/senna/senna.txt", help='Initial embedding to be loaded')
    parser.add_argument('--opt', default='adam', help='optimization method')
    parser.add_argument('--lr1', type=float, default=0.01, help='learning rate')
    parser.add_argument('--lr2', type=float, default=0.01, help='learning rate')
    parser.add_argument('--reg', type=float, default=0.0005, help='L2 Reg rate')
    parser.add_argument('--batch', type=int, default=8, help='batch size')
    parser.add_argument('--epoch', type=int, default=500, help='number of epochs to train')
    parser.add_argument('--no-shuffle', action='store_true', default=False, help='don\'t shuffle training data')
    parser.add_argument('--model', default="train_dir/Layer-4_Dim-128_Batch-8_Hidden-128_Reg-0.000500_Epoch-2.pkl.gz", help='path to model')
    parser.add_argument('--arg_dict', default="train_dir/arg_dict-67.pkl.gz", help='path to arg dict')
    parser.add_argument('--train_dir', default='train_dir/', help='path to train dir')

    argv = parser.parse_args()

    if argv.mode == 'train':
        train.main(argv)
    elif argv.mode =='predict':
        assert argv.model is not None
        assert argv.arg_dict is not None
        assert argv.predict_data is not None
        predict.main(argv)
    else:
        assert argv.model is not None
        assert argv.arg_dict is not None
        test.main(argv)
