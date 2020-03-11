# implements word2vec from gensim
# https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html

from gensim.test.utils import datapath
from gensim import utils

class MyCorpus(object):
    # print("hello")
    def __iter__(self):
        corpus_path = datapath('lee_background.cor')
        for line in open(corpus_path):
            yield utils.simple_preprocess(line)


import gensim.models

sentences = MyCorpus()
model = gensim.models.Word2Vec(sentences=sentences)

vec_king = model.wv['king']

for i,word in enumerate(model.wv.vocab):
    if i == 10:
        break
    print(word)

