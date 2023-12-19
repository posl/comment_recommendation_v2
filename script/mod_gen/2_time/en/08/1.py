def rotateArray(nums, k):
    if k == 0:
        return nums
    elif k > 0:
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums
    else:
        for i in range(abs(k)):
            nums.append(nums.pop(0))
        return nums

if __name__ == '__main__':
    rotateArray()