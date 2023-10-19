print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n"
      "↓                       WELCOME!                       ↓\n"
      "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

choice = eval(input("𝙒𝙝𝙞𝙘𝙝 𝙘𝙤𝙣𝙫𝙚𝙧𝙨𝙞𝙤𝙣 𝙬𝙤𝙪𝙡𝙙 𝙮𝙤𝙪 𝙡𝙞𝙠𝙚 𝙩𝙝𝙚 𝙫𝙖𝙡𝙪𝙚 𝙩𝙤 𝙗𝙚 𝙘𝙤𝙣𝙫𝙚𝙧𝙩𝙚𝙙 𝙩𝙤?\n"
                    "𝟭 𝘽𝙞𝙣𝙖𝙧𝙮?\n"
                    "𝟮 𝙊𝙘𝙩𝙖𝙡?\n"
                    "𝟯 𝙃𝙚𝙭𝙖𝙙𝙚𝙘𝙞𝙢𝙖𝙡?\n"))

if choice == 1:
    binary = int(input("Input a decimal value to be converted: "))
    binaryr = format(binary, "b")
    print(f"The Binary Conversion of {binary} is {binaryr}.\n"
          f"")
elif choice == 2:
    octal = int(input("Input a decimal value to be converted:"))
    octalr = format(octal, "o")
    print(f"The Octal Conversion of {octal} is {octalr}.")
elif choice == 3:
    hexa = int(input("Input a decimal value to be converted:"))
    hexar = format(hexa, "x")
    print(f"The Octal Conversion of {hexa} is {hexar}.")
else:
    print("Invalid input. Please try again.")
