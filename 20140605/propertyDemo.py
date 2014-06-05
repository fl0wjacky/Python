#! /usr/bin/env python
# coding:utf-8
# 特性即特殊的属性
# 特性使用内置函数property()来创建。property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。

class num(object):
	def __init__(self, value):
		self.value = value
	def getNeg(self):
		return -self.value
	def setNeg(self, value):
		self.value = -value
	def delNeg(self):
		print("value also deleted")
		del self.value
	
	neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg

# __dict__分层存储属性。每一层的__dict__只存储该层新增的属性。子类不需要重复存储父类中的属性
