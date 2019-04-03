
noun1 = input("Enter a noun: ")
# Accepts noun input from user
verb1 = input("Enter a verb: ")
# Accepts verb input from user
place1 = input("Enter a place: ")
# Accepts place input from user
adj1 = input("Enter an adjective: ")
# Accepts adjective input from user

def Madlib1():
    # prints out results for user choice 1
    print('\n\nOnce upon a time, a small {}\ncame along and {} my socks.\nI walked to {}\nand bought a {} pair.'.format(noun1, verb1, place1, adj1))

def Madlib2():
    # prints out results for user choice 2
    print('\n\nWhile walking home, I ran into {}.\nThey {} me then continued walking to {}.\nThe encounter was {}.'.format(noun1, verb1, place1, adj1))

def user_choice():
    # accepts user input and decides between Madlib 1 and Madlib 2 then returns the result
    answer = int(input('Choose your own adventure. Enter 1 or 2 to choose your story.'))
    return answer

# conditional statement based on user input
if __name__ == "__main__":
    answer = user_choice()
    if answer == 1:
        Madlib1()
    else:
        Madlib2()