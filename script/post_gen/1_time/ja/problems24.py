Synthesizing 10/10 solutions

=======
Suggestion 1

def numDistinct(self, s: str, t: str) -> int:
        # メモ化再帰
        memo = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i+1, j) + dfs(i+1, j+1)
            else:
                memo[(i, j)] = dfs(i+1, j)
            return memo[(i, j)]
        return dfs(0, 0)

=======
Suggestion 2

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for j in range(1, len(t) + 1):
            for i in range(1, len(s) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(s)][len(t)]

=======
Suggestion 3

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までで作れる数
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        # 0文字目までで作れる数は1通り
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                # s[i-1]とt[j-1]が等しいとき、s[i-1]を使うか使わないかで分岐
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                # s[i-1]とt[j-1]が等しくないとき、s[i-1]を使わない
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

=======
Suggestion 4

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までで、tを作る方法の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[-1][-1]

=======
Suggestion 5

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目まででtのj文字目まで使ってできる部分列の数
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1): dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                # tのj文字目がsのi文字目と一致する場合、
                # sのi文字目を使う場合と使わない場合の合計
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                # tのj文字目がsのi文字目と一致しない場合、
                # sのi文字目を使わない場合のみ
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

=======
Suggestion 6

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

=======
Suggestion 7

def numDistinct(self, s: str, t: str) -> int:
        #tの文字列の長さが0ならば1を返す
        if len(t) == 0:
            return 1
        #sの文字列の長さが0ならば0を返す
        if len(s) == 0:
            return 0
        #dpテーブルを作成。tの文字列の長さ+1のテーブルを作成する
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        #dpテーブルの0行目を1にする
        for i in range(len(s) + 1):
            dp[i][0] = 1
        #sの文字列の長さ分ループ
        for i in range(len(s)):
            #tの文字列の長さ分ループ
            for j in range(len(t)):
                #sのi番目の文字列とtのj番目の文字列が同じならば
                if s[i] == t[j]:
                    #dpテーブルのi+1行目j+1列目にdpテーブルのi行目j列目とi行目j+1列目の和を入れる
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                #sのi番目の文字列とtのj番目の文字列が同じでないならば
                else:
                    #dpテーブルのi+1行目j+1列目にdpテーブルのi行目j+1列目を入れる
                    dp[i + 1][j + 1] = dp[i][j + 1]
        #dpテーブルのsの文字列の長さ行目tの文字列の長さ列目を返す
        return dp[len(s)][len(t)]

=======
Suggestion 8

def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[-1][-1]

=======
Suggestion 9

def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] := sのi文字目までとtのj文字目までで作れる部分列の数
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)
        return dp[len(s)][len(t)]

=======
Suggestion 10

def numDistinct(self, s: str, t: str) -> int:
        #dp[i][j] = s[i]まででt[j]を作る場合の数
        #s[i] == t[j]のときは、dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        #s[i] != t[j]のときは、dp[i][j] = dp[i-1][j]
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]
