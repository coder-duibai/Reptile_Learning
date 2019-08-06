from urllib import request
import re



def douban250(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36' 
    }

    req = request.Request(url, headers = headers)
    resp = request.urlopen(req)
    return resp.read().decode('utf-8')
#a = douban250('https://movie.douban.com/top250?start=')
#print(a)


if __name__ == "__main__":

    result = []

    for i in range(10):
        url = 'https://movie.douban.com/top250?start='
        url += str(25*i)
        r = douban250(url)

        NUM = re.findall('<em class="">(.*?)</em>' ,r)
        NAME = re.findall('<img width="100" alt="(.*?)" src=', r)
        YEAR = re.findall('(\d+)&nbsp;/&nbsp;', r)
        DIRECTOR = re.findall('导演: (.*?)&nbsp;&nbsp;&nbsp', r)
        COUNTRY = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp', r)
        PROPERTY = re.findall('<span class="rating_num" property="v:average">(.*)</span>', r)


        z = zip(NUM, NAME, YEAR, DIRECTOR, COUNTRY, PROPERTY)
        for i in z:
            result.append(i)
    
    with open('douban250.txt', 'w', encoding='utf-8') as f:
        for i in result:
            f.writelines(str(i) + '\n')