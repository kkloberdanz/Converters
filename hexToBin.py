#!/usr/bin/python3

import sys

def hexDigitToDec( digit ): 

    digit = ord(digit)

    # Then digit is a capital letter
    if digit >= 65 and digit <= 70:
        return digit - 55
    elif digit >= 97 and digit <= 102:
        return digit - 87
    elif digit >= 48 and digit <= 57:
        return digit - 48
    else:
        print("Error in hexDigitToDec")
        sys.exit()

def fullLen( string ):
    if len(string) > 4 or len(string) < 1:
        print("Error in fullLen")
        sys.exit()
    string = ("0" * (4 - len(string))) + string
    return string

def hexToBin( hexString, space = "none" ):
    if hexString[0:2] == "0x" or hexString[0:1] == "0X":
        hexString = hexString[2:]
    binEquivalent = ''
    if space == "space":
        for digit in hexString:
            binEquivalent = binEquivalent + fullLen(str(bin(hexDigitToDec( digit ))[2:] )) + " "
    else:
        for digit in hexString:
            binEquivalent = binEquivalent + fullLen(str(bin(hexDigitToDec( digit ))[2:] ))
    return binEquivalent

# Main
arg1 = sys.argv[1]
if len(sys.argv) > 2:
    arg2 = sys.argv[2] 
    print( hexToBin(arg1, arg2) )
else:
    print( hexToBin(arg1) )

