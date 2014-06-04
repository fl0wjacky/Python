#! /usr/bin/env python
# coding:utf-8
# 如何主动抛出异常,用raise

def func():
	print 'lalala'
	raise StopIteration
	print 'HaHaHa'

if __name__ == "__main__":
	try:
		func()
	except StopIteration:
		print "Ooooo!Catch you at the main program"
