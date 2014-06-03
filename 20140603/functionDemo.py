#! /usr/bin/env python
# coding:utf-8

def f(a,b,c):
	return a+b+c
def f2(a, b, c=10):			#可以给参数赋予默认值，如果该参数最终没有被传递值，将使用该默认值
	return a+b+c
def f3( *name ):			#包裹传递：所有参数被name收集，根据位置合成一个元组
	print type(name)
	print name
def f4( **dict ):			#包裹传递：参数被合成在dict字典中
	print type(dict)		#包裹传递的关键在于定义函数时，在相应元组或字典前加*或**
	print dict

def f5(a, b, c, *name, **dict):
	print a,b,c
	print name
	print dict

if __name__ == "__main__":
	print f(1,2,3)			#位置传递参数
	print f(c=3, b=2, a=1)	#关键字传递参数
	print f(1, c=3, b=2)	#关键字传递可以和位置传递混用。但位置参数要出现在关键字参数之前

	print f2(3,2)
	print f2(3,2,1)			

	f3(1,4,6)
	f3(5,6,7,1,2,3)

	f4(a=1, b=9)
	f4(m=2, n=1, c=11)

	args = (1, 3, 4)		#解包裹，在传递元组时，让元组的每一个元素对应一个位置参数
	print f(*args)

	dict = {'a':1, 'b':2, 'c':3}
	print f(**dict)				#解包裹，在传递字典时，让字典的每个键值对作为一个关键字传递给函数

	#混用原则：先位置，再关键字，再包裹位置，再包裹关键字
	f5(3, 5, 7, 10, 20, x=50, z=100)
	
#注意：包裹参数和解包裹并不是相反的操作，时两个相对独立的过程。
