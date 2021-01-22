def func(inp):
    if inp < 2:
        return 0

    store_prime_list = [2]
    counter = 3

    while counter < inp:
        for y in store_prime_list:
            if counter % y == 0:
                counter += 2
                break
        else:
            store_prime_list.append(counter)
            counter += 2
    print(store_prime_list)
    print(len(store_prime_list))
