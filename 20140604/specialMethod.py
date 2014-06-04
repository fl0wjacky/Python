#! /usr/bin/env python
# coding:utf-8
# 特殊方法名的前后各有两个下划线,特殊方法又被称为魔法方法(magic method),定义了许多Python语法和表达方式。可通过dir()查看

print 'abc' + 'xyz'
print 'abc'.__add__('xyz')

print (1.8).__mul__(2.0)
print True.__or__(False)

print len([1,2,4])
print [1,2,4].__len__()

print (-1).__abs__()
print (2.3).__int__()

li = [1,2,3,4,5,6]
print li[3]
print li.__getitem__(3)
li.__setitem__(0,10)
print li

di = {'a':1, 'b':2}
print di
di.__delitem__('a')
print di
del di['b']
print di

# 在Python中，函数也是一种对象。实际上，任何一个有__call__()特殊方法的对象都被当作是函数。
class SampleMore(object):
	def __call__(self, a):
		return a+5

add = xx()
print(add(2))
print map(add, [2, 4, 5])
