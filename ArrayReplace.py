"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

"""

def solution(inputArray, elemToReplace, substitutionElem):
    answer = []
    for i in inputArray:
        if i != elemToReplace:
            answer.append(i)
        else:
            answer.append(substitutionElem)
    return answer