#!/usr/bin/env python3
"""The multiplication_table function prints the results of a number passed to
it multiplied by 1 through 5. An additional requirement is that
the result is not to exceed 25, which is done with the break statement."""
def multiplier(num):
 i=1
 while i<=5:
   if (i*num)>25:
    break
   else:
    print(str(num)+"*"+str(i)+"="+str(i*num))
    i=i+1
multiplier(3)
multiplier(2)
multiplier(4)
multiplier(10)
