from math import *
x=int(input())
n=int(input())
s=0
p=x
for i in range(0,n+1):
  p=sin(p)
  s=s+p
print(s)
