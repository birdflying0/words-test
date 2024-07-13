#!/usr/bin/env python3

#import libraries
import random
#regardless of lowercase or uppercase
import ctypes

# Word list with only the first three entries
#word_list = [  
#    ['household', '家庭'],  
#    ['possess', '拥有，持有'],  
#    ['remark', '言论，评述'],  
#    ['counsel', '忠告，建议']
#]

import getwords as gw

word_list = gw.get_words("dict.xlsx")

#global variables
t = len(word_list)
wrong_answer = []
word_list.sort()

    
# Prompt the user for translation direction once
language = input("Enter 0 to translate English to Chinese, enter 1 to translate Chinese to English, or q to quit: ").strip().lower()
while language not in ["0", "1","q"]:
    print("Invalid input. Please enter 0,1 or q.")
    language = input("Enter 0 to translate English to Chinese, enter 1 to translate Chinese to English, or q to quit: ").strip().lower()

if language == "q" :
    exit(0) 

# Main loop for the translation game
while word_list:
    # Generate a random number to select a word from the list
    r = random.randint(0, len(word_list) - 1)

    if language == "0":
        # Ask the user for the Chinese translation
        answer = input("Enter the Chinese for '{}': ".format(word_list[r][0]))
        # Check if the answer is correct
        correct_answer = word_list[r][1]
        if answer == correct_answer:
            print("Correct answer!")
            word_list.pop(r)
        else:
            print(f"Incorrect. The correct answer is '{correct_answer}'.")
    
    elif language == "1":
        #cut_off_line
        print("-----------")
        # Ask the user for the English translation
        answer = input("Enter the English for '{}': ".format(word_list[r][1])).lower()
        # Check if the answer is correct
        correct_answer = word_list[r][0].lower()
        #count_wrong_answer : count how many times you have got this word wrong
        #give a hint if the answer is empty
        if answer == correct_answer:
            print("Correct answer!")
            word_list.pop(r)
            #how many words remains
            t -=1
            print(t,"words remaining.")
        else:
            print(f"You have got {word_list[r][0]} wrong.")
            wrong_answer.append(word_list[r])
            print(f"Incorrect. The correct answer is '{correct_answer}'.")
            print(t,"words remaining.")

    if not word_list:
        print("Congratulations! You've translated all the words.")


if wrong_answer:
    print(f"\n-----------\nYou have got {len(wrong_answer)} spelling mistake out of {t} words \n\nThis is the wrong answer list\n\n {wrong_answer}")
print("Goodbye!")
