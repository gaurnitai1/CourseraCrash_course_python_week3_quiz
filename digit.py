#!/usr/bin/env python3
def digita(num):
    div=(num//10)
    if div==0:
     leng=1
     return print(leng)
    else:
     leng=len(str(div))
     return print((leng+1))
digita(40)
digita(2)
digita(100)
digita(1000)
digita(10000)
