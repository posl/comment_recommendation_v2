Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        #上記のやり方だと計算量がO(n^2)となってしまうので、辞書を使う
        #辞書のキーはリストの値、値はリストのインデックス
        dic = {}
        for i in range(len(nums)):
            #targetからリストの値を引いた値が辞書のキーにあるかどうか
            if target - nums[i] in dic:
                #ある場合はその値のインデックスと今の値のインデックスを返す
                return [dic[target-nums[i]],i]
            #ない場合は辞書に追加
            dic[nums[i]] = i
        return []

=======
Suggestion 2

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
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
                    return [i,j]
        return []

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        return [i,j]
                else:
                    continue

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return[i, j]

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        return None

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #解法1:2重ループで総当たり
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i]+nums[j]==target:
        #            return [i,j]
        #解法2:辞書を使って既に調べた数字を記録しておく
        #memo={}
        #for i in range(len(nums)):
        #    if target-nums[i] in memo:
        #        return [memo[target-nums[i]],i]
        #    memo[nums[i]]=i
        #解法3:辞書を使って既に調べた数字を記録しておく
        memo={}
        for i,num in enumerate(nums):
            if target-num in memo:
                return [memo[target-num],i]
            memo[num]=i

=======
Suggestion 8

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return [0, 0]
