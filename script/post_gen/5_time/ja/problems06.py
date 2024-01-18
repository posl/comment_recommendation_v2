Synthesizing 10/10 solutions

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

=======
Suggestion 2

def nthUglyNumber(self, n: int) -> int:
        #DP
        #dp = [1]
        #i2 = i3 = i5 = 0
        #for _ in range(n - 1):
        #    next2, next3, next5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5
        #    next = min(next2, next3, next5)
        #    dp.append(next)
        #    if next == next2:
        #        i2 += 1
        #    if next == next3:
        #        i3 += 1
        #    if next == next5:
        #        i5 += 1
        #return dp[-1]
        #heapq
        import heapq
        ugly = [1]
        seen = set()
        heapq.heapify(ugly)
        for _ in range(n):
            curr = heapq.heappop(ugly)
            for i in [2, 3, 5]:
                if curr * i not in seen:
                    seen.add(curr * i)
                    heapq.heappush(ugly, curr * i)
        return curr

=======
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        
        ugly = [0] * n
        ugly[0] = 1
        index2 = 0
        index3 = 0
        index5 = 0
        
        for i in range(1, n):
            ugly[i] = min(ugly[index2] * 2, ugly[index3] * 3, ugly[index5] * 5)
            
            if ugly[i] == ugly[index2] * 2:
                index2 += 1
            if ugly[i] == ugly[index3] * 3:
                index3 += 1
            if ugly[i] == ugly[index5] * 5:
                index5 += 1
                
        return ugly[-1]

=======
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly_list = [1]
        two_index, three_index, five_index = 0, 0, 0
        for i in range(n-1):
            two, three, five = ugly_list[two_index] * 2, ugly_list[three_index] * 3, ugly_list[five_index] * 5
            min_num = min(two, three, five)
            ugly_list.append(min_num)
            if min_num == two:
                two_index += 1
            if min_num == three:
                three_index += 1
            if min_num == five:
                five_index += 1
        return ugly_list[-1]

=======
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        i2 = i3 = i5 = 0
        for i in range(1, n):
            dp[i] = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            if dp[i] == dp[i2]*2:
                i2 += 1
            if dp[i] == dp[i3]*3:
                i3 += 1
            if dp[i] == dp[i5]*5:
                i5 += 1
        return dp[-1]

=======
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        for i in range(1, n):
            ugly[i] = min(next2, next3, next5)
            if ugly[i] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[i] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[i] == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 8

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 2,3,5をかけていった数をリストに格納していく
        # 2,3,5をかけていった数のリストの中から最小値を取り出す
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数をリストから削除する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,3,5をかけた数をリストに格納する
        # 2,3,5をかけていった数のリストの中から最小値を取り出した数に2,

=======
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

=======
Suggestion 10

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 2, 3, 5を素因数に持つ数を作っていく
        # 1からスタート
        # 1 * 2, 1 * 3, 1 * 5
        # 1 * 2, 1 * 3, 1 * 5, 2 * 2, 2 * 3, 2 * 5, 3 * 2, 3 * 3, 3 * 5
        # 1 * 2, 1 * 3, 1 * 5, 2 * 2, 2 * 3, 2 * 5, 3 * 2, 3 * 3, 3 * 5, 4 * 2, 4 * 3, 4 * 5, 5 * 2, 5 * 3, 5 * 5
        # 1 * 2, 1 * 3, 1 * 5, 2 * 2, 2 * 3, 2 * 5, 3 * 2, 3 * 3, 3 * 5, 4 * 2, 4 * 3, 4 * 5, 5 * 2, 5 * 3, 5 * 5, 6 * 2, 6 * 3, 6 * 5, 8 * 2, 8 * 3, 8 * 5, 9 * 2, 9 * 3, 9 * 5, 10 * 2, 10 * 3, 10 * 5, 12 * 2, 12 * 3, 12 * 5, 15 * 2, 15 * 3, 15 * 5
        # 1 * 2, 1 * 3, 1 * 5, 2 * 2, 2 * 3, 2 * 5, 3 * 2, 3 * 3, 3 * 5, 4 * 2, 4 * 3, 4 * 5, 5 * 2, 5 * 3, 5 * 5, 6 * 2,
