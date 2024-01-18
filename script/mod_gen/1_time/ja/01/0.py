class Solution:
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

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    a = Solution()
    print(a.twoSum(nums, target))