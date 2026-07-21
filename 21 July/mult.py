# Input:
# Variables:
# Loop:
# Condition:
# Inside the loop:
# Output:
# input : enter a number 
# varaible : the input number and answer 
# loop again for loop for i in range(1,11):
# condition answer = i x number
# output number x i = answer  

num = int(input("Enter a number: "))
answer = 0
for i in range(1,11):
    answer = i * num
    print(f"{num} x {i} = {answer}")


    