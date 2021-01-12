"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid" <- Edge Case
- last([1, 2, 3, 4, 5], 0) ➞ [] <- Edge Case

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

Questions:
- What if n is a string, a float, a negative number, a complex number, etc.?
--- String or float: Force it to an int with int()
--- Negative: Return an empty list
--- Complex numbers: Stopped by the schema
- What if the list is empty?
--- No special rules.
"""

def last(a, n):
# Make sure n is an int.
    n = int(n)
# Make sure n isn't too large.
    if n > len(a):
        return "Invalid: Request too long."
# Make sure n isn't negative or 0. 
    if n <= 0:
        return []
# Negative Slicing Solution: #
    result = a[-n:]
    
    return result

""" # Looping Solution: #
    result = []
# Loop n times
    for _ in range(n):
    # pop the value off the end of the list
        val = a.pop()
    # insert the value at the front of the result list
        result.insert(0, val)
    
    return result
"""


print(last([1, 2, 3, 4, 5], 1)) # Should return [5]
print(last([1, 2, 3, 4, 5], 7)) # Should return "invalid"
print(last([1, 2, 3, 4, 5], 0)) # Should return []
print(last([1, 2, 3, 4, 5], "jam")) # Should return an error