#! /usr/bin/env python
# coding:utf-8
# 闭包（closure)是函数式变成的重要的语法结构
def line_conf():
	def line(x):
		return 2*x + 1
	print(line(5))	# within the scope

line_conf()
#print(line(5))		# out of the scope

def line_conf2():
	def line2(x):
		return 2*x + 1
	return line2 	# return a function object
my_line = line_conf2()
print(my_line(5))

b = 5
def line_conf3():
	b = 15				# b为line3的环境变量
	def line3(x):
		return 2*x + b
	return line3
my_line2 = line_conf3()
print(my_line2(5))
# 一个函数和它的环境遍历那个合在一起，就构成一个闭包（closure），在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中。
def line_conf4():
	b = 15
	c = 10
	def line4(x):
		return 2*x + b + c
	return line4	# return a function object

b = 5
my_line3 = line_conf4()
print(my_line3.__closure__)
print(my_line3.__closure__[0].cell_contents)
print(my_line3.__closure__[1].cell_contents)
print "type of my_line3.__closure__ ==> ",type(my_line3.__closure__)
# __closure__是一个元组，每个元素是cell类型的对象

def line_conf5(a, b):
	def line5(x):
		return a*x + b
	return line5
line1 = line_conf5(1, 1)
line2 = line_conf5(4, 5)
print(line1(5), line2(5))
# 闭包有效地减少了函数所需定义的参数数目。这对于并行运算来说有着重要的意义。
