#! /usr/bin/env python
# coding:utf-8
# 列表可以通过引用其元素，改变对象本身。这种对象类型，称为可变数据对象(mutable object),词典也是这样的数据类型
# 而数字、字符串、元组（尽管可以引用元素，但不可以赋值），不能改变对象本身，只能改变引用的指向，称为不可变数据对象（immutable object)
# 函数的参数传递，本质上传递的是引用。
# 动态类型是Python的核心机制之一

def f(x):
	x = 100
	print x

def f2(x):
	x[0] = 100
	print x

a = 1
f(a) 	# 调用函数f(x),引用x指向引用a的指向，x被重定向，不影响a
print a

b = [1,2,3]
f2(b) # 传递可变（mutable）对象，改变函数参数，有可能改变原对象。
print b
