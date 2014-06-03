#! /usr/bin/env python
# coding:utf-8
# Program:
# 	内置函数dir()和help(),list为Python的一个内置类

print dir(list)
help(list)

nl = [1,2,5,3,5]
print nl.count(5)
print nl.index(3)
nl.append(6)
print nl
nl.sort()
print nl
print nl.pop()
nl.remove(2)
print nl
nl.insert(0,9)
print nl

print [1,2,3] + [5,6,9] # 运算符，比如+,-,>,<,以及下标引用[start:end]等等，从根本上都是定义在类内容部的方法。
#print [1,2,3] - [3,4]

class superList(list):
	def __sub__(self, b):
		a = self[:]
		b = b[:]
		while len(b) > 0:
			element_b = b.pop()
			if element_b in a:
				a.remove(element_b)
		return a

if __name__ == "__main__":
	a = superList([1,2,3])
	b = superList([3,4])
	print 
	print a
	print b
	print a - b
	print a
	print b
