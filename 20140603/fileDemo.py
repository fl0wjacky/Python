#! /usr/bin/env python
# coding:utf-8
# Program:
# 	file input and output

f = open('test.txt','w')
f.write('tom, 12, 86\n')
f.write('Lee, 15, 99\n')
f.write('Lucy, 11, 58\n')
f.write('Joseph, 19, 56\n')
f.close()

with open('test.txt','r') as f:
	content = f.readlines()
	for line in content:
		print line,		#python2.x print后面加一个逗号避免换行
						#python3.x print后添加 ,end=''


#content = f.read(N) 读取N bytes的数据
#content = f.readline() 读取一行
#content = f.readlines() 读取所有行，储存在列表中，每个元素是一行
#f.write('I like apple') 将‘I like apple'写入文件

