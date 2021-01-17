from random import shuffle
example_list = [1,2,3,4,5,6,7]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example_list)
print("Shuffled list is ", result)

