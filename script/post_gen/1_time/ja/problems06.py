Synthesizing 9/10 solutions

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
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
        # 2,3,5の倍数をそれぞれキューに格納
        q2, q3, q5 = deque([1]), deque(), deque()
        for i in range(n):
            # 3つのキューの先頭のうち最小のものを取り出す
            # 2の倍数のキューの先頭の値を取り出す
            v2 = q2[0] if q2 else float('inf')
            # 3の倍数のキューの先頭の値を取り出す
            v3 = q3[0] if q3 else float('inf')
            # 5の倍数のキューの先頭の値を取り出す
            v5 = q5[0] if q5 else float('inf')
            # 3つの中で最小の値を取り出す
            v = min(v2, v3, v5)
            # 最小の値が2の倍数のキューの先頭の値と一致した場合
            if v == v2:
                # 2の倍数のキューの先頭の値を取り出す
                q2.popleft()
                # 2の倍数のキューの先頭の値に2をかけてキューに格納する
                q2.append(v * 2)
                # 3の倍数のキューの先頭の値に3をかけてキューに格納する
                q3.append(v * 3)
            # 最小の値が3の倍数のキューの先頭の値と一致した場合
            if v == v3:
                # 3の倍数のキューの先頭の値を取り出す
                q3.popleft()
                # 3の倍数のキューの先頭の値に3をかけてキューに格納する
                q3.append(v * 3)
            # 最小の

=======
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly_number = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(n):
            ugly_number.append(min(ugly_number[i2] * 2, ugly_number[i3] * 3, ugly_number[i5] * 5))
            if ugly_number[-1] == ugly_number[i2] * 2:
                i2 += 1
            if ugly_number[-1] == ugly_number[i3] * 3:
                i3 += 1
            if ugly_number[-1] == ugly_number[i5] * 5:
                i5 += 1
        return ugly_number[n - 1]

=======
Suggestion 4

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
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > len(ugly):
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

=======
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0
        while len(nums) < n:
            val2, val3, val5 = nums[i2]*2, nums[i3]*3, nums[i5]*5
            nextval = min(val2, val3, val5)
            if nextval == val2:
                i2 += 1
            if nextval == val3:
                i3 += 1
            if nextval == val5:
                i5 += 1
            nums.append(nextval)
        return nums[-1]

=======
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        
        while len(ugly) < n:
            while ugly[p2] * 2 <= ugly[-1]:
                p2 += 1
            while ugly[p3] * 3 <= ugly[-1]:
                p3 += 1
            while ugly[p5] * 5 <= ugly[-1]:
                p5 += 1
                
            ugly.append(min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5))
            
        return ugly[-1]

=======
Suggestion 8

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            umin = min((u2, u3, u5))
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
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
        #dp[i]はi番目のugly number
        dp = [0] * n
        #初期値
        dp[0] = 1
        #2,3,5の倍数のindex
        i2 = i3 = i5 = 0
        #2,3,5の倍数の値
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            #2,3,5の倍数のうち最小の値をdp[i]に格納
            dp[i] = min(next2, next3, next5)
            #2の倍数の値がdp[i]と等しい場合、i2をインクリメントし、次の2の倍数をnext2に格納
            if dp[i] == next2:
                i2 += 1
                next2 = dp[i2] * 2
            #3の倍数の値がdp[i]と等しい場合、i3をインクリメントし、次の3の倍数をnext3に格納
            if dp[i] == next3:
                i3 += 1
                next3 = dp[i3] * 3
            #5の倍数の値がdp[i]と等しい場合、i5をインクリメントし、次の5の倍数をnext5に格納
            if dp[i] == next5:
                i5 += 1
                next5 = dp[i5] * 5
        #n番目のugly numberを返す
        return dp[n - 1]
