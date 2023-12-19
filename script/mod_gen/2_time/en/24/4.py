def numDistinct(s, t):
    # if the length of s is less than the length of t, there is no way to make t from s
    if len(s) < len(t):
        return 0
    # if the length of s is the same as the length of t
    if len(s) == len(t):
        # if s and t are the same, there is one way to make t from s
        if s == t:
            return 1
        # if s and t are not the same, there is no way to make t from s
        else:
            return 0
    # if the length of s is greater than the length of t
    if len(s) > len(t):
        # if t is empty, there is one way to make t from s
        if t == "":
            return 1
        # if t is not empty
        else:
            # if the first character of s is the same as the first character of t
            if s[0] == t[0]:
                # there are two ways to make t from s:
                # 1. by keeping the first character of s and removing the first character of t
                # 2. by removing the first character of s and keeping t
                return numDistinct(s[1:], t[1:]) + numDistinct(s[1:], t)
            # if the first character of s is not the same as the first character of t
            else:
                # there is one way to make t from s:
                # by removing the first character of s and keeping t
                return numDistinct(s[1:], t)

if __name__ == '__main__':
    numDistinct()