# Write a program in Python to print the Fibonacci series using an iterative method. 
# ● Example: 
# ○ Input: 5 
# ○ Output: [0, 1, 1, 2, 3] 
# first ten number should be printed


number = int(input("Enter your number: "))

if number <= 0:
    list = []
elif number == 1:
    list = [0]
else:

    a = 0
    b = 1
    list = [0, 1]
    
    for i in range(0, number):
        new_number = a + b
        list.append(new_number)
        
        c = b
        a = c
        b = new_number  


print(list)


    


