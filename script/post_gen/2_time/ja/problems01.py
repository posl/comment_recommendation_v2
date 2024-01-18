Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

=======
Suggestion 2

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

=======
Suggestion 3

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #numsの長さを取得
        nums_len = len(nums)
        #numsの長さ分ループ
        for i in range(nums_len):
            #numsの長さ分ループ
            for j in range(nums_len):
                #iとjが同じでない場合
                if i != j:
                    #nums[i]とnums[j]を足してtargetと同じ場合
                    if nums[i] + nums[j] == target:
                        #iとjを返す
                        return [i,j]

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #解答
        #ハッシュテーブルを用いる
        #for文でnumsを回し、targetからnumsの値を引いたものがハッシュテーブルにあるか確認する
        #あればそのインデックスと現在のインデックスを返す
        #なければハッシュテーブルに現在のインデックスと値を追加する
        #ハッシュテーブルは辞書型で実装する
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i
        #解答
        #for文でnumsを回し、targetからnumsの値を引いたものがハッシュテーブルにあるか確認する
        #なければハッシュテーブルに現在のインデックスと値を追加する
        #あればそのインデックスとハッシュテーブルのインデックスを返す
        #ハッシュテーブルは辞書型で実装する
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target - nums[i]], i]
            hash_table[nums[i]] = i

=======
Suggestion 8

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        return -1,-1

=======
Suggestion 9

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
