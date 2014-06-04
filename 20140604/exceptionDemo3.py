#! /usr/bin/env python
# coding:utf-8
# try->异常->except->finally
# try->无异常->else->finally

try:
	print(a*2)
except TypeError:
	print("TypeError")
except:
	print("Not Type Error & Error noted")
finally:
	print("Hey,I am here!")


print 'Xman'
