Synthesizing 9/10 solutions

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            for j in str(i):
                if j == "1":
                    count += 1
        return count

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            count += self.countOne(i)
        return count

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        count = 0
        for i in range(1, n + 1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

=======
Suggestion 4

class Solution:
    def countDigitOne(self, n: int) -> int:
        #1の位を数える
        #10の位を数える
        #100の位を数える
        #1000の位を数える
        #10000の位を数える
        #100000の位を数える
        #1000000の位を数える
        #10000000の位を数える
        #100000000の位を数える
        #1000000000の位を数える
        #10000000000の位を数える
        #100000000000の位を数える
        #1000000000000の位を数える
        #10000000000000の位を数える
        #100000000000000の位を数える
        #1000000000000000の位を数える
        #10000000000000000の位を数える
        #100000000000000000の位を数える
        #1000000000000000000の位を数える
        #10000000000000000000の位を数える
        #100000000000000000000の位を数える
        #1000000000000000000000の位を数える
        #10000000000000000000000の位を数える
        #100000000000000000000000の位を数える
        #1000000000000000000000000の位を数える
        #10000000000000000000000000の位を数える
        #100000000000000000000000000の位を数える
        #1000000000000000000000000000の位を数える
        #10000000000000000000000000000の位を数える
        #100000000000000000000000000000の位を数える
        #1000000000000000000000000000000の位を数える
        #10000000000000000000000000000000の位を数える
        #1000

=======
Suggestion 5

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1 10 100 1000 10000 ...
        # 1 11 111 1111 11111 ...
        # 1 2  3   4    5
        # 1 3  6   10   15
        # 1 4  10  20   35
        # 1 5  15  35   70
        # 1 6  21  56   126
        # 1 7  28  84   210
        # 1 8  36  120  330
        # 1 9  45  165  495
        # 1 10 55  220  715
        # 1 11 66  286  1001
        # 1 12 78  364  1365
        # 1 13 91  455  1820
        # 1 14 105 560  2380
        # 1 15 120 680  3060
        # 1 16 136 816  3876
        # 1 17 153 969  4845
        # 1 18 171 1140 5985
        # 1 19 190 1330 7315
        # 1 20 210 1540 8855
        # 1 21 231 1771 10626
        # 1 22 253 2024 12650
        # 1 23 276 2300 14975
        # 1 24 300 2600 17625
        # 1 25 325 2925 20650
        # 1 26 351 3276 24076
        # 1 27 378 3654 27930
        # 1 28 406 4060 32215
        # 1 29 435 4495 36905
        # 1 30 465 4960 42000
        # 1 31 496 5456 47520
        # 1 32 528

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        count = 0
        for i in range(1,n+1):
            count += str(i).count("1")
        return count

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            ans += str(i).count('1')
        return ans

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        ans = 0
        # 1桁目から順に処理する
        for keta in range(len(str(n))):
            # 1の位から順に処理する
            for i in range(10):
                # 1の位がiのときの数を数える
                num = 10**keta * i
                # keta桁目までの数を数える
                num += 10**(keta-1) * (keta-1) * 9
                # keta桁目がiのときの数を数える
                if i == 1:
                    num += n%(10**keta) + 1
                elif i > 1:
                    num += 10**keta
                # keta桁目がiのときの数を足す
                ans += num
            # print(ans)
        return ans

=======
Suggestion 9

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1 <= n <= 2*10^9
        # 0 <= n <= 10^9
        # 1 <= n <= 10^9
        # 1 <= n <= 10^9
