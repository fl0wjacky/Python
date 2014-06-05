#! /usr/bin/env python
# coding:utf-8
# 含参装饰器实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有环境参量的闭包

#a new wrapper layer
def pre_str(pre=''):
	# old decorator
	def decorator(F):
		def new_F(a, b):
			print(pre + "input", a, b)
			return F(a, b)
		return new_F
	return decorator

#get square sum
@pre_str('^_^') 	# ==> square_sum = pre_str('^_^')(square_sum)
def square_sum(a, b):
	return a**2 + b**2

#get square diff
@pre_str('T_T')
def square_diff(a, b):
	return a**2 - b**2

print(square_sum(3, 4))
print(square_sum.__closure__[0].cell_contents)
print(square_diff(3, 4))
print(square_diff.__closure__[0].cell_contents)
