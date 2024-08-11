while True:
    function = input('''What would you like to do?
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exponent
    6. Quit ''').lower()
    if function == "quit":
        break
    if function != "exponent":
        while True:
            numbers = input("Please enter the numbers you would like to use separated by a space: ")
            num_list = numbers.split()
            try:
                num_list = [int(num) for num in num_list]
                break
            except ValueError:
                print("Please enter valid numbers only.")
    if function == "add":
        print(sum(num_list))
    elif function == "subtract":
        print(num_list[0] - sum(num_list[1:]))
    elif function == "multiply":
        result = 1
        for number in num_list:
            result = result * number
        print(result)
    elif function == "divide":
        result = num_list[0]
        for number in num_list[1:]:
            result = result / number
        print(result)
    elif function == "exponent":
        while True:
            try:
                base = int(input("What number would you like to use as the base? "))
                exponent = int(input("What exponent would you like to use? "))
                print(f"{base} to the power of {exponent} is {base ** exponent}")
                break
            except ValueError:
                print("Please enter valid numbers only.")
    else:
        print("I don't understand that.")
