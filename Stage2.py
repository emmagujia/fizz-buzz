#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 3/18/2019 7:38 AM
# @Author: gujia
# @File  : Stage2.py

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n < 1:
        return []
    out_list = []
    for i in range(1, n + 1):
        if (i % 5 == 0 or checkDigit(5, i)) and (i % 3 == 0 or checkDigit(3, i)):
            out_list.append("FizzBuzz")
        elif i % 5 == 0 or checkDigit(5, i):
            out_list.append("Buzz")
        elif i % 3 == 0 or checkDigit(3, i):
            out_list.append("Fizz")
        else:
            out_list.append(str(i))
    return out_list


def checkDigit(a, b):
    if str(b).find(str(a)) != -1:
        return True
    else:
        return False


def main():
    print('\n'.join(fizzBuzz(100)))


main()
