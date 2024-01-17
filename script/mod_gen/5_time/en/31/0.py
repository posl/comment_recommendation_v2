class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # If there is no repetition, return 0
        if n1 == 0:
            return 0
        # Build the full string from s1
        s = s1 * n1
        # Keep track of the number of times s2 is found in s
        count = 0
        # Keep track of the index in s2
        j = 0
        # For each character in s
        for c in s:
            # If the character matches the current character in s2
            if c == s2[j]:
                # Increment the index of s2
                j += 1
                # If we have reached the end of s2
                if j == len(s2):
                    # Increment the count and reset the index
                    count += 1
                    j = 0
        # Return the number of times s2 is found in s
        return count // n2

if __name__ == '__main__':
    s1 = input()
    n1 = int(input())
    s2 = input()
    n2 = int(input())
    a = Solution()
    print(a.getMaxRepetitions(s1, n1, s2, n2))