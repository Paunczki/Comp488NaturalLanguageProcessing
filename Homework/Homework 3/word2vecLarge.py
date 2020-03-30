from gensim.test.utils import datapath
from gensim import utils
import pandas as pd
import gensim.models
import gensim.downloader as api

wv = api.load('word2vec-google-news-300')

'''
Question 3
'''

gold = 'data/wordsim353_sim_rel/wordsim_similarity_goldstandard.txt'
gold_std = []
for line in open(gold).readlines():
    gold_std.append(line.split())

google = []
for row in gold_std:
    w1 = row[0]
    w2 = row[1]
    sim = row[2]
    mod_sim = wv.similarity(w1,w2)
    google.append([w1,w2, mod_sim])

print("Number of examples: " + str(len(google)))

s = pd.DataFrame(gold_std)
m = pd.DataFrame(google)

google_spearman = pd.concat((s.iloc[:,2],m.iloc[:,2]),axis=1)

from scipy.stats import spearmanr

google_corr = spearmanr(google_spearman)
print("Google News: " + str(google_corr))

lee_sim = []
for row in gold_std:
    w1 = row[0]
    w2 = row[1]
    sim = row[2]
    try:
        model_sim = lee_sim.wv.similarity(w1,w2)
        lee_sim.append([w1,w2, mod_sim])
    except KeyError:
        print(F"{w1} or {w2} word does not appear in this model")

print("Number of examples: " + str(len(lee_sim)))

s = pd.DataFrame(gold_std)
m = pd.DataFrame(lee_sim)

lee_spearman = pd.concat((s.iloc[:,2],m.iloc[:,2]),axis=1)

from scipy.stats import spearmanr

lee_corr = spearmanr(lee_spearman)
print("Lee: " + str(lee_corr))

'''
Question 4
'''
a1 = ["king - man + woman = " + wv.most_similar(positive = ['king', 'woman'], negative=['man'],topn=4)]
print(a1)
a2 = ["bread + sauce + cheese = " + wv.most_similar(positive = ['bread', 'sauce', 'cheese'], negative=[],topn=4)]
print(a2)
a3 = ["wolf - dog + cat = " + wv.most_similar(positive = ['wolf', 'cat'], negative=['dog'],topn=4)]
print(a3)
a4 = ["mouse + large = " + wv.most_similar(positive = ['mouse', 'large'], negative=[],topn=4)]
print(a4)
a5 = ["Christianity - Jesus = " + wv.most_similar(positive = ['christianity'], negative=['jesus'],topn=4)]
print(a5)
a6 = ["flour + egg + milk = " + wv.most_similar(positive = ['flour', 'milk', 'egg'], negative=[],topn=4)]
print(a6)
a7 = ["turkey - european = " + wv.most_similar(positive = ['turkey'], negative=['european'],topn=4)]
print(a7)

