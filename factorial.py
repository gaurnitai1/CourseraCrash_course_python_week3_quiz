#!/usr/bin/env python3
"""print the first 10 factorials (from 0 to 9) with the corresponding number.
Remember that the factorial of a number is defined as the product of an integer
and all integers before it. For example, the factorial of five (5!) is equal
to 1*2*3*4*5=120"""

def fac(num):
 for x in range(1,num+1):
  sum=1
  for y in range(1,x+1):

   sum=sum*y
  return print(x,sum)
fac(5)
