n=int(input())
p=0
s=0
i=1
for i in range(1,n+1,2):
  s=s+1/i
  if (i+1)<=n:
    p=p+1/(i+1)
d=p*(-1)
w=s+d
print(w)
