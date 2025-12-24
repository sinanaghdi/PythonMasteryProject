#import and global variables
import random
MAX_num = 10
MIN_num = 1
Max_guess_counts = 3
  



# generate a random number
def generate_random_num():
    return random.randint(MIN_num,MAX_num)



# get user input as guess
def get_user_input():
    print("Your number should be between f{MIn_num}-{MAX_num}")
    while True:
        try:
            user_input = int(input("Enter your guess: "))
        except ValueError:
            print("Enter a valid number!")
        else:
            return user_input

# check guesses number
def check_guessed_num(user_input , random_num):
    return user_input == random_num


# main function for running application
def main():
    random_num = generate_random_num()
    print(f" random number is {random_num}.")
    while Max_guess_counts > 0:
        user_input = get_user_input()
        if check_guessed_num(user_input,random_num):
            print("you have guessed right")
            break
        Max_guess_counts -=1
        print(f"guesses left: {Max_guess_counts}")
    else:
        print("you couldn't guess the number , and out of guesses!")
        
if __name__ == "__main__":
    main()