#! /usr/bin/env python
# coding:utf-8
# 特殊方法名的前后各有两个下划线

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
