def isprime(n):   #creating the function
    if n > 1:
        for i in range(2,n):
            if (n%i)==0:
                return False
        else:    
            return True

p=isprime(45)  #function calling
print(p)

