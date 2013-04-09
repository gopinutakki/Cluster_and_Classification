import math, token__

news = {}


def idf(news):
    tok = token__.tokenize(news)
    text = []
    for i in tok:
        text += list(set(tok[i]))

    idf = {}
    for word in text:
        idf[word] = math.log(float(len(text)) / float(text.count(word))) / math.log(2)
    return idf

vec = []


def idf_optimal(news):
    c = idf(news)
    print len(c)
    wordlist = c.keys()
    tmp = []
    for word in wordlist:
        tmp.append((word, c[word]))
    tmpsorted = sorted(tmp, key=lambda x: x[1])
    idf_o = {}
    for word in tmpsorted[len(tmp) / 10:]:
        idf_o[word[0]] = word[1]
    print len(idf_o)
    return idf_o


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
            matrix[t][wordlist.index(i)] = (1 + math.log(tok[label[t]].count(i))) * c[i]

    #normalization
    for i in matrix:
        normalize(matrix[i])

    return matrix


def tfidf_optimal(news):
    c = idf_optimal(news)
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
            if i in wordlist:
                matrix[t][wordlist.index(i)] = (1 + math.log(tok[label[t]].count(i))) * c[i]

    #normalization
    for i in matrix:
        normalize(matrix[i])
    return matrix


