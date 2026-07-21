# Write a Python program to count the number of
# vowels and consonants in a string.
#
# Example:
#
# Input:
# Python
#
# Output:
# Vowels: 1
# Consonants: 5

# Input:
text = str(input("Enter your text: "))

# Variables:
vowel_count = 0
consonant_count = 0
text = text.lower()

# Loop:
for character in text:
    if character in ("a", "e", "i", "o", "u"):
        vowel_count += 1
    else:
        consonant_count += 1

#output
print("vowel count:", vowel_count)
print("consonant count:", consonant_count)

