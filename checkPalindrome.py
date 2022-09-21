"""
Given the string, check if it is a palindrome

"""
def solution(inputString):
    r = reversed(inputString) # First, we reverse the list 
    if list(r) == list(inputString): # Then check if the reverse list is equal to original list if is it then return True else return false. 
        return True
    else:
        return False