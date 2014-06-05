#! /sur/bin/env python
# coding:utf-8
# 装饰器(decorator)是一种高级Python语法。装饰器可以对一个函数、方法或者类进行加工

#get square sum
def square_sum(a, b):
	return a**2 + b**2

#get suqare diff
def square_diff(a, b):
	return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))


#modify: print input
#get square_sum
def square_sum2(a, b):
	print('input:',a,b)
	return a**2 + b**2

#get square diff
def square_diff2(a, b):
	print('input:',a,b)
	return a**2 - b**2

print(square_sum2(3, 4))
print(square_diff2(3,4))
