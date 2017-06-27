#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2017/1/12 18:32:45        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：官方域名的内容爬取还有待更新 √ ━━━━━☆*°☆*°
"""
import urllib2
import urllib
import cookielib
import codecs
import process_data
import allrequest_data
import class_process_data
import time
global sum,xh
import UI
sum=0
xh=0
def get_info_0():
	global xh
	cookie=cookielib.CookieJar()
	handle=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(handle)
	#实际上教务网没有cookie验证，为了规范还是写上去
	postdata=urllib.urlencode(allrequest_data.data['学生选课'])
	req = urllib2.Request(allrequest_data.url2['学生选课'],headers=allrequest_data.headers['学生选课'])
	response = opener.open(req)
	html=response.read()
	html=html.decode("gb2312")
	outputFp = codecs.open("d:\\0test.txt", 'w', 'gbk')
	outputFp.write(html)
	outputFp.flush()
	outputFp.close()
	class_process_data.get_table("d:\\0test.txt")
	req = urllib2.Request(allrequest_data.url2['学生选课'], postdata,headers=allrequest_data.headers['学生选课'])
	response = opener.open(req)
	html = response.read()
	html = html.decode("gb2312")
	outputFp = codecs.open("d:\\0test.txt", 'w', 'gbk')
	outputFp.write(html)
	outputFp.flush()
	outputFp.close()
	class_process_data.get_table("d:\\0test.txt")
	UI.tell_Success(xh)
# get_info()
def get_info_1():
	global xh
	cookie=cookielib.CookieJar()
	handle=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(handle)
	#实际上教务网没有cookie验证，为了规范还是写上去
	postdata=urllib.urlencode(allrequest_data.data['2016'])
	req = urllib2.Request(allrequest_data.url2['2016'],postdata,headers=allrequest_data.headers['2016'])
	response = opener.open(req)
	html=response.read()
	html=html.decode("gb2312")
	outputFp = codecs.open("d:\\0test.txt", 'w', 'gbk')
	outputFp.write(html)
	outputFp.flush()
	outputFp.close()
	process_data.get_table("d:\\0test.txt")
	UI.tell_Success(xh)

def get_info_2():
	global xh
	cookie=cookielib.CookieJar()
	handle=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(handle)
	#实际上教务网没有cookie验证，为了规范还是写上去
	postdata=urllib.urlencode(allrequest_data.data_3['2017'])
	req = urllib2.Request(allrequest_data.url3['2017'],postdata,headers=allrequest_data.headers['2017_3'])
	response = opener.open(req)
	html=response.read()
	html=html.decode("gb2312")
	outputFp = codecs.open("d:\\0test.txt", 'w', 'gbk')
	outputFp.write(html)
	outputFp.flush()
	outputFp.close()
	process_data.get_table("d:\\0test.txt")
	UI.tell_Success(xh)

def get_info_3():
	global xh
	cookie=cookielib.CookieJar()
	handle=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(handle)
	#实际上教务网没有cookie验证，为了规范还是写上去
	postdata=urllib.urlencode(allrequest_data.data['专业选修'])
	req = urllib2.Request(allrequest_data.url3['专业选修'],postdata,headers=allrequest_data.headers['专业选修'])
	response = opener.open(req)
	html=response.read()
	html=html.decode("gb2312")
	outputFp = codecs.open("d:\\0test.txt", 'w', 'gbk')
	outputFp.write(html)
	outputFp.flush()
	outputFp.close()
	class_process_data.get_table("d:\\0test.txt")
	UI.tell_Success(xh)

def update_info():
	global sum
	global xh
	xh=1
	print 'Successfully login in and acquire the data'
	get_info_2()
	cnt=0
	while True:
		time.sleep(1)
		cnt=cnt+1
		print '第',cnt,'次查询期末成绩数据,暂无更新'
		if cnt%20==0:
			break
		t=get_info_2()
		if not sum:
			sum=t
		if t>sum:
			print '第', cnt, '次查询期末成绩数据,你有成绩更新了！'
			UI.tell_update()
			break
	UI.tell_Success(2)

# update_info()
def update_info_30s():
	global sum
	global xh
	xh=1
	print 'Successfully login in and acquire the data'
	get_info_2()
	cnt=0
	while True:
		#实际上会有延迟 所以此处设置为20s
		time.sleep(20)
		cnt=cnt+1
		print '第',cnt,'次查询期末成绩数据,暂无更新'
		t=get_info_2()
		if not sum:
			sum=t
		if t>sum:
			print '第', cnt, '次查询期末成绩数据,你有成绩更新了！'
			UI.tell_update()
			break
