__author__ = 'Wenchen Li'

import sys
import time
import theano
from utils import load_conll, load_init_emb, get_id_samples, convert_data_test, output_results, load_data, count_correct, f_measure

# import nltk

def main(argv):
    print '\nSYSTEM START'
    print '\nMODE: Predict'
    print '\nRECURRENT HIDDEN UNIT: %s\n' % argv.unit

    print '\tINITIAL EMBEDDING\t %s' % argv.init_emb
    print '\tNETWORK STRUCTURE\tEmb Dim: %d  Hidden Dim: %d  Layers: %d' % (argv.emb, argv.hidden, argv.layer)

    """ load corpus"""
    print '\n\tCorpus Preprocessing...'

    # sentence = "Scotty accepted the decision with indifference and did not enter the arguments"
    #
    # def count_predicate(pos,sentence):
    #     count = 0
    #     for i, s in enumerate(sentence.split(" ")):
    #         tag = pos[i]
    #         print s, tag
    #         if tag[1] in ["VB", "VBZ", "VBD", "VBG", "VBN", "VBP"]:  # predicates or verb
    #             count +=1
    #     return count
    #
    # def sentence_to_conll_pred(sentence):
    #     seperator = "\t"
    #     placeholder = "*"
    #     st = nltk.stem.lancaster.LancasterStemmer()
    #     pos = nltk.pos_tag(sentence)
    #
    #     NUM_PROPS = count_predicate(pos,sentence)
    #     print NUM_PROPS
    #     nltk.download('averaged_perceptron_tagger')
    #     with open("to_be_predicted.txt", 'w') as f:
    #         for i,s in enumerate(sentence.split(" ")):
    #             tag = pos[i]
    #             print s,tag
    #             if tag in ["VB","VBZ","VBD","VBG","VBN","VBP"]:#predicates or verb
    #                 target = st.stem(s)
    #             else:
    #                 target = "-"
    #             line = [s] + [placeholder] * 3 + [target] + [placeholder]* NUM_PROPS
    #             f.write(seperator.join(line)+"\n")
    # sentence_to_conll_pred(sentence)
    # predict_corpus = load_conll("to_be_predicted.txt")

    predict_corpus = load_conll(argv.predict_data)
    print '\tTest Sentences: %d' % len(predict_corpus)

    """ load initial embedding file """
    print '\n\tInitial Embedding Loading...'
    init_emb, vocab_word = load_init_emb(init_emb=argv.init_emb)
    print '\tVocabulary Size: %d' % vocab_word.size()

    """ load arg dict """
    print '\n\targ dict Loading...'
    arg_dict = load_data(argv.arg_dict)
    print '\tLabel size: %d' % arg_dict.size()

    """ convert words into ids """
    print '\n\tConverting Words into IDs...'
    #prd = TARGETs for chinese is the same word but for english,
    # they has find and finds, the target word is find for finds
    #   TARGET"The target verbs of the sentence, in infinitive form.
    # for english , for an online product to parse ,we need to parse the syntax
    # first to get the verbs as pottential targets, then send into the system as prds to predict
    te_id_sents, te_id_ctx, te_marks, te_prds, test_y, _ = get_id_samples(predict_corpus,
                                                                                      vocab_word=vocab_word,
                                                                                      a_dict=arg_dict)

    """ convert formats for theano """
    print '\n\tCreating  Samples...'
    test_sample_x, test_sample_y = convert_data_test(te_id_sents, te_prds, te_id_ctx, te_marks, test_y, init_emb)

    """ load tagger"""
    print '\nModel Loading...'
    tagger = load_data(argv.model)

    print '\nTheano Code Compiling...'
    # like tensorflow , theano is static graph,
    # for prediction tagger.d, tagger.error need to be an place holder
    predict_model = theano.function(
        inputs=[tagger.x, tagger.d],
        outputs=[tagger.y_pred, tagger.errors],
        mode='FAST_RUN',
    )

    predicts = predict(predict_model, test_sample_x, test_sample_y)
    output_results(predict_corpus, te_prds, arg_dict, predicts,'Predict-result.txt')


def predict(model, sample_x, sample_y):

    start = time.time()
    predicts = []

    # sample_y = [[i*sample_x[0].shape[1]] for i in xrange(len(sample_x))]
    sample_index = 0
    for index in xrange(len(sample_x)):
        batch_x = sample_x[index]
        batch_y = sample_y[index]

        for b_index in xrange(len(batch_x)):
            sample_index += 1
            if sample_index % 100 == 0:
                print '%d' % sample_index,
                sys.stdout.flush()

            # a = batch_y[b_index]
            pred, _ = model([batch_x[b_index]],[batch_y[b_index]])
            predicts.append(pred[0])

    end = time.time()
    print '\tTime: %f seconds' % (end - start)

    return predicts

