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
    with open('./idf.txt', 'w') as f:
        f.writelines(str(idf))
    f.close()
    return idf

vec = []


def idf_optimal(news):
    c = idf(news)

    wordlist = c.keys()
    tmp = []
    for word in wordlist:
        tmp.append((word, c[word]))
    tmpsorted = sorted(tmp, key=lambda x: x[1])
    idf_o = {}
    for word in tmpsorted[len(tmp) / 10:]:
        idf_o[word[0]] = word[1]

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

    for t in label:
        matrix[t] = []
        for word in range(len(c)):
            matrix[t].append(0)

    for t in label:
        for i in tok[t]:
            matrix[t][wordlist.index(i)] = (1 + math.log(tok[t].count(i))) * c[i]

    #normalization
    for i in matrix:
        normalize(matrix[i])
    with open('./tf.txt', 'w') as f:
        for i in matrix:
            f.write(str(matrix[i]) + '\n')
    f.close()
    return matrix


def tfidf_optimal(news):
    c = idf_optimal(news)
    wordlist = c.keys()
    tok = token__.tokenize(news)
    label = tok.keys()
    matrix = {}

    for t in label:
        matrix[t] = []
        for word in range(len(c)):
            matrix[t].append(0)

    for t in label:
        for i in tok[t]:
            if i in wordlist:
                matrix[t][wordlist.index(i)] = tok[t].count(i) * c[i]

    #normalization
    for i in matrix:
        normalize(matrix[i])
    with open('./tf.txt', 'w') as f:
        for i in matrix:
            f.write(str(matrix[i]) + '\n')
    f.close()
    return matrix


def idf_knn(news, category):
    tok = token__.tokenize2(news, category)
    text = []
    for topic in tok:
        for i in tok[topic]:
            text += list(set(tok[topic][i]))

    idf = {}
    for word in text:
        idf[word] = math.log(float(len(text)) / float(text.count(word))) / math.log(2)
    print len(idf)
    return idf


def tfidf_knn(news, category):
    c = idf_knn(news, category)
    wordlist = c.keys()
    tok = token__.tokenize2(news, category)
    label = tok.keys()
    matrix = {}
    print 'hello'
    for topic in label:
        matrix[topic] = {}
        for t in tok[topic].keys():
            matrix[topic][t] = []
            for i in range(len(c)):
                matrix[topic][t].append(0)
    print 'world'
    for topic in label:
        for i in tok[topic].keys():
            for word in tok[topic][i]:
                if word in wordlist:
                    matrix[topic][i][wordlist.index(i)] = tok[topic][i].count(i) * c[word]
    print 'today'
    #normalization
    for topic in matrix:
        for i in matrix[topic]:
            normalize(matrix[topic][i])
    return matrix

