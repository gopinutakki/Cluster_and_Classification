__author__ = 'hanwang'
import naive, token__
from search import searchcategory
from eva import classify
news = {}
guess = {}

if __name__ == '__main__':
    category = ['Business', 'Entertainment', 'Politics']
    training = [['bing', 'amazon', 'twitter', 'yahoo', 'google'],
              ['beyonce', 'bieber', 'television', 'movies', 'music'],
              ['obama', 'america', 'congress', 'senate', 'lawmakers']]
    test = ['apple', 'facebook', 'westeros', 'gonzaga', 'banana']
    for c in category:
        for t in training:
            for i in t:
                searchcategory(i, c, news)
    p = naive.bayes(news, category)

    for c in category:
        for t in test:
            searchcategory(t, c, guess)
    classify(guess, p, category)