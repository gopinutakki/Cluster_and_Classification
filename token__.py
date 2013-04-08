__author__ = 'hanwang'
import re

news = {}


def tokenize(news):
    tok = {}
    for topic in news:
        for title in news[topic].keys():
            tmp = []
            tmp += re.findall(r"[a-z']+", title.lower())
            tmp += re.findall(r"[a-z']+", news[topic][title].lower())
            tmp += re.findall(r"[a-z']+", news[topic][title].lower())
            tok[title] = tmp

    return tok


def tokenize2(news, category):
    tok = {}
    for i in range(len(category)):
        tok[i] = tokenize(news[category[i]])

    return tok


def labelize(news):
    iterator = 0
    lab = {}
    for topic in news:
        lab[topic] = {}
        for title in news[topic].keys():
            lab[topic][title] = iterator
            iterator += 1
    return lab
