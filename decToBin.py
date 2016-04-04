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
    if decAsString == '0':
        return '0'
    dec = int(decAsString)
    binary = ''
    while dec > 0:
        binary = str(dec%2) + binary
        dec = dec // 2 
    return binary

inputList = []
set_fill  = False
max_len = 0
for inputArg in sys.argv[1:]:
    if inputArg[0] == '-':
        if inputArg == '--fill':
            set_fill = True
        else:
            print('unknown modifier: ' + str(inputArg))
            quit()

    else:
        inputList.append(inputArg)

        if max_len < len(decToBinary(inputArg)):
            max_len = len(decToBinary(inputArg))


for inputArg in inputList:
    assertAllNumeric( inputArg ) 
    convertedNum = decToBinary(inputArg)
    if set_fill:
        if len(convertedNum) == max_len:
            print( convertedNum , end=' ')
        else:
            for i in range(max_len - len(convertedNum)):
                print('0', end = '')
            print( convertedNum , end=' ')
    else:
        print( convertedNum , end=' ')

print()
