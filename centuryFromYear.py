"""
     Given a year, return the century it is in. The first century spans from the year 1 up 
     to and including the year 100, the second - from the year 101 up to and including the year 200,etc. 
"""
def solution(year):
    return ((year - 1) //100 + 1) # Set a cutoff on Dec 31 00 for emxample, 1 because 2017 is 21st and 1989 = 20th.
