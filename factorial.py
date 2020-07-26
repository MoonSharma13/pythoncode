prod=1
def fact(N):
  for i in range(0,N+1):
    prod*=i
return prod
a=int(input("enter the number: "))
print("the factorial of "a "is"fact(a))
