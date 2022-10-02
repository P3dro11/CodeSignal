"""
Given two cells on the standard chess board,
determine whether they have the same color or not.

"""

def solution(cell1, cell2):
    if (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0:
        return True
    else:
        return False
    
