from random import shuffle
mylist = [' ','O',' ']

# Shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

mixed_list = shuffle_list(mylist)
print("Shuffled list is ", mixed_list)

# Ask the user to Guess
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0 | 1 | 2")
    return int(guess)


def validate_the_guess(mixed_list,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong Guess")
        print(mylist)


mylist = [' ','O',' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
validate_the_guess(mixed_list,guess)