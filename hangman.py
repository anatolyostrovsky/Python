import random

def hangman():
    word = random.choice(["slice", "spice", "gross", "chemist", "totem", "poppy", "light", "spirit", "check", "bombard", "ghost", "fight", "loser", "comic"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    attemptmade = ""

    while len(word) > 0:
        main = ""
        missed = 0




name = input("Enter your name")

print("Welcome ", name)
print("--------------------------")
print("Now try to guess the word in 10 turns!")
hangman()
