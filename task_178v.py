n=int(input())
t=0
f=0
for i in range(n):
  k=int(input())
  if k%2==0 and k>=100:
      p=(k**0.5)%2
      if p==0:
              t=t+1
  else:
      if k<100 and k%2==0:
          p=((k**0.5)*1000)%1000
          if p==0:
                    f=f+1
g=f+t
print(g)
