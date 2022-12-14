"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
Sequence containing only one element is also considered to be strictly increasing.
    
"""
def solution(sequence):
    fails1 = 0 # we do two testing case bc if there is another values that needs to be taken out of the array. 
    fails2 = 0
    
    for i in range(len(sequence)-1): #We first check through the array for an element to be remove. 
        if sequence[i] >= sequence[i+1]:
            fails1 = fails1 + 1
    
    for i in range(len(sequence)-2):# Same thing goes on here. 
        if sequence[i] >= sequence[i+2]:
            fails2 = fails2 + 1
    
    if (fails1 < 2) and (fails2 < 2):
        return True
    else:
        return False