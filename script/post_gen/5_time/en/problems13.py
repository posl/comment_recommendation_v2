Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n/2
                count += 1
            elif n == 3 or n % 4 == 1:
                n = n - 1
                count += 1
            else:
                n = n + 1
                count += 1
        return count

=======
Suggestion 2

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                if n == 3 or bin(n - 1).count('1') < bin(n + 1).count('1'):
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

=======
Suggestion 3

def integerReplacement(self, n: int) -> int:
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n = n/2
            else:
                if n == 3:
                    steps += 2
                    break
                if (n-1)/2 % 2 == 0 or n == 1:
                    n = n-1
                else:
                    n = n+1
            steps += 1
        return steps

=======
Suggestion 4

class Solution:
    def integerReplacement(self, n: int) -> int:
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd, add 1 or subtract 1
        # return the minimum number of operations needed for n to become 1
        # n is between 1 and 2^31 - 1
        # if n is even, divide it by 2
        # if n is odd

=======
Suggestion 5

def integerReplacement(self, n: int) -> int:
        # # solution 1: recursion
        # def helper(n):
        #     if n == 1:
        #         return 0
        #     if n % 2 == 0:
        #         return helper(n // 2) + 1
        #     else:
        #         return min(helper(n + 1), helper(n - 1)) + 1
        # return helper(n)
        
        # solution 2: iteration
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3:
                    n -= 1
                elif n % 4 == 1:
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

=======
Suggestion 6

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

=======
Suggestion 7

def integerReplacement(self, n: int) -> int:
        def helper(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return helper(n // 2) + 1
            else:
                return min(helper(n + 1), helper(n - 1)) + 1
        return helper(n)

=======
Suggestion 8

class Solution:
    def integerReplacement(self, n: int) -> int:
        #if even, divide by 2
        #if odd, add 1 or subtract 1
        #return minimum number of operations to get to 1
        #if n = 1, return 0
        #if n = 2, return 1
        #if n = 3, return 2
        #if n = 4, return 2
        #if n = 5, return 3
        #if n = 6, return 3
        #if n = 7, return 4
        #if n = 8, return 3
        #if n = 9, return 4
        #if n = 10, return 4
        #if n = 11, return 5
        #if n = 12, return 4
        #if n = 13, return 5
        #if n = 14, return 5
        #if n = 15, return 5
        #if n = 16, return 4
        #if n = 17, return 5
        #if n = 18, return 5
        #if n = 19, return 6
        #if n = 20, return 5
        #if n = 21, return 6
        #if n = 22, return 6
        #if n = 23, return 7
        #if n = 24, return 5
        #if n = 25, return 6
        #if n = 26, return 6
        #if n = 27, return 7
        #if n = 28, return 6
        #if n = 29, return 7
        #if n = 30, return 7
        #if n = 31, return 7
        #if n = 32, return 5
        #if n = 33, return 6
        #if n = 34, return 6
        #if n = 35, return 7
        #if n = 36, return 6
        #if n = 37, return 7
        #if n = 38, return 7
        #if n = 39

=======
Suggestion 9

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 2147483647:
            return 32
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

=======
Suggestion 10

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n%2 == 0:
            return 1 + self.integerReplacement(n/2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
