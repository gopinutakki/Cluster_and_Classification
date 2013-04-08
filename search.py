import requests

news = {}
topic = ''


def searchnews(topic, news):
    l = topic.split(' ')
    query = '%27'
    for word in l:
        query += word + '%20'
    query = query[:-1] + '7'
    news[topic] = {}
    while len(news[topic]) < 30:
        r = requests.get('https://api.datamarket.azure.com/Bing/Search/News?Query=' + query + '&$format=json&$skip='
                         + str(len(news[topic])) + '&$top=15',
                         auth=('vRPwDpjqDn8sycuI4Ayn3wKAcwHbzIZ/hzYNZcrHRnI=',
                               'vRPwDpjqDn8sycuI4Ayn3wKAcwHbzIZ/hzYNZcrHRnI='))
        for i in r.json()['d']['results']:
            if i['Title'] not in news[topic]:
                news[topic][i['Title']] = i['Description']
            if len(news[topic]) == 30:
                break


def searchcategory(topic, category, news):
    if category not in news:
        news[category] = {}
    news[category][topic] = {}
    while len(news[category][topic]) < 15:
        r = requests.get('https://api.datamarket.azure.com/Bing/Search/News?Query=%27' + topic +
                         '%27&NewsCategory=%27rt_' + category + '%27&$format=json&$skip='
                         + str(2 * len(news[category][topic])) + '&$top=15',
                         auth=('vRPwDpjqDn8sycuI4Ayn3wKAcwHbzIZ/hzYNZcrHRnI=',
                               'vRPwDpjqDn8sycuI4Ayn3wKAcwHbzIZ/hzYNZcrHRnI='))
        for i in r.json()['d']['results']:
            if i['Title'] not in news[category][topic]:
                news[category][topic][i['Title']] = i['Description']
                print  len(news[category][topic])
            if len(news[category][topic]) == 15:
                break