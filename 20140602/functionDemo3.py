#! /usr/bin/env python 
# coding:utf-8
# 闰年：年份是整百数时，必须是400的倍数才是闰年；不是400的倍数的年份，即使是4的倍数也是平年。
# 这就是通常所说的：四年一闰，百年不闰，四百年再闰。

def leap_year(y,m,d):
	if y%4==0 and (y%100 != 0 or y%400 == 0):
		return True
	else:
		return False

print leap_year(1992,1,1)
print leap_year(2000,1,1)
print leap_year(2100,1,1)
