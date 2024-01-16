Synthesizing 10/10 solutions

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n

=======
Suggestion 2

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
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next_2 = 2
        next_3 = 3
        next_5 = 5
        for i in range(1, n):
            ugly[i] = min(next_2, next_3, next_5)
            if ugly[i] == next_2:
                i2 += 1
                next_2 = ugly[i2] * 2
            if ugly[i] == next_3:
                i3 += 1
                next_3 = ugly[i3] * 3
            if ugly[i] == next_5:
                i5 += 1
                next_5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
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
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = 0
        i3 = 0
        i5 = 0
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
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5))
        return ugly[-1]

=======
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5
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
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next_multiple_2 = 2
        next_multiple_3 = 3
        next_multiple_5 = 5
        for i in range(1, n):
            ugly[i] = min(next_multiple_2, next_multiple_3, next_multiple_5)
            if ugly[i] == next_multiple_2:
                i2 += 1
                next_multiple_2 = ugly[i2] * 2
            if ugly[i] == next_multiple_3:
                i3 += 1
                next_multiple_3 = ugly[i3] * 3
            if ugly[i] == next_multiple_5:
                i5 += 1
                next_multiple_5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 10

def nthUglyNumber(self, n: int) -> int:
        # 1. 1 is ugly
        # 2. 1 * 2, 1 * 3, 1 * 5 are ugly
        # 3. if x is ugly, then x * 2, x * 3, x * 5 are ugly
        # 4. only number in ugly number list can be multiplied by 2, 3, 5
        # 5. sort ugly number list after each multiplication
        # 6. set 3 pointers to track the next number to be multiplied by 2, 3, 5
        # 7. after each multiplication, move the corresponding pointer to the next number in the ugly number list
        # 8. return the last number in the ugly number list
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
