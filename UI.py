#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2017/1/9 15:39:54        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：简易查询UI √ ━━━━━☆*°☆*°
"""
import Tkinter as t
import time
import tkFont
import grades
import tkMessageBox
import grades2
import grades3
# root.iconbitmap('c:\\test\\48X48_tk_logo.ico')
global qh
qh=0

def tell_Success(xh):
	if xh==0:
		tkMessageBox.showinfo('Successfully acquire','查询成绩成功，请看控制台窗口输出')
	elif xh==2:
		tkMessageBox.showinfo('Successfully acquire', '查询成绩成功，已每3s持续查询20次,若要继续查询请重新点击')
	# else:
		# tkMessageBox.showinfo('Successfully acquire', '查询成绩成功，将每30s持续更新')
def tell_update():
	tkMessageBox.showinfo('你的成绩！！！','你有新成绩更新了,请看最新成绩表')
def info_0():
	global qh
	tkMessageBox.showinfo('查询大二上学生选课','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xsxk.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121101
Request Method:GET
Status Code:200 OK
Remote Address:110.65.10.235:80
Response Headers
Content-Type:text/html; charset=gb2312
Date:Wed, 11 Jan 2017 15:45:40 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers(伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Connection:keep-alive
Host:110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xs_main.aspx?xh=201530612644 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
xh:HTTP请求时这是你的学号数据
xm:HTTP请求时这是你的姓名utf编码
gnmkdm:N121101(查询页面代码)\n按确定开始爬取数据''')
	if qh==0:
		grades.get_info_0()
	else:
		grades2.get_info_0()
	print 'Successfully login in and acquire the data'

def info_1():
	global qh
	tkMessageBox.showinfo('查询2015-2016大一学年成绩','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605
Request Method:POST
Remote Address:110.65.10.235:80
Response Headers
Cache-Control:private
Content-Length:76306
Content-Type:text/html; charset=gb2312
Date:Thu, 12 Jan 2017 01:27:28 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers (伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:4124
Content-Type:application/x-www-form-urlencoded
Host:110.65.10.235
Origin:http://110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
view URL encoded
xh:HTTP请求时这是你的学号数据
xm:HTTP请求时这是你的姓名utf编码
gnmkdm:N121605(查询页面代码)
\n请按确定开始查询''')
	if qh==0:
		grades.get_info_1()
	else:
		grades2.get_info_1()
	print 'Successfully login in and acquire the data'

def info_2():
	global qh
	tkMessageBox.showinfo('查询2016-2017大二学年成绩','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605
Request Method:POST
Remote Address:110.65.10.235:80
Response Headers
Cache-Control:private
Content-Type:text/html; charset=gb2312
Date:Wed, 11 Jan 2017 15:37:32 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers (伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:20674
Content-Type:application/x-www-form-urlencoded
Host:110.65.10.235
Origin:http://110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
view URL encoded
xh:HTTP请求时这是你的学号数据
xm:HTTP请求时这是你的姓名utf编码
gnmkdm:N121605(查询页面代码)\n请按确定开始查询''')
	if qh==0:
		grades.get_info_2()
	elif qh==1:
		grades2.get_info_2()
	else:
		grades3.get_info_2()
	print 'Successfully login in and acquire the data'

def info_3():
	global qh
	tkMessageBox.showinfo('查询大二专业选修课','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xsxk.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121101
Request Method:POST
Status Code:200 OK
Remote Address:110.65.10.235:80
Response Headers
Cache-Control:private
Content-Length:21975
Content-Type:text/html; charset=gb2312
Date:Thu, 12 Jan 2017 01:30:34 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers (伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:14737
Content-Type:application/x-www-form-urlencoded
Host:110.65.10.235
Origin:http://110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xsxk.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121101 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
view URL encoded
xh:HTTP请求时这是你的学号数据
xm:HTTP请求时这是你的姓名utf编码
gnmkdm:N121101(查询页面代码)\n请按确定开始查询''')
	if qh==0:
		grades.get_info_3()
	elif qh==1:
		grades2.get_info_3()
	else:
		grades3.get_info_3()
	print 'Successfully login in and acquire the data'

def update_info():
	global qh
	tkMessageBox.showinfo('已开启自动查询功能，每3s发送HTTP请求','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605
Request Method:POST
Remote Address:110.65.10.235:80
Response Headers
Cache-Control:private
Content-Type:text/html; charset=gb2312
Date:Wed, 11 Jan 2017 15:37:32 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers (伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:20674
Content-Type:application/x-www-form-urlencoded
Host:110.65.10.235
Origin:http://110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
view URL encoded
xh:201530612644
xm:(unable to decode value)
gnmkdm:N121605\n请按确定开始进入3s自动获取模式（有更新时提醒）''')
	if qh==1:
		grades2.update_info()
	else:
		grades.update_info()

def update_info_30s():
	global qh
	tkMessageBox.showinfo('已开启自动查询功能，每3s发送HTTP请求','''Request URL:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605
Request Method:POST
Remote Address:110.65.10.235:80
Response Headers
Cache-Control:private
Content-Type:text/html; charset=gb2312
Date:Wed, 11 Jan 2017 15:37:32 GMT
Server:Microsoft-IIS/6.0
X-AspNet-Version:1.1.4322
X-Powered-By:ASP.NET
Request Headers (伪装浏览器查询的header参数,√的为重要参数)
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:20674
Content-Type:application/x-www-form-urlencoded
Host:110.65.10.235
Origin:http://110.65.10.235 √
Referer:http://110.65.10.235/(fjom1245jzafvjimgfcdewqc)/xscjcx.aspx?xh=201530612644&xm=%C8%C4%BA%C6%B4%CF&gnmkdm=N121605 √
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 √
Query String Parameters
view URL encoded
xh:201530612644
xm:(unable to decode value)
gnmkdm:N121605\n请按确定开始进入3s自动获取模式（有更新时提醒）''')
	if qh==1:
		grades2.update_info_30s()
	else:
		grades.update_info_30s()

def change_tube():
	global qh
	if qh==0:
		qh=1
		tkMessageBox.showinfo("Successfully change", '已成功切换至外网备用域名通道http://110.65.10.235/(3t3xo1jj22lvv3eeyixqzxai)/,可重新查询')
	elif qh==1:
		qh=2
		tkMessageBox.showinfo("Successfully change", '已成功切换至官方域名通道http://110.65.10.219/(1gyjdp450azudpexcktha345),可重新查询')
	else:
		qh=0
		tkMessageBox.showinfo("Successfully change", '已成功切换至官方域名通道http://110.65.10.235/(fjom1245jzafvjimgfcdewqc),可重新查询')
if __name__=='__main__':
	root=t.Tk()
	root.title('教务系统成绩/课程小爬虫V2.0')
	tkMessageBox.showinfo('关于V2.0版本新特性','比1.0版本多了备用域名通道(可能还会更新)\n增加了自动更新提醒(新成绩)\n谷歌探查关键数据标记\n两种模式 3s or 30s更新查询\n新增定时提示功能')
	root.geometry('565x180')
	root.iconbitmap('d:\\123.ico')
	ft = tkFont.Font(family='Fixdsys', size=16, weight=tkFont.NORMAL)
	ftt_ln=tkFont.Font(family='Tempus Sans ITC', size=14,weight=tkFont.BOLD)
	ft2 = tkFont.Font(family='Comic Sans MS', size=15, weight=tkFont.BOLD)
	ft22 = tkFont.Font(family='Comic Sans MS', size=12, weight=tkFont.BOLD)
	ft21 = tkFont.Font(family='Comic Sans MS', size=10, weight=tkFont.BOLD)
	ft20 = tkFont.Font(family='Comic Sans MS', size=8, weight=tkFont.BOLD)
	# for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
	t.Button(root, text='自动查询周期:\n30s*∞', borderwidth=2, relief=t.GROOVE, width=10, font=ft22,command=update_info_30s).grid(row=1,column=1,columnspan=1,rowspan=2)
	t.Label(root, text=' ', font=ft2).grid(row=0, column=2, rowspan=4)
	t.Button(root,text='2015-2016\n大一成绩',borderwidth=2, relief=t.SOLID,width=10,font=ft2,command=info_1).grid(row=3,column=1,columnspan=1)
	t.Button(root, text='自动查询周期:\n3s*∞', borderwidth=2, relief=t.GROOVE, width=10, font=ft22,command=update_info).grid(row=1,column=5,columnspan=1,rowspan=2)
	t.Button(root, text='切换备用通道', borderwidth=2, relief=t.SOLID, width=10,font=ft21,command=change_tube).grid(row=1, column=3,rowspan=1)
	t.Button(root, text='2016-2017\n大二成绩', borderwidth=2, relief=t.SOLID, width=10,font=ft2,command=info_2).grid(row=2, column=3,rowspan=4)
	t.Label(root, text=' ', font=ft2).grid(row=0, column=4, rowspan=4)
	t.Button(root, text='大二学生选课\n(已选)', borderwidth=2, relief=t.SOLID, width=10,font=ft2,command=info_0).grid(row=3, column=5)
	t.Label(root, text=' ', font=ft2).grid(row=0, column=6, rowspan=4)
	t.Label(root, text='Copyright © 2017 All rights reserved by Haocong', font=ft22).grid(row=0, columnspan=8)
	t.Button(root, text='Quit', command=root.quit,borderwidth=2, relief=t.SOLID, width=10,font=ft2).grid(row=1, column=7)
	t.Button(root, text='大二专业选修\n(总表)', borderwidth=2, relief=t.SOLID, width=10,font=ft2,command=info_3).grid(row=2, column=7,rowspan=2)
	root.mainloop()
	# 'Tempus Sans ITC', 14

