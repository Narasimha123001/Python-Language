n=int(input())
ans=1
if n==0:
    print(1)
elif n<0:
    print("Error")
else:
    for i in range(1,n+1):
        ans=ans*i
    print(ans)