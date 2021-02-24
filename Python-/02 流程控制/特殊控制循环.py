#!/usr/bin/python3
# -*- coding:utf-8 -*-
# break是退出循环
# continue 是退出这次循环，马上进行下一次循环，后面的代码都不知行了
for i in range(10):
    if i == 5:
        continue
    print(i)
