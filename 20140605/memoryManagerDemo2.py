#! /usr/bin/env python
# coding:utf-8
#在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count)
#可以使用sys包中的getrefcount()来查看某个对象的引用计数。注意：当时用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。因此，getrefcount()所得到的结果，会比期望的多1
from sys import getrefcount
a = [1, 2, 3]
print(getrefcount(a))
b = a
print(getrefcount(a))


#Python的一个容器类(container),比如表、词典等，可以包含多个对象。实际上，容器对象中包含的并不是元素对象本身，是指向各个元素的引用
class from_obj(object):
	def __init__(self, to_obj):
		self.to_obj = to_obj

b = [1, 2, 3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))
print globals()
print globals()['a']
#对象引用对象，是Python最基本的构成方式。即使是a = 1这一赋值方式，实际上是让词典的一个键值"a"的元素引用整数对象1.
#该词典对象用于记录所有的全局引用。我们可以通过globals()函数来查看该词典
a = [1, 2, 3]
print(getrefcount(a))
b = [a, a]
print(getrefcount(a))
