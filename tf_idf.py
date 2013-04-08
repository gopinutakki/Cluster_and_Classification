import math, token__

news = {}


def idf(news):
    tok = token__.tokenize(news)
    text = []
    for i in tok:
        text += tok[i]

    idf = {}
    for word in text:
        idf[word] = math.log(float(len(text)) / float(text.count(word))) / math.log(2)
    return idf

vec = []


def normalize(vec):
    denom = 0
    for i in range(len(vec)):
        denom += vec[i] * vec[i]
    denom = math.sqrt(denom)
    for j in range(len(vec)):
        vec[j] = vec[j] / denom


def tfidf(news):
    c = idf(news)
    wordlist = c.keys()
    tok = token__.tokenize(news)
    label = tok.keys()
    matrix = {}

    for t in range(len(tok)):
        matrix[t] = []
        for word in range(len(c)):
            matrix[t].append(0)

    for t in range(len(label)):
        for i in tok[label[t]]:
            matrix[t][wordlist.index(i)] = tok[label[t]].count(i) * c[i]

    #normalization
    for i in matrix:
        normalize(matrix[i])

    return matrix




