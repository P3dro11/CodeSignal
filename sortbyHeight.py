"""
Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

"""
def solution(a):
    tree = []
    person = []
    
    for i in range(len(a)):
        if a[i] == -1:
            tree.append(i)
        else:
            person.append(a[i])
            person.sort()
    
    for j in tree:
        person.insert(j, -1)
    return person
    