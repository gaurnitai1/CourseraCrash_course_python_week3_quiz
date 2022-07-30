#!/usr/bin/env python3
def print_prime_factor(num):
 i=1
 while i< num:
   if (num%i)==0:
    print(i)
    i=i+1
   else:
    i=i+1
print_prime_factor(10)
