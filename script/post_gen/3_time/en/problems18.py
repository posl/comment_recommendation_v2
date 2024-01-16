Synthesizing 10/10 solutions

=======
Suggestion 1

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + (dp[i-1]-dp[i-2])*(11-i)
        
        return dp[-1]

=======
Suggestion 2

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - (i - 1))

        return dp[n]

=======
Suggestion 3

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        result = 10
        unique_digits = 9
        available_digits = 9
        while n > 1 and available_digits > 0:
            unique_digits = unique_digits * available_digits
            result += unique_digits
            available_digits -= 1
            n -= 1
        return result

=======
Suggestion 4

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n == 1:
            return 10
        
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        dp[2] = 81
        for i in range(3,n+1):
            dp[i] = dp[i-1] * (10 - i + 1)
            
        return sum(dp)

=======
Suggestion 5

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n == 1:
            return 10
        
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        
        res = 10
        for i in range(2, n+1):
            tmp = 9
            for j in range(9, 9-i+1, -1):
                tmp *= j
            res += tmp
        return res

=======
Suggestion 6

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1] + (dp[i-1] - dp[i-2]) * (11 -i)
        
        return dp[n]

=======
Suggestion 7

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        base = 9

        for i in range(2, n + 1):
            base *= (9 - i + 2)
            ans += base

        return ans

=======
Suggestion 8

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        total = 10
        unique = 9
        available = 9
        
        while n > 1 and available > 0:
            unique *= available
            total += unique
            available -= 1
            n -= 1
        return total

=======
Suggestion 9

def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        1. 0<=x<10^n
        2. x has unique digits
        '''
        if n == 0:
            return 1
        ans = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp *= j
            ans += temp
        return ans

=======
Suggestion 10

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        res = 10
        unique_digits = 9
        available_digits = 9
        
        while n > 1 and available_digits > 0:
            unique_digits *= available_digits
            res += unique_digits
            available_digits -= 1
            n -= 1
        
        return res
