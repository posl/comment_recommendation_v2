Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n%2 == 0:
            return 1+self.integerReplacement(n//2)
        else:
            return 1+min(self.integerReplacement(n+1),self.integerReplacement(n-1))

=======
Suggestion 2

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n%2 == 0:
            return 1 + self.integerReplacement(n/2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))

=======
Suggestion 3

class Solution:
    def integerReplacement(self, n: int) -> int:
        #dp = [0] * (n+1)
        #dp[1] = 0
        #dp[2] = 1
        #dp[3] = 2
        #dp[4] = 2
        #dp[5] = 3
        #dp[6] = 3
        #dp[7] = 4
        #dp[8] = 3
        #dp[9] = 4
        #dp[10] = 4
        #dp[11] = 5
        #dp[12] = 4
        #dp[13] = 5
        #dp[14] = 5
        #dp[15] = 5
        #dp[16] = 4
        #dp[17] = 5
        #dp[18] = 5
        #dp[19] = 6
        #dp[20] = 5
        #dp[21] = 6
        #dp[22] = 6
        #dp[23] = 7
        #dp[24] = 5
        #dp[25] = 6
        #dp[26] = 6
        #dp[27] = 7
        #dp[28] = 6
        #dp[29] = 7
        #dp[30] = 7
        #dp[31] = 7
        #dp[32] = 5
        #dp[33] = 6
        #dp[34] = 6
        #dp[35] = 7
        #dp[36] = 6
        #dp[37] = 7
        #dp[38] = 7
        #dp[39] = 8
        #dp[40] = 6
        #dp[41] = 7
        #dp[42] = 7
        #dp[43] = 8
        #dp[44] = 7
        #dp[45] = 8
        #dp[46] = 8
        #dp[47] = 9
        #dp[48] = 6
        #dp[49]

=======
Suggestion 4

def integerReplacement(self, n: int) -> int:
        # 1の場合は0回
        if n == 1:
            return 0
        # 偶数の場合は2で割る
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        # 奇数の場合は1増減させる
        else:
            return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

=======
Suggestion 5

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            elif n == 3:
                n = n - 1
                count += 2
            elif n % 4 == 1:
                n = n - 1
                count += 1
            else:
                n = n + 1
                count += 1
        return count

=======
Suggestion 6

def integerReplacement(self, n: int) -> int:
        # 偶数は2で割る
        # 奇数は1足すか1引く
        # 1になるまでの回数を返す
        # 例外処理
        if n == 1:
            return 0
        # 2で割り切れる間は割る
        while n % 2 == 0:
            n //= 2
        # 奇数の場合は1引くか1足す
        if n == 1:
            return 1
        elif n % 4 == 1:
            return self.integerReplacement(n-1) + 1
        else:
            return self.integerReplacement(n+1) + 1

=======
Suggestion 7

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

=======
Suggestion 8

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                count += 1
            else:
                if n == 3:
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
Suggestion 9

def integerReplacement(self, n: int) -> int:
        # nが1なら0を返す
        if n == 1:
            return 0
        # nが偶数なら2で割る
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        # nが奇数なら1を足すか引くか
        return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

=======
Suggestion 10

def integerReplacement(self, n: int) -> int:
        # 1の場合は0
        if n == 1:
            return 0
        # 偶数の場合は2で割る
        elif n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        # 奇数の場合は+1か-1
        else:
            return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
