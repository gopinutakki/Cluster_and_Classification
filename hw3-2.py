__author__ = 'hanwang'
import naive, json
#from search import searchcategory
from eva import classify
news = {}
guess = {}

if __name__ == '__main__':
    category = ['Business', 'Entertainment', 'Politics']
    '''training = [['bing', 'amazon', 'twitter', 'yahoo', 'google'],
               ['beyonce', 'bieber', 'television', 'movies', 'music'],
               ['obama', 'america', 'congress', 'senate', 'lawmakers']]
    test = ['apple', 'facebook', 'westeros', 'gonzaga', 'banana']
    for c in category:
        for t in training:
            for i in t:
                searchcategory(i, c, news)
    s = json.dumps(news)
    f = open('./training.json', 'w')
    f.write(s + "\n")
    f.close()

    for c in category:
        for t in test:
            searchcategory(t, c, guess)
    s = json.dumps(guess)
    f = open('./guess.json', 'w')
    f.write(s + "\n")
    f.close()
    '''
    f = open('./training.json')
    news = json.load(f)
    f.close()

    f = open('./guess.json')
    guess = json.load(f)
    f.close()

    p = naive.bayes(news, category)
    classify(guess, p, category)