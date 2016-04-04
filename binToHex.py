#!/usr/bin/python3

import sys

def assertAllBinary( numAsString ):
    nums = []
    nums = list(range(0, 2))
    nums = str(nums)
    for digit in numAsString:
        if digit not in nums:
            print("ERROR: Non-binary input")
            sys.exit()

def binaryToDecimal( binAsString ):
    factor = 1
    total = 0
    # reverseString = binAsString.reverse()
    reverseString = binAsString[::-1]
    for digit in reverseString:
        total = total + (factor * int(digit))
        factor *= 2
    return total

def binaryQuartetToDec( quartet ):
    dec = binaryToDecimal(quartet)    
    if (dec > 15) or (dec < 0):
        print("Error: binaryQuartetToDec only accepts numbers between 0 and 15")
        sys.exit()
    else:
        return dec

def decToHexLetter( dec ):
    if dec < 10 and dec >= 0:
        return str(dec)
    elif dec >= 10 and dec < 16:
        return chr( 55 + dec )
    else:
        print("Error: enexpected argument for quartetToHexLetter")
        sys.exit()

binaryNumber = sys.argv[1]

assertAllBinary(binaryNumber)
if " " in binaryNumber:
    print("ERROR: remove all spaces from input")
    sys.exit()

hexString = "" 

while binaryNumber != "":
    quartet = binaryNumber[-4:]
    binaryNumber = binaryNumber[0:-4]
    dec = binaryQuartetToDec( quartet )
    hexString = decToHexLetter(dec) + hexString

hexString = "0x" + hexString

print(hexString)
