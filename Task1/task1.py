#学习get与post请求，尝试使用requests或者是urllib用get方法向https://www.baidu.com/发出一个请求，并将其返回结果输出。
import urllib.request
url = 'http://www.baidu.com'
#request是最基本的HTTP请求模块，用来模拟发送请求
response=urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
#返回状态码
print(response.status)
print(response.reason)

#如果请求中需要加入Headers等信息，可以使用Request类来包装请求，再通过urlopen()获取页面
headers={
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.baidu.com',
    'Connection': 'keep-alive'
}
response1=urllib.request.Request(url,headers=headers)
page=urllib.request.urlopen(response1).read()
page=page.decode('utf-8')
print(page)
