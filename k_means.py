__author__ = 'hanwang'
import random, token__
from tf_idf import tfidf, normalize, tfidf_optimal

k = 0
matrix = {}
news = {}


#random start
def start(k, matrix):
    centroid = []
    seed = []
    while len(seed) < k:
        seed.append(random.randint(0, len(matrix) - 1))
        seed = list(set(seed))

    for i in seed:
        centroid.append(matrix[matrix.keys()[i]])
    return centroid


def start_optimal(k, matrix):
    centroid = []
    seed = []
    threshold = len(matrix) / k
    while len(seed) < k:
        seed.append(random.randint(0, threshold) + len(seed) * threshold)
        seed = list(set(seed))
    print seed
    for i in seed:
        centroid.append(matrix[matrix.keys()[i]])
    return centroid


a = []
b = []


#point multiplication
def multi(a, b):
    product = 0
    for i in range(len(a)):
        product += a[i] * b[i]
    return product


#euclidean distance
def euclidean(a, b):
    product = 0
    for i in range(len(a)):
        product += (a[i] - b[i]) * (a[i] - b[i])
    return product


#k-means algorithm with cosine distance
def kernel_cos(centroid, matrix, k):
    table = []
    for i in range(len(matrix)):
        table.append([])
        for j in range(k):
            table[i].append(0)

    cluster = []

    for i in range(len(matrix)):
        for j in range(k):
            table[i][j] = multi(matrix[matrix.keys()[i]], centroid[j])

    for i in table:
        if sum(i) == 0:
            i[random.randint(0, len(i) - 1)] = 1
        for j in range(len(i)):
            if i[j] == max(i):
                i[j] = 1
            else:
                i[j] = 0

    for i in range(k):
        tmp = []
        for j in range(len(table)):
            if table[j][i]:
                tmp.append(matrix[matrix.keys()[j]])
        cluster.append(tmp)

    for i in cluster:
        print len(i),
    print
    return cluster


#k-means algorithm with euclidean distance
def kernel_euc(centroid, matrix, k):
    table = []
    for i in range(len(matrix)):
        table.append([])
        for j in range(k):
            table[i].append(0)

    cluster = []

    for i in range(len(matrix)):
        for j in range(k):
            table[i][j] = euclidean(matrix[matrix.keys()[i]], centroid[j])

    for i in table:
        for j in range(len(i)):
            if i[j] == min(i):
                i[j] = 1
            else:
                i[j] = 0

    for i in range(k):
        tmp = []
        for j in range(len(table)):
            if table[j][i]:
                tmp.append(matrix[matrix.keys()[j]])
        cluster.append(tmp)

    for i in cluster:
        print len(i),
    print

    for i in centroid:
        print i
    print
    return cluster


#new centroid
def new(cluster):
    new_centroid = []
    for i in range(len(cluster)):
        new_centroid.append([])
        for j in range(len(cluster[0][0])):
            tmp = 0
            for l in range(len(cluster[i])):
                tmp += cluster[i][l][j]
            new_centroid[i].append(tmp)
        normalize(new_centroid[i])
    return new_centroid


#residual sum of squares
def rss(cluster, centroid):
    s = 0
    for i in range(len(cluster)):
        for j in range(len(cluster[i])):
            tmp = 0
            for l in range(len(centroid[i])):
                tmp += (centroid[i][l] - cluster[i][j][l]) * (centroid[i][l] - cluster[i][j][l])
            s += tmp
    return s


def output(cluster, matrix, news):
    iterator = 1
    purity = {}
    for i in cluster:
        purity[iterator] = {}
        print 'cluster ' + str(iterator)
        for j in range(len(i)):
            for n in matrix:
                if matrix[n] == i[j]:
                    for topic in news:
                        if n in news[topic].keys():
                            print '  ' + topic + ': ' + n
                            # purity
                            if topic in purity[iterator]:
                                purity[iterator][topic] += 1
                            else:
                                purity[iterator][topic] = 1
        print
        iterator += 1
    print '================================================================='
    for i in purity:
        print purity[i]
    p = []
    for i in purity:
        tmp = []
        for j in purity[i]:
            tmp.append(purity[i][j])
        p.append(max(tmp))
    print 'purity = ', float(sum(p)) / float(len(matrix))
    #RI
    P = 0
    TP = 0
    for i in range(len(purity.keys())):
        if len(purity[purity.keys()[i]]) > 1:
            P += sum(purity[purity.keys()[i]].values()) * (sum(purity[purity.keys()[i]].values()) - 1) / 2
            for topic in purity[purity.keys()[i]]:
                if purity[purity.keys()[i]][topic] > 1:
                    TP += purity[purity.keys()[i]][topic] * (purity[purity.keys()[i]][topic] - 1) / 2
    FP = P - TP
    N = 0
    for i in range(len(purity.keys()) - 1):
        j = 1
        while i + j < len(purity.keys()):
            N += sum(purity[purity.keys()[i]].values()) * sum(purity[purity.keys()[i + j]].values())
            j += 1
    FPTN = 0
    for i in range(len(news) - 1):
        i += 1
        j = 1
        while i + j != len(news):
            FPTN += len(news[news.keys()[i]]) * len(news[news.keys()[i + j]])
            j += 1
    TN = FPTN - FP
    print 'TP = ', TP, ' TN = ', TN, ' TP + FP =', P, 'TN + FN = ', N
    print 'RI = ' + str(float(TP + TN) / float(P + N))


def kmeans_cos(k, news):
    matrix = tfidf(news)
    centroid = start(k, matrix)
    ii = 0
    while ii < 10:
        cluster = kernel_cos(centroid, matrix, k)
        print rss(cluster, centroid)
        centroid = new(cluster)
        ii += 1
        if ii == 10:
            out = token__.labelize(news)
            output(cluster, matrix, out)


def kmeans_euc(k, news):
    matrix = tfidf(news)
    centroid = start(k, matrix)
    ii = 0
    while ii < 10:
        cluster = kernel_euc(centroid, matrix, k)
        print rss(cluster, centroid)
        centroid = new(cluster)
        ii += 1
        if ii == 10:
            out = token__.labelize(news)
            output(cluster, matrix, out)


def kmeans_optimal(k, news):
    matrix = tfidf(news)
    centroid = start_optimal(k, matrix)
    ii = 0
    while ii < 10:
        cluster = kernel_cos(centroid, matrix, k)
        print rss(cluster, centroid)
        centroid = new(cluster)
        ii += 1
        if ii == 10:
            output(cluster, matrix, news)