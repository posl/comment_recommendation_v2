#文字列の配列  words (重複なし) が与えられた場合、 与えられた配列 words に含まれるすべての連結された単語を出力せよ。
#連結された単語とは、与えられた配列に含まれる少なくとも2つの短い単語(相異なる必要はない)で完全に構成される文字列と定義する。
#
#例1：
#入力： words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
#出力： ["catsdogcats"、"dogcatsdog"、"ratcatdogcat"]。
#説明： "catsdogcats" は "cats"、"dog"、"cats "で連結できる；
#"dogcatsdogl" は "dog"、"cats"、"dog "で連結できる；
#"ratcatdogcat" は "rat"、"cat"、"dog"、"cat "で連結できる。
#
#例2：
#入力： words = ["cat", "dog", "catdog"]
#出力： ["catdog"]
#
#制約：
#1 <= words.length <= 10^4
#1 <= words[i].length <= 30
#words[i] は英小文字のみで構成される。
#単語の文字列はすべて一意である。
#1 <= sum(words[i].length) <= 10^5
class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]: