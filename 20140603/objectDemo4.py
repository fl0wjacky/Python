#! /usr/bin/env python
# coding:utf-8
# Program:
# 	about __init__()
#	__init__()是一个特殊方法。Python有一些特殊方法。Python会特殊对待它们。特殊方法的特点是名字前后有连个下划线。
# 	如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。这个过程也叫 初始化。

from objectDemo import Bird
class happyBird(Bird):
	def __init__(self, more_words):
		print 'We are happy birds.',more_words

if __name__ == "__main__":
	summer = happyBird('Happy,Happy!')
