c = True
while c:
    x =int(input("Enter the First number: "))
    y = int(input("Enter the Second Number: "))
    selection = input("Select the operations: \n+ \n- \nX \n/ \n")
    match selection:
        case "+":
            print("Result = ",x+y)
        case "-":
            print("Result = ",x-y)
        case "X":
            print("Result = ",x*y)
        case "/":
            print("Result = ",x/y)
        case _:
            print("Please enter any from the above")
        