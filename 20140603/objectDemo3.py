#! /usr/bin/env python
# coding:utf-8
# Program:
# 	How use self

class Human(object):
	laugh = 'hahahaha'
	def show_laugh(self):
		print self.laugh
	def laugh_100th(self):
		for i in range(100):
			self.show_laugh()


if __name__ == "__main__":
	li_lei = Human()
	li_lei.laugh_100th()
