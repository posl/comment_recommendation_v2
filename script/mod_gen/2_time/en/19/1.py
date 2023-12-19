def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    # if desiredTotal is 0, then first player always wins
    if desiredTotal == 0:
        return True
    # if the sum of all numbers from 1 to maxChoosableInteger is less than desiredTotal, then first player always loses
    if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
        return False
    # if the sum of all numbers from 1 to maxChoosableInteger is equal to desiredTotal, then if maxChoosableInteger is odd, first player wins, else first player loses
    if maxChoosableInteger*(maxChoosableInteger+1)/2 == desiredTotal:
        return maxChoosableInteger%2 == 1
    # if the sum of all numbers from 1 to maxChoosableInteger is greater than desiredTotal, then first player can win if any of the numbers from 1 to maxChoosableInteger can be chosen such that the next player loses
    # use a dictionary to store the result of the game for a given state of the game
    # key is the list of numbers that have not been chosen yet
    # value is True if first player can win, else False
    # initially, all values are None
    cache = {}
    def canWin(nums, desiredTotal):
        if tuple(nums) in cache:
            return cache[tuple(nums)]
        # if the largest number in nums is greater than or equal to desiredTotal, then first player can win by choosing that number
        if nums[-1] >= desiredTotal:
            cache[tuple(nums)] = True
            return True
        # if the largest number in nums is less than desiredTotal, then first player can win if any of the numbers in nums can be chosen such that the next player loses
        for i in range(len(nums)):
            # if the next player loses when first player chooses nums[i], then first player wins
            if not canWin(nums[:i]+nums[i+1:], desiredTotal-nums[i]):
                cache[tuple(nums)] = True
                return True
        # if the next player wins no matter which number in nums is chosen by first player

if __name__ == '__main__':
    canIWin()