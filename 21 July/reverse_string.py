# Write a Python program to reverse a string.
#
# Example:
# Input: "Python"
#
# Output:
# "nohtyP"

text = str(input("Enter your name: "))

# print(txt[::-1])

# for i in range(len(text) - 1, -1, -1):
#     print(text[i])
answer = ""
for character in text:
    answer = character + answer
    print(answer)