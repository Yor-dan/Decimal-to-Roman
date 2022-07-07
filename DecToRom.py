def decToRom():
    try:
        roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        dec = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        x = int(input("\nEnter a decimal number: "))
        result = []

        while x != 0:
            for i in dec:
                while i <= x:
                    subtract = i
                    break
                    
            x = x - subtract
            result.append(roman[dec.index(subtract)])

        print("\nRoman numeral: ",end="")
        for i in result:
            print(i,end="")

    except ValueError:
        print("Invalid Input!")

decToRom()