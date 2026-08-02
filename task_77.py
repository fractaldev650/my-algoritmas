from math import *
n=int(input())
f=0
k=0
p=1
for i in range(1,n+1):
  k=k+sin(i)
  f=f+cos(i)
  p=p*(f/k)
print(p)
