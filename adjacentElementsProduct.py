"""
Given an array of integers, find the pair of adjacent elements that has the largest product 
and return that product.

"""

def solution(inputArray):
    return max( #This will return the max ouput
        [inputArray[i] * inputArray[i+1] for i in range(0, len(inputArray) - 1)] # this part will literate through the array and also multiplying each element. 
    )