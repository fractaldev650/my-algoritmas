a=int(input())
n=int(input())
p=1
for i in range(n+1):
  p=p*(a-n*i)
print(p)
