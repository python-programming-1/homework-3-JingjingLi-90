#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:13:46 2019

@author: jingjingli
"""

def collatz(num):
    if num%2==0:
        num=num//2
        print(num)
        return num
        
    elif num%2==1:
        num =3*num+1
        print(num)
        return num
try: 
    n=int(input('please type a number:'))
    while n != 1:
        n=collatz(n)
except ValueError:
    print('interger please')
        