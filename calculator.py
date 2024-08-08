while True:
    function = input('''What would you like to do?
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Quit ''').lower()
    if function == "quit":
        break
    numbers = input("Please enter the numbers you would like to use separated by a space: ")
    if numbers != "<class 'int>":
       numbers = input("Please enter a number(s) seperated by a space ")
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
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
    else:
        print("I don't understand that.")
