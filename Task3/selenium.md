# Task3（2天）
## 3.1 安装selenium并学习
#### 1.安装selenium并学习
##### 1.1selenium介绍：
selenium是一款支持多种语言、多种浏览器和多个平台的开源web自动化测试软件，测试人员可以用python、java等语言编写自动化测试脚本，使得浏览器可以完全按照脚本运行，大大节省测试人员用鼠标点击测试浏览器的时间。
##### 1.2安装selenium和chromedriver：
安装selenium非常简单，可以用pip或conda，由于本人的python环境在Anaconda下，所以采用conda安装selenium，命令如下：
`conda install selenium`
chromedriver是Chrome浏览器的webdriver，**只有安装了chromedriver，才能使用selenium.webdriver打开Chrome浏览器**，Mac下安装chromedriver的方法：
**首先查看Chrome浏览器版本：**
![](https://s2.ax1x.com/2019/08/11/ev9w8A.png)
然后进入[http://npm.taobao.org/mirrors/chromedriver/](http://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chromeddriver
##### 1.3测试selenium
```
from selenium import webdriver
browser=webdriver.Chrome()#打开谷歌浏览器
browser.get("http://www.baidu.com")#打开百度网址
browser.find_element_by_id("kw").send_keys("selenium")#定位到输入框并输入关键字
browser.find_element_by_id("su").click()#定位到搜索框并点击搜索      
browser.maximize_window()#最大化浏览器窗口
browser.set_window_size(480,800)#设置浏览器窗口尺寸
browser.forward()#浏览器前进
browser.back()#浏览器后退        
browser.close()#浏览器关闭
browser.quit()#浏览器退出
```
输入以上代码，如果可以进行以上操作则selenium安装成功。

#### 2.使用selenium模拟登陆163邮箱
使用selenium模块可以让浏览器完全按照脚本运行，需要注意的点是邮箱账号登陆框对应在iframe标签中，想要定位查找账号输入元素，需要使用selenium提供的switch_to.frame()方法切换进入frame标签中，对应代码在这里：[code](https://github.com/lijinze9456yy000/Reptile_Learning/blob/master/Task3/open_163mail.py)
![](https://s2.ax1x.com/2019/08/11/evyBrD.png)
**成功进入163邮箱：**
![](https://s2.ax1x.com/2019/08/11/ev6ndH.png)
**PS:163邮箱直通点:**
https://mail.163.com/ 。

## 3.2 学习IP相关知识
#### 1.学习什么是IP，为什么会出现IP被封，如何应对IP被封的问题。
对于同一个IP在一段时间内具有大量同类型的访问，这个IP就会被封。
##### 如何应对IP被封
有几种套路：
1.使用本机ip并修改请求头（**主要修改用户代理User-Agent**），模拟真实用户向浏览器访问web；
2.使用代理IP并轮换访问；
3.使用本机ip设置访问时间间隔；

#### 2.抓取西刺代理，并构建自己的代理池。
目的：发送请求时使用代理ip并轮换访问，防止自己的ip被封
将验证可用的代理ip保存到文件中，供今后使用。
**代码如下：**
```
import requests
from bs4 import BeautifulSoup as bs
def get_html(url):
    headers={
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.baidu.com',
    'Connection': 'keep-alive'
    }
    #通用代码框架
    try:
        response=requests.get(url,headers=headers)
        #不是200抛出异常:HTTPError，是200返回None
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        return response.text
    except:
        return "产生异常"
   
def get_ip(text):
    #beautifulsoup的元素定位方法：find()、find_all()、select()
    ip_list=[]
    soup=bs(text,'html.parser')
    proxy_ips=soup.find(id='ip_list').find_all('tr')
    for proxy_ip in proxy_ips:
        if (len(proxy_ip.select('td'))>=8):
            ip=proxy_ip.select('td')[1].text
            port=proxy_ip.select('td')[2].text
            protocol=proxy_ip.select('td')[5].text
            if protocol in ('HTTPS','HTTP'):
                #用大括号{}表示被替换的字段
                ip_list.append(f'{protocol}://{ip}:{port}')
    return ip_list
def check_ip(ip):
    url='http://www.baidu.com'
    headers={
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3'
    }
    try:
        proxies={}
        #startswith(str):检查字符串是否以指定子字符串开头
        if ip.startswith('HTTPS'):
            proxies['https']=ip
        else:
            proxies['http']=ip
        #检查代理ip是否可用
        #timeout用作设置响应时间，响应时间包括连接时间和读取时间
        response=requests.get(url,headers=headers,proxies=proxies,timeout=10)
        #抛出异常
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        if response.status_code==200:
            print("有效ip："+ ip)
            with open('valid_proxy_ip.txt','a') as f:
            f.writelines(ip)
            return True
        else:
            print("无效ip："+ ip)
            return False
    except:
        print("无效ip: " + ip)
        return False

if __name__=='__main__':
    url='https://www.xicidaili.com/'
    html=get_html(url)
    ips=get_ip(html)
    #print(ips)
    #print(len(ips))
    ip_use_list=[]
    for ip in ips:
        result=check_ip(ip)
        if(result):
            ip_use_list.append(result)
    print("有效代理ip：")
    print(ip_use_list)
```
最终运行结果如下：
![](https://s2.ax1x.com/2019/08/12/mpDe2t.png)
有效的ip保存在valid_proxy_ip.txt文件中：
![](https://s2.ax1x.com/2019/08/12/mpgoFS.png)
**PS 3.西刺直通点：**
https://www.xicidaili.com/ 