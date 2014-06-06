#! /usr/bin/env python
# coding:utf-8
# 两个对象可能相互引用，从而构成所谓的引用环(reference cycle)
# 引用环会给垃圾回收机制带来很大的麻烦
# 即使是一个对象，只需要自己引用自己，也能构成引用环
import objgraph
from sys import getrefcount

a = []
b = [a]
a.append(b)
print(getrefcount(a))
print(getrefcount(b))
objgraph.show_refs([a], filename='memoryManagerDemo4_a.png')
objgraph.show_refs([b], filename='memoryManagerDemo4_b.png')

c = []
c.append(c)
print(getrefcount(c))
objgraph.show_refs([c], filename='memoryManagerDemo4_c.png')
