"""
Given an array of equal-length strings, 
you'd like to know if it's possible to rearrange the order of the elements in 
such a way that each consecutive pair of strings differ by exactly one character. 
Return true if it's possible, and false if not.
Note: You're only rearranging the order of the strings,
not the order of the letters within the strings!

"""
    
from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def solution(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False
