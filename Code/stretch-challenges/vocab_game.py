import random

new_game = input("Type yes to play my word game! ") #takes user input to initiate game

#condition that keeps the game running
while new_game == "yes":

    dict = {  # dictionary of words and definition
        "beloved": "dearly loved",
        "appreciate": "realize fully",
        "worthy": "important or honorable",
        "teamwork": "labor done by a group"
    }


    vocab_list = list(dict.keys()) #takes keys from dict and turns them into a list
    
    random.shuffle(vocab_list) #shuffled the words list
    
    #counters to keep track of right and wrong answers
    correct = 0
    wrong = 0
    
    for word in vocab_list: #accessing each definition
        display = "{}"
        
        print(display.format(word))  # displays the definition
        user_answer = input("Answer: ") #takes answer as user input
        print(dict[word]) #shows correct answer
        print(" ")

        if user_answer == (dict[word]): #checks if user's input is correct
            print("That answer is correct")
            correct += 1
        else:
            print("That answer is incorrect")
            wrong += 1

    #displays score
    display_score = "Score: {} correct"
    print(display_score.format(correct))
    # takes user input to initiate game
    new_game = input("Type yes to play my word game! ")

print("See you next time!")


