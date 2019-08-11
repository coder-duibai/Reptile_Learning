# **Task1**
> Task1要求
> 1. 学习get与post请求
> 2. 正则表达式

**1.1 get和post请求**   
1.学习get与post请求，尝试使用requests或者是urllib用get方法向https://www.baidu.com 发出一个请求，并将其返回结果输出。见代码[task1.py](https://github.com/lijinze9456yy000/Reptile_Learning/blob/master/Task1/task1.py)
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

3.了解什么是请求头，如何添加请求头
HTTP请求报文由三部分组成：请求行、请求头和请求体。
请求行包含请求方法（get和post是最常见的请求方法）、请求URL和HTTP协议及版本号。
请求头包含若干属性，服务器据此获取客户端信息，常见的属性名：
* Accept：客户端告诉服务器接收什么类型的响应。
* Cookie：对请求进行标识，客户端将cookie发送给服务器端。
* Referer：记录请求来源于哪个url地址。

4. 学习什么是正则表达式并尝试一些正则表达式并进行匹配
正则表达式是一种特殊的字符串模式，用于匹配一组字符串。
 字符簇：[a-z]:匹配字符a到字符z中任意字符
        [0-9]:匹配数字0到数字9中任意字符
        [^a-z]:匹配除字符a到字符z中任意字符
        [^0-9]:匹配除数字0到数字9中任意字符
