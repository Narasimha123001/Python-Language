def is_prime(num):
    if num <=1:
        return False
    if num<=3:
        return True
    if num %2 == 0 or num % 3 == 0:
        return False
    i=5
    while i*i <=num:
        if num%i == 0 or num % (i+2) ==0:
            return False
        i +=6
    return True
def next_prime(N):
    if N <=1:
        return 2
    prime =N
    found =False
    while not found:
        prime +=1
        if is_prime(prime):
            found = True
    return prime

N = int(input("Enter an integer N:"))
print(f"The lowest prime number greater than {N} is {next_prime(N)}.")