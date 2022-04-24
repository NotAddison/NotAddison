# Time Taken : 
# - Main Game [1.5 hours]
# - Turtle (est) [40-50 min]

import requests
import turtle

# Get words from API
def GetWord():
    url = "https://random-word-api.herokuapp.com/word"  
    response = requests.get(url)
    word = response.text[2:-2]
    word = 'hi'
    wordlist = list(word)
    return wordlist

# Checks User input (Validations) [Char, Used, & other stuff]
def CheckInput(userInput, wordlist,userInput_list):
    ## Validation 1 : Check if userinput is a single char
    if len(userInput) == 1 & userInput.isalpha():
        ## Validation 2 : Check if user input exists in wordlist
        if userInput in wordlist:
                ## Validation 3 : Check if word is already guessed
                if userInput in userInput_list:
                    print("Already Guessed")
                    return False
                else:
                    return True
    else:
        print("{} is not a valid input!".format(userInput))
        return False

# Literally just checks for completion
def CheckCompletion(userInput_list,word):
    valid = 0
    for letter in word:
        for user_letter in userInput_list:
            if user_letter == letter:
                valid+=1
    if valid == len(word):
        return True
    else:
        return False

# Draws the "_" and the guessed letters in terminal
def DrawTerminal(word,userInput_list):
    for letter in word:
        if letter in userInput_list:
            print(letter, end= " " )
        else:
            print("_", end= " " )
    print("\n")
        

# ----- Main Game ------
wrong_ans = 0
userInput_list = []

word = GetWord()
print(word)
while (wrong_ans != 8):
    DrawTerminal(word,userInput_list)
    print("User Input: ", userInput_list)
    userInput = input(">> Type a letter: ").lower()

    ## Checks user input (chars validaiton & check if used before)
    if(CheckInput(userInput, word, userInput_list)):
        userInput_list.append(userInput)

    ## Check if user completed the word
    if(CheckCompletion(userInput_list,word)):
        print(f">> '{''.join(word)}' is the word!")
        print("You won!")
        break
    elif wrong_ans == 8:
        print("You Lost!")
        break

