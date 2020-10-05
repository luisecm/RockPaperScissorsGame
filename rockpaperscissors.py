import random
import sys
random.seed(1)
index_word = 0
index_computer_choice = 0
scores_array = []
current_score = 0
options_computer = []
full_options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
you_win_against = []
options_to_end_of_array = 0
name = input("Enter your name: ")
print("Hello, " + name)
file = open("rating.txt", "r")
options_for_play = input()
if len(options_for_play) == 0:
    options_computer = ['rock', 'paper', 'scissors']
else:
    options_computer = options_for_play.split(",")
print("Okay, let's start")

for line in file:
    scores_array = line.split()
    if name == scores_array[0]:
        current_score = int(scores_array[1])

while True:
    you_win_against = []
    index_word = 0
    options_to_end_of_array = 0

    word = input()
    if word == '!exit':
        print("Bye!")
        break
    elif word == '!rating':
        print("Your rating: " + str(current_score))
    elif word in options_computer:
        computer_choice = random.choice(options_computer)
        if word == computer_choice:
            current_score += 50
            print("There is a draw (" + computer_choice + ")")
        elif word != computer_choice:
            index_word = full_options.index(word)
            options_to_end_of_array = len(full_options) - index_word - 1
            if options_to_end_of_array >= 7:
                you_win_against = full_options[index_word + 1:index_word + 8]
                if computer_choice in you_win_against:
                    current_score += 100
                    print("Well done. The computer chose (" + computer_choice + ") and failed")
                elif computer_choice not in you_win_against:
                    print("Sorry, but the computer chose (" + computer_choice + ")")
            elif options_to_end_of_array < 7:
                you_win_against = full_options[index_word + 1:]
                you_win_against += full_options[0:7 - options_to_end_of_array]
                if computer_choice in you_win_against:
                    current_score += 100
                    print("Well done. The computer chose (" + computer_choice + ") and failed")
                elif computer_choice not in you_win_against:
                    print("Sorry, but the computer chose (" + computer_choice + ")")
    else:
        print("Invalid input")

file.close()
