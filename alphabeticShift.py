"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e.
replace a with b, replace b with c, etc (z would be replaced by a).

"""

def solution(inputString):
    
    answer = ""
    
    for i in inputString:
        if i == "z":
            answer += "a"
        else:
            answer += chr(ord(i)+1)
    return answer