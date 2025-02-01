
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    #
    # YOUR IMPLEMENTATION GOES HERE
    #
    if not lst or len(lst) == 1:
        return True  
    
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False
        
        if not increasing and not decreasing:
            return False
    
    return True

# Test cases
print(monotonic([1, 2, 3, 4, 5]))  # True (increasing)
print(monotonic([5, 4, 3, 2, 1]))  # True (decreasing)
print(monotonic([1, 2, 2, 3, 4]))  # True (non-decreasing)
print(monotonic([4, 3, 3, 2, 1]))  # True (non-increasing)
print(monotonic([1, 3, 2, 4, 5]))  # False (not monotonic)
print(monotonic([10]))  # True (single element)
print(monotonic([]))  # True (empty list)
#
# Feel free to replace these comments with
# code that tests your function monotonic.
#
