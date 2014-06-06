#! /usr/bin/env python
# coding:utf-8
# 可使用del关键字删除引用

from sys import getrefcount

#删除引用
a = [1, 2, 3]
b = a
print(getrefcount(b))

del a
print(getrefcount(b))

#删除容器元素中的元素
c = [1, 2, 3]
del c[0]
print(c)

#引用指向新对象，旧对象的引用计数减少
d = [1, 3, 5]
e = d
print(getrefcount(e))
d = 2
print(getrefcount(e))
