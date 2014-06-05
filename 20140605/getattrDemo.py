#! /usr/bin/env python
# coding:utf-8
# __getattr__(self,name)可查询即时生成的属性。当我们查询一个属性时，如果通过__dict__方法无法找到该属性，那么Python会调用对象的__getattr__方法，来即时生成该属性
# 每个特性需要自己的处理函数，而__getattr__可以将所有的即使生成属性放在同一个函数中处理
# Python中还有一个__getattribute__特殊方法，哦鸟个与查询任一属性。__getattr__只能用来查询不在__dict__系统中的属性
class Bird(object):
	feather = True

class Chicken(Bird):
	fly = False
	def __init__(self, age):
		self.age = age
	def __getattr__(self, name):
		if name == "adult":
			if self.age > 1.0 : return True
			else: return False
		else: raise AttributeError(name)

summer = Chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)

print(summer.male)
