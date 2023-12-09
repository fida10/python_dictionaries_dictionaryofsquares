"""
Practice Question 1: Dictionary of Squares

Task:

Write a function generate_squares that takes an integer n 
and returns a dictionary where the keys are numbers from 
1 to n and the values are their squares.
"""

def generate_squares(n):
    ans = {}
    
    for i in range(1, n + 1):
        ans[i] = i * i

    return ans
