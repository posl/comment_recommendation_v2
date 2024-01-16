Synthesizing 10/10 solutions

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while n > 1:
            n2 = ugly[i2] * 2
            n3 = ugly[i3] * 3
            n5 = ugly[i5] * 5
            min_ugly = min(n2, n3, n5)
            if min_ugly == n2:
                i2 += 1
            if min_ugly == n3:
                i3 += 1
            if min_ugly == n5:
                i5 += 1
            ugly.append(min_ugly)
            n -= 1
        return ugly[-1]

=======
Suggestion 2

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
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        i2=i3=i5=0
        count=1
        while count<n:
            next2=ugly[i2]*2
            next3=ugly[i3]*3
            next5=ugly[i5]*5
            next=min(next2,next3,next5)
            ugly.append(next)
            if next==next2:
                i2+=1
            if next==next3:
                i3+=1
            if next==next5:
                i5+=1
            count+=1
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0
        while len(nums) < n:
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3: 
                i3 += 1
            if ugly == nums[i5] * 5: 
                i5 += 1
        return nums[-1]

=======
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
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
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

=======
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        for i in range(1,n):
            ugly[i] = min(next2,next3,next5)
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

def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p2 = p3 = p5 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2: p2 += 1
            if dp[i] == dp[p3] * 3: p3 += 1
            if dp[i] == dp[p5] * 5: p5 += 1
        return dp[-1]

=======
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2 = i3 = i5 = 0
        while len(dp) < n:
            u2, u3, u5 = dp[i2]*2, dp[i3]*3, dp[i5]*5
            umin = min(u2, u3, u5)
            if umin == u2: i2 += 1
            if umin == u3: i3 += 1
            if umin == u5: i5 += 1
            dp.append(umin)
        return dp[-1]

=======
Suggestion 10

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        for i in range(1,n):
            ugly[i] = min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5)
            if ugly[i] == ugly[i2]*2:
                i2+=1
            if ugly[i] == ugly[i3]*3:
                i3+=1
            if ugly[i] == ugly[i5]*5:
                i5+=1
        return ugly[-1]
