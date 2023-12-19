def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    for i in range(1, len(stones)):
        if stones[i] > stones[i-1] * 2:
            return False
    stones_set = set(stones)
    last_stone = stones[-1]
    positions = [0]
    jumps = [0]
    while positions:
        position = positions.pop()
        jump_distance = jumps.pop()
        for i in range(jump_distance-1, jump_distance+2):
            if i <= 0:
                continue
            next_position = position + i
            if next_position == last_stone:
                return True
            elif next_position in stones_set:
                positions.append(next_position)
                jumps.append(i)
    return False
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
print(canCross([0,2]))
print(canCross([0,1,3,6,10,15,16,21]))
print(canCross([0,1,3,6,10,15,16,21,22]))
print(canCross([0,1,3,6,10,15,16,21,22,23]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24,25]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24,25,26]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24,25,26,27]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24,25,26,27,28]))
print(canCross([0,1,3,6,10,15,16,21,22,23,24,25,26,27,28,29]))
print(can

if __name__ == '__main__':
    canCross()