# coding:utf-8

a = 1

def change_integer(a):
	a = a + 1
	return a

print change_integer(a)
print a

#===(Python中“#”后面跟的内容是注释，不执行)

b = [1,2,3]

def change_list(b):
	b[0] = b[0] + 1
	return b

print change_list(b)
print b
