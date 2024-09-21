#assume boysis odd and girl is even
n=int(input())
boys=0
girls=0
for i in range(1,n+1):
    if int(i)%2==0:
        girls=girls+int(i)
    else:
        boys=boys+int(i)
print("the sum of boys is",boys,"and the sum of the girls",girls)
