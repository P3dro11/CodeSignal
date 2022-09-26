"""
Given a string, find out if its characters can be rearranged to form a palindrome.
    
"""
def solution(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1