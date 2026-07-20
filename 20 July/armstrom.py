# take input 
# should divide the number as much as the input is 
#if armstrong number it should print that

#functions 
#number
number = int(input("Enter your number: "))
n = number
a = len(str(number))
answer = 0
while (n != 0):
    
    digit = n % 10

    answer = answer + digit ** a 
    n = n//10
    # print(answer)
if number == answer:
    print("It is armstrong number")
print(answer)
