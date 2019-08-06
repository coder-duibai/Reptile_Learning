# **Task1**
> Task1要求
> 1. 学习get与post请求
> 2. 正则表达式

**1.1 get和post请求**   
1.学习get与post请求，尝试使用requests或者是urllib用get方法向https://www.baidu.com 发出一个请求，并将其返回结果输出。
```
import urllib.request  
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
print(response.getcode())
```

2.如果是断开了网络，再发出申请，结果又是什么。了解申请返回的状态码。 
如果断开了网络再发出申请吗，会返回URLError。
状态码告知从服务器返回的请求结果。
`1XX`:信息性状态码，接收的请求正在处理。
`2XX`:成功状态码，请求正常处理完毕。
`3XX`:重定向状态码，需要进行附加操作以完成请求。
`4XX`:客户端错误状态码，服务器无法处理请求。
* 400:服务器不理解请求的语法。
* 403:服务器拒绝请求。
* 404:服务器找不到请求的网页。
`5XX`:服务器错误状态码，服务器处理请求出错。
