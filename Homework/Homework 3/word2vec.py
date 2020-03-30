'''
Question 1
'''

# implements word2vec from gensim
# https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.test.utils import datapath
from gensim import utils
import pandas as pd

class MyCorpus(object):
    # print("hello")
    def __iter__(self):
        corpus_path = datapath('lee_background.cor') # Path to corpora
        for line in open(corpus_path):
            yield utils.simple_preprocess(line)

import gensim.models

sentences = MyCorpus()
lee_model = gensim.models.Word2Vec(sentences=sentences)

lee_model.save('Homework/Homework 3/lee')
lee_model = gensim.models.Word2Vec.load('Homework/Homework 3/lee')

vec_king = lee_model.wv['king']

for i,word in enumerate(lee_model.wv.vocab):
    if i == 3: # Top n words
        break
    print(word)

# This was the basic tutorial provided and now I need to train on my own model
# I will us MASC download from the anc
# I just combined all jokes to one file called alljokes.txt

class mascCorpus(object):
    def __iter__(self):
        corpus_path =  'data/masc_500k_texts/written/jokes/alljokes.txt'
        for line in open(corpus_path): 
            yield utils.simple_preprocess(line)

sentences = mascCorpus()
jokes_model = gensim.models.Word2Vec(sentences=sentences)

jokes_model.save('Homework/Homework 3/jokes')
jokes_model = gensim.models.Word2Vec.load('Homework/Homework 3/jokes')

vec_little = jokes_model.wv['little']
vec_had = jokes_model.wv['had']
vec_title = jokes_model.wv['title']
vec_girl = jokes_model.wv['girl']

print(jokes_model.similarity('little', 'girl'))
print(jokes_model.similarity('had', 'title'))
print(jokes_model.similarity('little', 'title'))
print(jokes_model.similarity('www', 'girl'))

#print(jokes_model.evaluate_word_pairs('Homework/Homework 3/jokes'))

# for i,word in enumerate(jokes_model.wv.vocab):
#     if i == 3: # Top i words
#         break
#     print(word)

'''
Question 2
'''

import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

for i, word in enumerate(wv.vocab):
    if i == 10:
        break
    print(word)


print("\nGoogle car pairs:")
car_pairs = [
    {'car', 'minivan'}, {'car', 'bicycle'}, {'car', 'airplane'}, {'car', 'cereal'}, {'car', 'communism'},
]

for w1,w2 in car_pairs:
    print('%r\t%r\t%.2f' % (w1,w2,wv.similarityw1,w2))

print(wv.most_similar(positive=['car', 'minivan'], topn=5))

print(wv.doesnt_match(['fire', 'water', 'land', 'sea', 'air', 'car']))

