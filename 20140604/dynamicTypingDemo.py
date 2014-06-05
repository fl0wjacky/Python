#! /usr/bin/env python
# coding:utf-8
# 对象是储存在内存中的实体。但我们并不能直接接触到该对象。我们在程序中写的对象名，只是指向这一对象的引用（reference).
# 引用和对象分离，是动态类型的核心。引用可以随时指向一个新的对象：
a = 3
print a
a = 'at'
print a

a = 5
print a
b = a
print b
a = a + 2
print a,b

L1 = [1,2,3]
L2 = L1
print L1,L2
L1 = 1
print L1,L2

L1 = [4,5,6]
L2 = L1
print L1,L2
L1[0] = 10
print L1,L2
