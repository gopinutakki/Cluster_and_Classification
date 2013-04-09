__author__ = 'hanwang'
from k_means import start_optimal, euclidean, new, rss, output
from tf_idf import tfidf
import random, token__

k = 0
matrix = {}
news = {}


def kernel(centroid, matrix, news):
    cluster = []
    for i in range(len(centroid)):
        cluster.append([centroid[i]])
    for i in matrix:
        distance = []
        for j in centroid:
            distance.append(euclidean(matrix[i], j))
        if sum(distance) == 0:
            l = random.randint(0, len(centroid) - 1)
            cluster[l].append(matrix[i])
            cluster[l] = list(set(cluster[l]))
            centroid = new(cluster)
        else:
            for m in range(len(distance)):
                if distance[m] == min(distance) and matrix[i] not in cluster[m]:
                    cluster[m].append(matrix[i])
                    centroid = new(cluster)
    print rss(cluster, centroid)
    out = token__.labelize(news)
    print out
    output(cluster, matrix, out)


def rocchio(k, news):
    matrix = tfidf(news)
    centroid = start_optimal(k, matrix)
    kernel(centroid, matrix, news)
