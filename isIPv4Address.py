"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
    
"""

def solution(inputString):
    try:
        ip_list =[i for i in inputString.split(".") if i != ""]
        
        space = len([i for i in inputString.split(".")]) == len([i for i in ip_list])
        
        range = len([i for i in ip_list if 0 <= int(i) <= 255]) == len(ip_list)
        
        length = len(ip_list) == 4
        
        return (space and range and length)
        
    except:
        return False