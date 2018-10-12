import os
bitwise = ['&','|','^','~','<<','>>']
while True:
    theInput = str(input("= "))
    isBitwise = False
    for i in bitwise:
        if i in theInput:
            isBitwise = True
    if theInput == "?":
        print("""\n
General
\tAddition: +\tExample: 5+7
\tSubtraction: -\tExample: 10-2
\tMultiplication: *\tExample: 4*3
\tDivision: /\t Example: 12/4
\tExponents: ** \t Example: x**2
\t
Bitwise
\tAnd &\t Example: 0b01 & 0b10
\tOr |\t Example: 0b001110 | 0b110001
\tXor ^\t Example: 0b100 ^ 0b011
\tOnes Complement ~\t Example: ~0b0
\tLeft Shift <<\t Example: 0b0011 << 0b1100
\tRight Shift >>\t Example: 0b1100 >> 0b0011
Set

Logical
        """)

    elif theInput == "":
        os.system("cls")
    else:
        theInput = theInput.replace("[","(").replace("]",")")
        if '=' in theInput:
            if isBitwise:
                print("= "+str(bin(exec(theInput))))
            else:
                print("= "+str(exec(theInput)))
        else:
            if isBitwise:
                print("= "+str(bin(eval(theInput))))
            else:
                print("= "+str(eval(theInput)))
