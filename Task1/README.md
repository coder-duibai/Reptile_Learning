# **Task1**
> Task1要求
> 1. 学习get与post请求
> 2. 正则表达式

**1.1 get和post请求**   
1.学习get与post请求，尝试使用requests或者是urllib用get方法向https://www.baidu.com/发出一个请求，并将其返回结果输出。  
#学习get与post请求，尝试使用requests或者是urllib用get方法向https://www.baidu.com/发出一个请求，并将其返回结果输出。
`import urllib.request
url = 'http://www.baidu.com'
#request是最基本的HTTP请求模块，用来模拟发送请求
response=urllib.request.urlopen(url=url)
#返回response类型
print(type(response))
#返回头部信息
print(response.getheaders())
#返回server信息
print(response.getheader('Server'))
#返回状态码
print(response.status)
#返回状态码
print(response.getcode())`
