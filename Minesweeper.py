"""
In the popular Minesweeper game you have a board with some mines 
and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. 
Starting off with some arrangement of mines we want to create a Minesweeper game setup.
    
"""

def solution(matrix):
    row = len(matrix)
    column = len(matrix[0])
    answer = [[0 for i in range(column)] for j in range(row)]
    pad_matrix = [[0 for i in range(column+2)] for j in range(row+2)]
    
    for i in range(row):
        for j in range(column):
            pad_matrix[i+1][j+1] = matrix[i][j]
            
    for x in range(row):
        for y in range(column):
            answer[x][y] = pad_matrix[x][y] + pad_matrix[x][y+1] + pad_matrix[x][y+2] + pad_matrix[x+1][y] + pad_matrix[x+1][y+2] + pad_matrix[x+2][y] + pad_matrix[x+2][y+1] + pad_matrix[x+2][y+2]
    return answer
