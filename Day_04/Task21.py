# Task 21: Count vowels and consonants in a string.

input_string = input("Enter a string to count vowels and consonants: ").strip().lower()

# Sets provide O(1) lightning-fast lookups
vowels = set("aeiou")

# Using generators and sum() is highly Pythonic
vowel_count = sum(1 for char in input_string if char in vowels)
consonant_count = sum(1 for char in input_string if char.isalpha() and char not in vowels)

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f" \n Python 30 days Series - Day 4 Task 21 \n")
print(f" \n Day 4: Strings \n")
print(f" \n Have a good one! \n " + "-"*40)
