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

