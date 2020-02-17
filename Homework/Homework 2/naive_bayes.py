stopwords = []
def stop_words():
    f = open('Homework/Homework 2/stop_words.txt', 'r')
    for line in f.readlines():
        s = line.split('\n')
        stopwords.append(s[0])


posrev = []
negrev = []
def store_reviews():
    fpos = open('data/Movie Polarity/rt-polarity.pos', 'r')
    fneg = open('data/Movie Polarity/rt-polarity.neg', 'r')
    for line in fpos.readlines():
        s = line.split('\n')
        posrev.append(s[0])
    for line in fneg.readlines():
        s = line.split('\n')
        negrev.append(s[0])


stop_words()
store_reviews()

# We now have raw data stored and can split

from sklearn.model_selection import train_test_split

postrain, poshold = train_test_split(posrev, test_size=0.3)
posdev, postest = train_test_split(poshold, test_size=0.5)

negtrain, neghold = train_test_split(negrev, test_size=0.3)
negdev, negtest = train_test_split(neghold, test_size=0.5)

# dev = posdev + negdev
# test = postest + negtest

# Now we can work
# I do not join training since we want to know the polarity


def naive_bayes_classifier():
    print('hi')


'''
s = "one two three one two five"

l = s.split()

set(l)

from collections import Counter

Counter(s.split())
'''
