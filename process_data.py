#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2017/1/11 16:57:33        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：教务网成绩html的正则解析 √ ━━━━━☆*°☆*°
"""
import re
import sys
from prettytable import PrettyTable
def get_table(s):
	f=open(s)
	type = sys.getfilesystemencoding()
	temp=f.readlines()
	for line in temp:
		line=line.decode(type).encode('utf-8')
		# print line
	mat_str=r'<td>(.*?)</td>'
	grade_list=[]
	for line in temp:
		m_tr =  re.findall(mat_str,line,re.S|re.M)
		if m_tr:
			list = []
			cnt=0
			for line in m_tr:
				s = line.decode(type).encode('utf-8')
				if s=='&nbsp;':
					list.append('')
					continue
				list.append(s)
			cnt=0
			for i in list:
				# print cnt,i
				cnt=cnt+1
			grade_list.append(list)
	cnt=0
	for l in grade_list:
		# print cnt,l
		cnt=cnt+1
	x = PrettyTable(['学年','学期','课程代码','课程名称','课程性质','课程归属','学分','绩点','成绩','辅修标记','补考成绩','重修成绩','开课学院','备注','重修标记','排名'])
	cnt=2
	cnt = 2
	while grade_list[cnt] and len(grade_list[cnt]) == 16:
		x.add_row(grade_list[cnt])
		cnt = cnt + 1
		if cnt>len(grade_list)-1:
			break
	print x
	return len(grade_list)
	# return x
