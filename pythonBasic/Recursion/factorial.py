def fact(n):      #creating the function  
    if (n == 0 or n == 1):
        return 1       #if n = 0 or 1 then the value is 1
    else:
        return n * fact(n-1)      # base function(n * fact(n-1))
    
n=int(input("Enter the number : "))
print(fact(n))
