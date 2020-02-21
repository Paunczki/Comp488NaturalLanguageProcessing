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
# print(stopwords)
store_reviews()

# We now have raw data stored and can split

from sklearn.model_selection import train_test_split

postrainer, poshold = train_test_split(posrev, test_size=0.3, random_state=0)
posdev, postest = train_test_split(poshold, test_size=0.5, random_state=0)

negtrainer, neghold = train_test_split(negrev, test_size=0.3)
negdev, negtest = train_test_split(neghold, test_size=0.5)

# dev = posdev + negdev
# test = postest + negtest

# This will take in parameter of class, and the word you want, also vocab
def prob_word(binaryclass, word, totvocab):
    prob = (binaryclass[word]+1) / (len(binaryclass) + totvocab)
    return prob

from collections import Counter

def train_naive_bayes(postrain, negtrain):
    posbagwords = []
    negbagwords = []
    for line in postrain:
        a = line.split()
        for i in a:
            if i not in stopwords:
                posbagwords.append(i)
    for line in negtrain:
        b = line.split()
        for j in b:
            if j not in stopwords:
                negbagwords.append(j)
    poscounter = Counter(posbagwords)
    negcounter = Counter(negbagwords)
    allwords = poscounter + negcounter
    vocab = len(allwords)
    # Create probability table for each word given class
    posprob = dict()
    for word in poscounter:
        probword = prob_word(poscounter, word, vocab)
        posprob[word] = probword
    negprob = dict()
    for word in negcounter:
        probword = prob_word(negcounter, word, vocab)
        negprob[word] = probword
    return posprob, negprob
    
    
positiveprobabilities, negativeprobabilities = train_naive_bayes(postrainer, negtrainer)


pwords, nwords = [], []
for word in positiveprobabilities:
    pwords.append(word)
for word in negativeprobabilities:
    nwords.append(word)


def probability_sentence(allwords, polarclass, wordlist):
    percent = 1
    for word in allwords:
        if word in wordlist:
            if isinstance(polarclass, float) or isinstance(polarclass, int):
               continue
            w = polarclass.get(word)
            if w is not None:
                percent *= w 
    return percent
 

# 0 is negative
# 1 is positive
def naive_bayes_classifier(testset, posprob, negprob, polarity, words):
    tot, correct = 0,0
    percentages = []
    for line in testset:
        tot+=1
        bagwords = []
        a = line.split()
        for i in a:
            if i not in stopwords:
                bagwords.append(i)
        # Here I need to calculate probabilities for each
        posp = probability_sentence(bagwords, posprob, words)
        negp = probability_sentence(bagwords, negprob, words)
        if (posp > negp) and (polarity == 1):
            correct += 1
        elif (posp < negp) and (polarity == 0):
            correct += 1
        percentages.append([posp, negp])

        # now I want to create a function to see at least 10 fold differnce between the values to 
        
    percent = correct / tot
    return percent, percentages


pp, ppview = naive_bayes_classifier(posdev, positiveprobabilities, negativeprobabilities, 1, pwords)
pn, pnview = naive_bayes_classifier(negdev, positiveprobabilities, negativeprobabilities, 0, nwords)

print(pp)
print(pn)
