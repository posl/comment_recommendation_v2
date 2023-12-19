def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    #Solution 1
    # if not s:
    #     return 0
    # if not t:
    #     return 1
    # if len(s) < len(t):
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 2
    # if not s:
    #     return 0
    # if not t:
    #     return 1
    # if len(s) < len(t):
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 3
    # if len(s) < len(t):
    #     return 0
    # if not t:
    #     return 1
    # if not s:
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 4
    # if len(s) < len(t):
    #     return 0
    # if not t:
    #     return 1
    # if not s:
    #     return 0
    # if s == t:
    #     return 1
    # if s[0] == t[0]:
    #     return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
    # else:
    #     return numDistinct(s[1:], t)
    
    #Solution 5
    # if len

if __name__ == '__main__':
    numDistinct()