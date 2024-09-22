from random import randint

def guess_number():
    while True:
        n=str(randint(100,999))
        if not (n[0]==n[1] or n[0]==n[2] or n[1]==n[2]):
            return n
        
name=input("Enter your name: ")
print("Hi,",name,"Start the game")
bulls=0
cows=0
chances =10
num =str(guess_number())

while chances > 0:
    n=str(input("Enter your number: "))
    if n == num:
        print("Great! you are brillient")
        break
    else: 
        for i in range(0,3):
            if n[i] == num[i]:
                cows =cows+1
            elif n[i] in num:
                
                bulls=bulls+1
        print("you have ",cows,"cows and",bulls,"bulls.")
        print("you have ",chances-1,"chances")
        bulls=0
        cows=0
        chances=chances-1
print(num)


"""
if the digit is correct and position also in correct positon then shows one cow
if the digit only is correct ,but position was wrong then add one bull
"""