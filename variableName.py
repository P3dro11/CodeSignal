"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

    
"""

def solution(name):
    answer = []
    
    for i in range(len(name)):
        if name[0].isdigit():
            answer.append(False)
        else:
            if name[i].isalpha() or name[i] == "_":
                answer.append(True)
            elif name[i].isdigit():
                answer.append(True)
            else:
                answer.append(False)
    return all(answer)
                
    

