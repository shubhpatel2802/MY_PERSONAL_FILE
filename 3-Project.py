import random
word_list=["apple","beutiful","potato"]
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display +='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ")
    for letter in chosen_word:
        if letter ==guessed_letter:
            print("Match")
        else:
            print("No match")
