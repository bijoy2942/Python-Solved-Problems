import string
def pan(str1, alph=string.ascii_lowercase):

    # Create a set of the alphabets
    alph_set = set(alph)


    # Remove any spaces from the input string
    str1 = str1.replace(' ','')

    # Convert into all lowercase
    str1 = str1.lower()


    # Grab all unique letters from the string set
    str1_set = set(str1)

    # alphabet set == string set input
    if alph_set == str1_set:
        return 'PANGRAM'
    else:
        pass

pan("The quick brown fox jumps over the lazy dog")
