#! /usr/bin/env python
# coding:utf-8
# Program:
# 	abount Dictionary
# 	词典的元素包含有两部分，键和值，常见的是以字符串来表示键，也可以使用数字或者真值
# 	来表示键（不可变的对象可以作为键）。值可以是任意对象。键和值两者一一对应。
# 	词典元素没有顺序。你不能通过下标引用元素。词典是通过键来引用。

dic = {'tom':11, 'sam':57, 'lily':100}
print dic,type(dic)
print dic['tom']
dic['tom'] = 30
print dic

#构建一个新的空词典
dic = {}
print dic
#在词典中增添一个新元素
dic['lilei'] = 99
print dic
#词典元素的循环调用
dic = {'lilei':90, 'lily':100, 'sam':57, 'tom':90}
for key in dic:
	print key,dic[key]


print dic.keys()
print dic.values()
print dic.items()
del dic['lilei']
print dic
print len(dic)
dic.clear()
print dic
