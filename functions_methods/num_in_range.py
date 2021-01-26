#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran(num,high,low):
    if num > low and num < high:
        print(f"the middle number is {num} and low is {low} and high is {high}")
        # if num in range(low,high)