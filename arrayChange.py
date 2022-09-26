"""
    You are given an array of integers. 
    On each move you are allowed to increase exactly one of its element by one. 
    Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
    
"""

def solution(inputArray):
    letter = 0
    
    for i in range(len(inputArray)-1):
        if inputArray[i] >= inputArray[i+1]:
            letter += (inputArray[i]+1 - inputArray[i+1])
            inputArray[i+1] = inputArray[i]+1
        else:
            inputArray[i]
    return letter