#! /usr/bin/env python
# coding:utf-8
# 如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错

def test_func():
	try:
		m = 1/0
	except NameError:
		print("Catch NameError in the sub-function")

try:
	test_func()
except ZeroDivisionError:
	print('Catch error in the main program')
