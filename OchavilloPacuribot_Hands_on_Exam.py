choice = eval(input("Which conversion would you like the value to be converted to?\n"
                    "1 Binary\n"
                    "2 Octal\n"
                    "3 Hexadecimal\n"))

if choice == 1:
    binary = int(input("Input a decimal value to be converted: "))
    binaryr = format(binary, "b")
    print(f"The Binary Conversion of {binary} is {binaryr}.")
elif choice == 2:
    octal = int(input("Input a decimal value to be converted:"))
    octalr = format(octal, "o")
    print(f"The Octal Conversion of {octal} is {octalr}.")
elif choice == 3:
    hexa = int(input("Input a decimal value to be converted:"))
    hexar= format(hexa, "x")
    print(f"The Octal Conversion of {hexa} is {hexar}.")
else:
    print("Invalid input. Please try again.")
