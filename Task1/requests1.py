#requests或urllib.request：向浏览器模拟发送请求
#BeautifulSoup:将html文档转换成树形结构，通俗意思：去除html标签
#selenium:开源web自动化测试软件，通俗意思：与浏览器进行通话，使得浏览器完全按照脚本运行
import requests
from bs4 import BeautifulSoup as bs
def getInfo(url,headers):
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    soup=bs(response.text,'html.parser')
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

