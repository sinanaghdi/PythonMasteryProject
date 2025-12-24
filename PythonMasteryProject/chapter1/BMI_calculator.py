# global variables and imports


# getting user input as height and weight
def get_user_input():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("enter your height (m): "))
    return weight, height


#  calculate bmi
def calculate_bmi(weight , height):
    bmi = weight // (height ** 2)
    return bmi

# get the bmi result
def get_bmi_result(bmi):
    if bmi < 18.5:
        print("Under weight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("overweight")
    elif 30 <= bmi < 35:
        print("obese")
    else:
        print("extremely obese")
         

# create main function to run
def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    get_bmi_result(bmi)
    
    
    
main()