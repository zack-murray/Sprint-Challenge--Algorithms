'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word): #single parameter 'word'
    # Base case
    if len(word) < 1:
        return 0    
    # Recursion; no loops (check)
    # First cycle breaks down list one letter at
    # a time, next cycle appends back together keeping 
    # count of the amt of times 'th' appear together
    elif word[:2] == "th": # Case matters
        return count_th(word[1:]) + 1 # Returns a count
    else:
        pass
    return count_th(word[1:])



# Test
word = "abcthefthghith"
print(count_th(word))