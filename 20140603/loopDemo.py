#! /usr/bin/env python
# coding:utf-8

S = 'abcdefghijk'
for i in range(0, len(S), 2):
	print S[i]

for (index, char) in enumerate(S):	#enumerate()在每次循环中，返回的时一个包括2个元素的元组，分别赋予index和char
	print index,char

#zip() 每次循环时从等长序列中分别取出一个元素
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta, tb, tc):
	print (a,b,c)
zipped = zip(ta, tb)
print zipped,type(zipped)
na, nb = zip(*zipped)
print na,nb
