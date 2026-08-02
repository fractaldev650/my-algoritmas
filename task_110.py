n=int(input())
p=1
i=1
for i in range(1,n,2):
  p=1/(p+i+1)
print(p)
