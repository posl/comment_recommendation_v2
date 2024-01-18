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
        # ループで回す
        for i in range(len(nums)):
            # ループで回す
            for j in range(len(nums)):
                # i と j が同じ数値の場合は処理をしない
                if i == j:
                    continue
                # i と j の合計が target と同じ場合は i と j の値を返す
                if nums[i] + nums[j] == target:
                    return [i, j]
        # 見つからなかった場合は空の配列を返す
        return []

=======
Suggestion 3

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #配列の長さを取得
        nums_len = len(nums)
        #配列の長さ分for文を回す
        for i in range(nums_len):
            #配列の長さ分for文を回す
            for j in range(nums_len):
                #iとjが同じ数字の場合はfor文を抜ける
                if i == j:
                    continue
                #iとjの値を足してtargetと同じ場合
                if nums[i] + nums[j] == target:
                    #インデックスを返す
                    return [i,j]

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                else:
                    continue
        return [0, 0]

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []

=======
Suggestion 8

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #辞書を用意する
        dic = {}
        #enumerateでインデックスを取得する
        for i, num in enumerate(nums):
            #targetからnumを引いた値がdicの中にあれば、そのインデックスとiを返す
            if target - num in dic:
                return [dic[target - num], i]
            #なければdicにnumをキー、iを値として追加する
            dic[num] = i
        #ループが終わったら、答えがないので、空のリストを返す
        return []
