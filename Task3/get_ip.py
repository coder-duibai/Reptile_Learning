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
            ip_use_list.append(ip)
    print("有效代理ip：")
    print(ip_use_list)

 