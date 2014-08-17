import urllib2
import urllib
import json
from datetime import datetime

ENDPOINT = 'https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q=%s'

def search_keyword(keyword):
    query = keyword.encode('utf-8')
    print('xoxo keyword is ', query)
    resp = urllib2.urlopen(ENDPOINT % urllib.quote(query))
    resp_json = json.load(resp)
    rets = resp_json['responseData']['results']
    for ret in rets:
        print(ret['publishedDate'])
        print(len(ret['publishedDate']))
        ret['date'] = datetime.strptime(ret['publishedDate'][0:25], '%a, %d %b %Y %H:%M:%S')
    return rets

def search(keyworkds):
    ret = []
    for keyword in keyworkds:
        ret.extend(search_keyword(keyword))
    ret.sort(key=lambda item: item['date'], reverse = True)
    for item in ret:
        item['date'] = str(item['date'])
    return ret    

if __name__ == '__main__':
    result = search(['Kobe', 'Leban', 'hah'])
    print(len(result))


