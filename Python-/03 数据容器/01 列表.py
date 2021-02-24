#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :  2021/2/24 15:08
# @Author   :  葛柏辰
# @File     :  01 列表.py
# @Software :  PyCharm
"""课件地址：https://zhuanlan.zhihu.com/p/59740559
一、list（列表）
list作为Python中最常用的数据结构之一，与其他编程语言的数组有相似的特点，但是它具有着更为强大的功能，接下来将详细地为大家介绍一下list的所有操作。

（注：tuple元组类型与list类似，但是tuple的元素不能修改；set集合与list也类似，但是集合中的元素是无序的，且会自动除去重复元素）

"""
a = ['a', 'b', 1, True, 1.2]
print(a)
a.append('2')
print(a)
a.remove('2')
print(a)
# 顾左不顾右
print(a[1:-1:2])