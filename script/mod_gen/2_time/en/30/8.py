def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) < 2:
        return True
    # create a dictionary of all the stones
    stone_dict = {}
    for i in range(len(stones)):
        stone_dict[stones[i]] = i
    # create a dictionary of all the jumps
    jump_dict = {}
    for i in range(len(stones)):
        jump_dict[stones[i]] = set()
    # the first jump is always 1
    jump_dict[0].add(1)
    # iterate through each stone
    for i in range(len(stones)):
        # iterate through each jump
        for j in jump_dict[stones[i]]:
            # check if the jump is valid
            if stones[i] + j in stone_dict:
                # add the jump to the next stone
                jump_dict[stones[i] + j].add(j)
                # check if the jump is valid
                if j - 1 > 0:
                    jump_dict[stones[i] + j].add(j - 1)
                jump_dict[stones[i] + j].add(j + 1)
    # check if the last stone has a jump
    if len(jump_dict[stones[-1]]) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    canCross()