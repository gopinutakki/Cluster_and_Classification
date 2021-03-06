__author__ = 'hanwang'
import token__, math
news = {}


def bayes(news, category):
    tok = token__.tokenize2(news, category)
    text = []
    text_c = {}
    s = []
    for i in range(len(tok)):
        tmp = 0
        text_c[i] = []
        for doc in tok[i]:
            text += tok[i][doc]
            text_c[i] += tok[i][doc]
            tmp += len(tok[i][doc])
        s.append(tmp)
    text = list(set(text))
    p = {}
    for word in text:
        p[word] = {}
        for i in range(len(text_c)):
            p[word][i] = math.log(float(text_c[i].count(word) + 1) / float(s[i] + len(text)))
    return p


def not_naive(news, category):
    tok = token__.tokenize2(news, category)
    text = []
    text_c = {}
    text_raw = []
    s = []
    for i in range(len(tok)):
        tmp = 0
        text_c[i] = []
        for doc in tok[i]:
            text += tok[i][doc]
            text_c[i] += tok[i][doc]
            text_raw += tok[i][doc]
            tmp += len(tok[i][doc])
        s.append(tmp)
    text = list(set(text))
    p = {}
    for word in text:
        p[word] = {}
        for i in range(len(text_c)):
            p[word][i] = math.log(float(text_c[i].count(word) + 1) / float(s[i] + len(text)))

    p_optimal = {}
    for word in p:
        for i in p[word].keys():
            if p[word][i] == max(p[word].values()):
                a = text_c[i].count(word)
                c = text_raw.count(word) * 0.5
                if a >= c:
                    p_optimal[word] = {}

    for word in p_optimal:
        for i in range(len(text_c)):
            p_optimal[word][i] = p[word][i]

    return p_optimal


