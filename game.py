import random

with open('words.txt', 'r') as file:
    words = file.read().split('\n')

random.shuffle(words)
input("Are you ready?")

for word in words:
    print("\n" * 40)
    print("Welcome to the game!")
    print(f'\n{"*" * 35}\n')
    print(f'{" " * 12}{word}{" " * 12}')
    print(f'\n{"*" * 35}\n')
    input("Click 'Enter' to see the next word")

print("\n\n----- END OF GAME -----\n\n")
