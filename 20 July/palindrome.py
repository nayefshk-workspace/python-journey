# # txt = input("Enter your text: ")

# # # a = (txt[-1::-1])
# # # if txt == a: 
# # #     print("It is a palentrome")
# # # else:
# # #     print("It is not a palentrome")

# # # for i in range(len(txt)::-1):
# # #     reverse = (txt[i]) 
# # #     if txt == reverse:
# # #         print("It is a palentrome")
# # #     else:
# # #         print("It is not a palentrome")

# # a = len(txt)-1
# # reverse = ""
# # for i in range(a,-1,-1):
# #     reverse = reverse + txt[i]
# #     print(reverse)
# # print(reverse)


# a = 1

# b = (a%10)
# c = ()
# # print(3 * 10 + 2)
# # print(32 *10 + 1)
# print(b)

number = int(input("Enter your number: "))
n=number
reverse=0
while n != 0:
    digit = n % 10 
    reverse = reverse * 10 + digit
    n = n//10
print(reverse)

