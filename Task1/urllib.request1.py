#使用requests或urllib.request向浏览器模拟发送请求
import urllib.request
from bs4 import BeautifulSoup as bs
def getInfo(url,headers):
    #urllib.request.urlopen()不支持添加headers信息，它默认的用户代理是本机python版本，服务器一下就能识别出这是爬虫
    #要想模拟一个真实用户用浏览器去访问网页，在发送请求的时候会有不同的用户代理
    response=urllib.request.Request(url,headers=headers)
    response1=urllib.request.urlopen(response)
    soup=bs(response1.read().decode('utf-8'),'html.parser')
    print(soup.text)
if __name__=='__main__':
    url="http://news.tsinghua.edu.cn/publish/thunews/index.html"
    headers={
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://info.tsinghua.edu.cn/',
    'Connection': 'keep-alive'
}
    getInfo(url,headers)

