# import random global variable
import random
User_Choices = ['Rock','Paper', 'scissors']


# function that give user input
def get_user_input():
    choice = input("Pick your choice ['Rock','Paper', 'scissor'] : ")
    while choice not in User_Choices:
            choice = input("Pick your choice ['Rock','Paper', 'scissor'] : ")
    return choice

# create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(User_Choices)
    print(f"pc choice is {pc_choice}")
    return pc_choice

# compare and determine which on is open
def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        print( "Draw!")
    elif user_input == "Rock" and pc_input == "scissor":
        print("user won!") 
    elif user_input == "Paper" and pc_input == "Rock":
        print("user won!")
    elif user_input == "scissor" and pc_input == "Paper":
        print("user won!")
    else:
        print("computer won!")
    
    

# create main function as runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input,pc_input)
    print("end of program")

# make an iteration to doing game as much as we need
answer = 'y'
while answer == 'y':
    main()
    answer=input("do you want to continue?(y/n): ")