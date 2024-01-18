Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                cnt += 1
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
                cnt += 1
            else:
                n += 1
                cnt += 1
        return cnt

=======
Suggestion 2

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

=======
Suggestion 3

def integerReplacement(self, n: int) -> int:
        # nが1になるまでの回数を数える
        # nが偶数の場合はn//2に置き換える
        # nが奇数の場合はn+1またはn-1に置き換える
        # nが1になったら終了
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n//2
                count += 1
            else:
                if (n+1) % 4 == 0 and n != 3:
                    n += 1
                    count += 1
                else:
                    n -= 1
                    count += 1
        return count

=======
Suggestion 4

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n - 1), self.integerReplacement(n + 1)) + 1

=======
Suggestion 5

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            else:
                if n == 3:
                    n = n - 1
                    count += 1
                else:
                    if (n + 1) % 4 == 0:
                        n = n + 1
                        count += 1
                    else:
                        n = n - 1
                        count += 1
        return count

=======
Suggestion 6

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            count += 1
        return count

=======
Suggestion 7

def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            ans += 1
        return ans

=======
Suggestion 8

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n & 1 == 0:
                n >>= 1
            elif n & 3 == 3 and n != 3:
                n += 1
            else:
                n -= 1
            count += 1
        return count

=======
Suggestion 9

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            elif n == 3:
                count += 2
                break
            elif (n + 1) % 4 == 0:
                n += 1
                count += 1
            else:
                n -= 1
                count += 1
        return count

=======
Suggestion 10

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n % 2 == 0:
            return 1 + self.integerReplacement(n/2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
