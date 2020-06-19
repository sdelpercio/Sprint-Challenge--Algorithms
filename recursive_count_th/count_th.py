'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    # check for end of word
    if len(word) <= 1:
        return 0
    
    # check for first two chars
    if word[0:2] == 'th':
        return 1 + count_th(word[2:])
    # recursive, skip first two
    else:
        return count_th(word[1:])
