n=int(input())
t=0
for i in range(n):
  k=int(input())
  if k%3==0 and k%5!=0:
    t=t+1
print(t)
