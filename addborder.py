"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

"""

def solution(picture):
    answer = []
    answer.append("*" * (len(picture[0]) + 2))
    for i in range(len(picture)):
        answer.append("*" + picture[i] + "*")
    answer.append("*" * (len(picture[0]) + 2))
    return answer