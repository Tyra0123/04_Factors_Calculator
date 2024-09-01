def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:

    # list to store the factors
    all_factors = []

    to_factor = int(input("Enter an integer to find factors (or xxx to quit): "))
    all_factor = ""

    print("Factors of number {} are : ".format(to_factor))
    for i in range(1, to_factor + 1):

        # if it's a factor (0 remainder), add it to the list
        if to_factor % i == 0:
            all_factors.append(i)

    if to_factor == "xxx":
        break

    # # get factors for integers that are 2 or more
    # elif to_factor != 1:
    #     all_factors = to_factor
    #
    # # Set up comment for unity
    # else:
    #     print(f"1 is unity (has only one factor, itself)")
    #     print()

    # comments for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        print(f"{to_factor} is a prime number")

    elif len(all_factors) == 1:
        print("1 is UNITY")
        all_factors = ""

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    print(all_factors)
