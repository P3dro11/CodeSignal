"""
Given a sorted array of integers a, 
your task is to determine which element of a is closest to all other values of a. 
In other words, find the element x in a, which minimizes the following sum:
abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)
If there are several possible answers, output the smallest one.
"""

def absoluteValuesSumMinimization(a):
    a_list = list(set(a))
    a_list.sort()
    diff_value = []
    answer = []
    
    for i in a_list:
        for j in a:
            diff_value.append(abs(i-j))
    
    while diff_value != []:
        answer.append(sum(diff_value[:len(a)]))
        del diff_value[:len(a)]
        
    for i in range(len(answer)):
        if answer[i] == min(answer):
            return a_list[i]