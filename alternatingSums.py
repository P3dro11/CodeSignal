"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, 
the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people. 
Return an array of two integers, where the first element is the total weight of team 1, 
and the second element is the total weight of team 2 after the division is complete.

"""
def solution(a):
    team1 = []
    team2 = []
    
    for i, v in enumerate(list(a)):
        if i % 2 == 0:
            team1.append(v)
        else:
            team2.append(v)
    
    return[sum(team1), sum(team2)]