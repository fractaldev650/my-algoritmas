x=2
n=int(input())
s=1
i=1
p=0
for i in range (1,n+1):
  s=+((i+2)/(i+3))*(x**(i+1))
  p=p+((i+1)/(i+2))*(x**i)
d=p*(-1)
w=s+d
print(w)
