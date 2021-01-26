def user_input():

    #DEFINE SOME VARIABLES
    user_choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # DIGIT OR WITHIN RANGE = FALSE
    while user_choice.isdigit() == False and within_range == False:
        user_choice = input("Enter the value between 0 to 10 ")

        # DIGIT CHECK
        if user_choice.isdigit() == False:
            print("Sorry not a digit")

        # RANGE CHECK
        if user_choice.isdigit() == True:
            if int(user_choice) in acceptable_range:
                within_range = True
            else:
                print("not in range")
                within_range = False
    return int(user_choice)
result = user_input()
print(result)

