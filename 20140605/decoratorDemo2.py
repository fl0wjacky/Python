#! /usr/bin/env python
# coding:utf-8
#

def decorator(F):
	def new_F(a, b):
		print('input', a, b)
		return F(a, b)
	return new_F

#get square sum
@decorator
def square_sum(a, b):
	return a**2 + b**2

#get square diff
@decorator
def square_diff(a, b):
	return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))

# 等效过程
#	square_sum = decorator(square_sum)
#	square_sum(3, 4)
# Python中的变量名和对象是分离的。变量名可以指向任意一个对象。从本质上讲，装饰器起到的就是这样一个重新指向变量名的作用(
# name binding),让同一个变量名指向一个新返回的可调用对象，从而达到修改可调用对象的目的。 
