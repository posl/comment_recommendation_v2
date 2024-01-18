Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            count += str(i).count("1")
        return count

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            count += str(i).count('1')
        return count

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        count = 0
        len_n = len(str(n))
        for i in range(len_n):
            if i == 0:
                if n % 10 == 0:
                    count += n // 10
                elif n % 10 == 1:
                    count += n // 10 + 1
                else:
                    count += n // 10 + 1
            elif i == len_n - 1:
                count += 1
            else:
                if n // 10 ** i % 10 == 0:
                    count += n // 10 ** (i + 1) * 10 ** i
                elif n // 10 ** i % 10 == 1:
                    count += n // 10 ** (i + 1) * 10 ** i + n % 10 ** i + 1
                else:
                    count += (n // 10 ** (i + 1) + 1) * 10 ** i
        return count

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 10:
            return 1
        elif n < 100:
            return 20
        elif n < 1000:
            return 300
        elif n < 10000:
            return 4000
        elif n < 100000:
            return 50000
        elif n < 1000000:
            return 600000
        elif n < 10000000:
            return 7000000
        elif n < 100000000:
            return 80000000
        elif n < 1000000000:
            return 900000000
        else:
            return 1000000000

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        def countOne(n):
            if n <= 0:
                return 0
            if n < 10:
                return 1
            str_n = str(n)
            high = int(str_n[0])
            pow = 10 ** (len(str_n) - 1)
            last = n - high * pow
            if high == 1:
                return self.countDigitOne(pow - 1) + self.countDigitOne(last) + last + 1
            else:
                return pow + high * self.countDigitOne(pow - 1) + self.countDigitOne(last)
        return countOne(n)

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        # 数字を文字列に変換して、桁ごとに分ける
        s = str(n)
        # 例えば、n = 1234 とすると、
        # 1000 以下の数字に含まれる 1 の個数 + 200 以下の数字に含まれる 1 の個数 + 30 以下の数字に含まれる 1 の個数 + 4 以下の数字に含まれる 1 の個数
        # という風に考えることができる
        # 例えば、200 以下の数字に含まれる 1 の個数は、100 以下の数字に含まれる 1 の個数 * 2 という風に考えることができる
        # 例えば、30 以下の数字に含まれる 1 の個数は、10 以下の数字に含まれる 1 の個数 * 3 という風に考えることができる
        # 例えば、4 以下の数字に含まれる 1 の個数は、1 以下の数字に含まれる 1 の個数 * 4 という風に考えることができる
        # という風に考えることができる
        # 例えば、1234 という数字に含まれる 1 の個数は、1 以下の数字に含まれる 1 の個数 * 4 + 10 以下の数字に含まれる 1 の個数 * 3 + 100 以下の数字に含まれる 1 の個数 * 2 + 1000 以下の数字に含まれる 1 の個数 * 1 という風に考えることができる
        # というわけで、1 以下の数字に含まれる 1 の個数、10 以下の数字に含まれる

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        # 1桁目を見る
        # 1桁目が0なら、それ以降の数字が出現する回数
        # 1桁目が1なら、それ以降の数字が出現する回数 + 1
        # 1桁目が2以上なら、10**(桁数-1) + 10**(桁数-1) * (1桁目-1) + それ以降の数字が出現する回数
        # 2桁目を見る
        # 2桁目が0なら、それ以降の数字が出現する回数
        # 2桁目が1なら、それ以降の数字が出現する回数 + 1
        # 2桁目が2以上なら、10**(桁数-2) + 10**(桁数-2) * (2桁目-1) + それ以降の数字が出現する回数
        # ...
        # 1桁目を見る
        # 1桁目が0なら、それ以降の数字が出現する回数
        # 1桁目が1なら、それ以降の数字が出現する回数 + 1
        # 1桁目が2以上なら、10**(桁数-1) + 10**(桁数-1) * (1桁目-1) + それ以降の数字が出現する回数
        if n < 1:
            return 0
        if n < 10:
            return 1
        digit = len(str(n))
        power = 10**(digit-1)
        first_digit = n // power
        rest = n % power
        if first_digit == 0:
            return self.countDigitOne(rest)
        if first_digit == 1:
            return rest + 1 + self.countDigitOne(rest) + self.countDigitOne(power-1)
        return power + power * (first_digit-1) + self.countDigitOne(rest) + self.countDigitOne(power-1)

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        ans = 0
        m = 1
        while n >= m:
            ans += (n//(m*10))*m + min(max(n%(m*10)-m+1, 0), m)
            m *= 10
        return ans

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        # 1の桁の数を数える
        def get_ones_count(num: int) -> int:
            cnt = 0
            while num > 0:
                if num % 10 == 1:
                    cnt += 1
                num //= 10
            return cnt

        ans = 0
        # 1の桁から順に1の数を数えていく
        for i in range(1, len(str(n)) + 1):
            # 1の桁を取得
            digit = n % 10 ** i
            # 1の桁を取り除く
            n -= digit
            # 1の桁の数を数える
            ans += get_ones_count(digit)
        return ans
