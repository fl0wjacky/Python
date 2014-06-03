#! /usr/bin/env python
# coding:utf-8
# 什么是循环对象？
# 循环对象是这样一个对象，它包含有一个next()方法（__next__()方法，在Python3.x中),这个方法的目的是进行到下一个结果，而在结束一系列结果之后，举出StopIteration错误。


def gen():		#生成器，编写方法和函数定义类似，只是在return的地方改成yield,生成器中可以有多个yield,当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield，生成器自身又构成一个循环器，每次循环使用一个yield返回的值。
	a = 100
	yield a
	a = a*8
	yield a
	yield 1000

for i in gen():	#gen()生成器用作循环器时，会进行3次循环。
	print i

G = (x for x in range(4)) #生成器表达式
L = [x**2 for x in range(10)] #表推导(list comprehension)

x1 = [1, 3, 5]
y1 = [9, 12, 15]
L  = [ x**2 for (x,y) in zip(x1, y1) if y > 10]
print L
