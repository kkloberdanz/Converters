#!/usr/bin/python3

import sys

def assertAllNumeric( numAsString ):
    nums = []
    nums = list(range(0, 10))
    nums = str(nums)
    for digit in numAsString:
        if digit not in nums:
            print("Non-numeric input")
            sys.exit()

def decToBinary( decAsString ):
    dec = int(decAsString)
    binary = ''
    while dec > 0:
        binary = str(dec%2) + binary
        dec = dec // 2 
    return binary

inputArg = sys.argv[1]
assertAllNumeric( inputArg ) 

print( decToBinary(inputArg) )
