# Task 21: Count vowels and consonants in a string.

input_string = input("Enter a string to count vowels and consonants: ").strip()
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f" \n Python 30 days Series - Day 4 Task 21 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n")
