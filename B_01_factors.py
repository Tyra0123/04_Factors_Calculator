# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
To use this program, simply enter an integer between 1 and 200. 
The program will show the factors of your chosen integer.

It will also tell you if your chosen number... 
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx'.  
    ''')


# Ask user for an integer between 1 and 200.
def num_check(question):
    error = "Please enter a number between 1 and 200\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return "xxx"

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


# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    # list to store the factors
    all_factors = []

    # ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")
    all_factor = ""

# Check if user wants to exit
    if to_factor == "xxx":
        break

    for i in range(1, to_factor + 1):

        # if it's a factor (0 remainder), add it to the list
        if to_factor % i == 0:
            all_factors.append(i)

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comment
    statement_generator(heading, "*")
    print(all_factors)

    # comments for squares / primes

    # Prime numbers have only two factors
    if len(all_factors) == 2:
        print(f"{to_factor} is a prime number")

    elif len(all_factors) == 1:
        print("1 is UNITY (has only one factor)")
        all_factors = ""

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        print(f"{to_factor} is a perfect square")
