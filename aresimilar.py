"""
Two arrays are called similar if one can be obtained from another 
by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.    
    
"""

def solution(a, b):
    element = sorted(a) == sorted(b)
    diff = sum([i != j for i,j in zip(a,b)]) < 3
    return element and diff
