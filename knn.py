__author__ = 'hanwang'
import token__
import tf_idf
from k_means import multi
news = {}
guess = {}
tok = {}
vec = []


def determine(vec):
    s = []
    d = ''
    for i in vec:
        s.append(vec.count(i))
    for i in vec:
        if vec.count(i) == max(s):
            d = i
    return d


def nearest(vec, tok, k):
    dist = []
    neighbours = []
    for topic in tok:
        for i in range(len(tok[topic].keys())):
            dist.append((topic, multi(vec, tok[topic][tok[topic].keys()[i]])))

    sortdist = sorted(dist, key=lambda x: x[1])[len(dist) - k:]
    for item in sortdist:
        neighbours.append(tok.keys()[item[0]])
    d = determine(neighbours)
    return d


def knn(guess, news, category, k):
    c = tf_idf.idf_knn(news, category)
    wordlist = c.keys()
    g = token__.tokenize2(guess, category)
    n = tf_idf.tfidf_knn(news, category)
    gmatrix = {}
    for topic in g:
        gmatrix[topic] = {}
        for t in g[topic]:
            gmatrix[topic][t] = []
            for i in range(len(c)):
                gmatrix[topic][t].append(0)

    for topic in g:
        for t in g[topic]:
            for word in g[topic][t]:
                if word in c:
                    gmatrix[topic][t][wordlist.index(word)] = g[topic][t].count(word) * c[word]
    gneighbour = {}
    for topic in gmatrix:
        gneighbour[topic] = {}
        for t in gneighbour[topic]:
            gneighbour[topic][t] = nearest(gmatrix[topic][t], n, k)

    for topic in gneighbour:
        print topic
        for t in gneighbour[topic]:
            print t, gneighbour[topic][t]
