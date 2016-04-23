#!/usr/bin/python3

import sys

def assertAllBinary( numAsString ):
    nums = []
    nums = list(range(0, 2))
    nums = str(nums)
    for digit in numAsString:
        if digit not in nums:
            print("Non-binary input")
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

# inputArg = sys.argv[1]

for inputArg in sys.argv[1:]:
    assertAllBinary( inputArg ) 
    print( binaryToDecimal(inputArg), end = ' ' )
print()
