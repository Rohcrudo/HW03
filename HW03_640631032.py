# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""
def complay(n,m):
     n = n-m
     print("Computer, take",m)
     if(n==0):
        print(str + " win")
     else:
        print("There are ",n,"sticks in the pile.")
     return n

n = int(input("How many sticks (N) in the pile: "))
print("There are ",n ,"sticks in the pile.")
str = input("What is your name : ")
while n > 0:
  m = int(input(str+", how many sticks you will take (1 or 2):  "))
  if m>2 :
    print("No you cannot take more than 2 sticks!")
  elif m<1:
    print("No you cannot take more less than 1 stick!")
  elif m>n:
    print("There are no enough sticks to take.")
  elif n-m==0:
    n = n-m
    print("Computer win")
  else:
    n = n-m
    print("There are ",n,"sticks in the pile.")
    if n>1:
        if (n+2-1)%3==0:
           n = complay(n,1)
        elif (n+2-2)%3==0:
           n = complay(n,2)
        elif n%2==0:
           n = complay(n,1)
        elif n%2!=0:
           n = complay(n,2)
    else:
        if n-1==0:
           n = n-1
           print("Computer, take a last sticks")
           print(str + " win")
