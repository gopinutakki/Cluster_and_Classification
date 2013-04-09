__author__ = 'hanwang'
import rocchio, json

news = {}


if __name__ == '__main__':
    f = open('./news.json')
    news = json.load(f)
    f.close()

    k = raw_input('input an integer k: ')
    k = int(k)
    k = rocchio.rocchio(k, news)