Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
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
Suggestion 2

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
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        for l in range(1, n):
            ugly[l] = min(next2, next3, next5)
            if ugly[l] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[l] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[l] == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]

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
        i2=i3=i5=0
        while n>1:
            u2,u3,u5 = 2*ugly[i2],3*ugly[i3],5*ugly[i5]
            umin = min(u2,u3,u5)
            if umin==u2:
                i2+=1
            if umin==u3:
                i3+=1
            if umin==u5:
                i5+=1
            ugly.append(umin)
            n-=1
        return ugly[-1]

=======
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        for i in range(1, n):
            ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            if ugly[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            if ugly[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next_multiple_of_2 = ugly[i2] * 2
        next_multiple_of_3 = ugly[i3] * 3
        next_multiple_of_5 = ugly[i5] * 5
        for i in range(1, n):
            ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            if ugly[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            if ugly[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            if ugly[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 8

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
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
        # 2, 3, 5
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
        # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
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
