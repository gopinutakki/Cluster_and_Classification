__author__ = 'hanwang'
import naive, json
from eva import classify
training = {}
guess = {}

if __name__ == '__main__':
    category = ['Business', 'Entertainment', 'Politics']
    f = open('./training.json')
    training = json.load(f)
    f.close()

    f = open('./guess.json')
    guess = json.load(f)
    f.close()

    p = naive.not_naive(training, category)
    classify(guess, p, category)