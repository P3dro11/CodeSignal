"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

"""

def solution(statues):
    s = 0
    statues.sort()
    for i in range(0, len(statues)-1):
        if statues[i + 1] - statues[i] > 1:
            s += statues[i+1] - statues[i]-1
    return s 

