#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2017/1/11 17:57:32        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：专业选修课+学生选课html解析 √ ━━━━━☆*°☆*°
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
	mat_str2=r">(.+?)</a>"
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
				if '</a>' in i:
					# print 'YES'
					num=list.index(i)
					new_matstr=re.findall(mat_str2,list[num],re.S | re.M)
					# print new_matstr
					s=''
					if new_matstr:
						for i in new_matstr:
							s=s+str(i)
						list[num]=s
						i=list[num]
				# print cnt,i
				cnt=cnt+1
			grade_list.append(list)
	cnt=0
	for l in grade_list:
		# print cnt,l
		cnt=cnt+1
	x = PrettyTable(['课程代码','课程名称','课程性质','组或模块','学分','周学时','考试时间','课程介绍','选否','余量'])
	cnt = 1
	while grade_list[cnt] and len(grade_list[cnt])==10 :
		# print grade_list[cnt]
		x.add_row(grade_list[cnt])
		cnt = cnt + 1
		if cnt>len(grade_list)-1:
			break
	print x
	return x
## get_table('d:\\0test.txt')
