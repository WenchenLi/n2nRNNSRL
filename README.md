#n2nSRL
deep learning approach(s) on Semantic Role Labeling 

## Semantic Role Labeler with Recurrent Neural Networks

### run
```bash
# you can ignore the gzip warning
chmod +x *.sh
./prepare_data.sh
./train.sh
```

### training output
notice the fact with limited data and wsj corpus and brown corpus are different
```bash
Epoch: 160
	Index:  100	Time: 57.226235 seconds
	Average Negative Log Likelihood: 0.111926
	Train Accuracy: 0.999139
	Index:  1000 2000 3000 4000 5000	Time: 40.484402 seconds
	Dev Accuracy: 0.999099
	Props: 5267	P total: 14055.000000	R total: 14077.000000	Correct: 13975.000000
	Precision: 0.994308	Recall: 0.992754	F1: 0.993530
	### Best Dev F Score: 0.993708  Epoch: 157 ###
	Index: 	Time: 5.371451 seconds
	Test Accuracy: 0.737695
	Props: 804	P total: 2060.000000	R total: 2177.000000	Correct: 1008.000000
	Precision: 0.489320	Recall: 0.463023	F1: 0.475808
	### Best Test F Score: 0.482759  Epoch: 157 ###
```

### Data
- CoNLL-2005 Shared Task (http://www.cs.upc.edu/~srlconll/)
- Word Embedding: SENNA (http://ronan.collobert.com/senna/)

### Notice
1. the original conll05 is not public available, the training are performed on test-wsj set and can achieve F1 score around 99%, 
which shows the learning capability of the model.

2. you can try your own word embedding, the required format is 1st colunm is the word, the rest is the corresponding vector.

3. With your own training: to avoid overfitting, try use higher L2 Reg rate, larger batch size and more annotated data.


#### how to label your own data for training
please follow [CoNLL-2005 Shared Tasks Semantic Role Labeling](http://www.lsi.upc.edu/~srlconll/)
to label your training data.

Notes on chinese training data, 
according to [this page](http://www.lsi.upc.edu/~srlconll/spec.html), on Format section Target column, 
chinese predicates are the same with the word itself. 

#### how to run prediction
under predict.txt, we have 2 same sentences with 1st one the labeled sentence for training, dev and testing,
 2nd one as the prediction format. Under main.py, the default argv is for prediction, you can simply run main
 to see how it predict the result given the input as in predict.txt(output as Predict-result.txt).

you can easily write a script to pipline the prediction process by :
1. has a tagger do POS finding the verbs(predicated)
2. put the base form(finds->find) to the target column 5th column as shown in predict.txt example, for chinese it is
    the same as the word itself.

#reference
- [Zhou, Jie and Wei Xu. “End-to-end learning of semantic role labeling using recurrent neural networks.” ACL (2015).](https://arxiv.org/pdf/1701.02593.pdf)


