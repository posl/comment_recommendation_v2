class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # 1 <= s.length <= 10^5
        # sは英小文字からなる。
        # ベースとなる文字列を作成
        base = 'abcdefghijklmnopqrstuvwxyz'
        # ベースとなる文字列の長さ
        base_len = len(base)
        # ベースとなる文字列を２倍にする
        base = base + base
        # 重複を削除するためにsetにする
        # 重複を削除した文字列を返す
        # 例えば、s = "cac"
        # s[0] = 'c'の場合、s[0] = 'c'の文字列を返す
        # s[1] = 'a'の場合、s[1] = 'a'の文字列を返す
        # s[2] = 'c'の場合、s[2] = 'c'の文字列を返す
        # set(['c', 'a', 'c']) = {'c', 'a'}
        # となり重複を削除する
        s = set(s)
        # ベースとなる文字列の長さ
        # ここでは、26
        # base_len = len(base)
        # ベースとなる文字列を２倍にする
        # base = base + base
        # base = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        # ベースとなる文字列の長さを取得
        # ここでは、52
        # base_len = len(base)
        # ベースとなる文字列を２倍にする
        # base = base + base
        # base = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        # ベースとなる文字列の長さを取得
        # ここでは、104
        # base_len = len(base)
        # ベースとなる文字列を２倍にする
        # base = base + base
        # base = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx

if __name__ == '__main__':
    s = input()
    a = Solution()
    print(a.findSubstringInWraproundString(s))