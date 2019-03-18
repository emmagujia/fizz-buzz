#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 3/18/2019 7:42 AM
# @Author: gujia
# @File  : Stage1.py


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n < 1:
        return []
    out_list = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out_list.append("FizzBuzz")
        elif i % 5 == 0:
            out_list.append("Buzz")
        elif i % 3 == 0:
            out_list.append("Fizz")
        else:
            out_list.append(str(i))
    return out_list


def main():
    print('\n'.join(fizzBuzz(100)))


main()
