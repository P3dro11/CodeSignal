"""
Check if all digits of the given integer are even.

"""

def solution(n):
    answer = []
    for i in str(n):
        if int(i) % 2 == 0:
            answer.append(True)
        else:
            answer.append(False)
    
    return all(answer)
