def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # 1. create a dict of stones and their indexes
    # 2. create a dict of stones and the steps it can take from that stone
    # 3. create a queue of possible steps
    # 4. check if the last stone is in the dict of stones
    # 5. if yes, return True
    # 6. if no, return False
    # 7. check if the last stone is in the dict of steps
    # 8. if yes, return True
    # 9. if no, return False
    # 10. create a set of visited stones
    # 11. while the queue is not empty
    # 12. pop the first element from the queue
    # 13. check if the element is in visited stones
    # 14. if yes, continue
    # 15. if no, add the element to visited stones
    # 16. check if the element is in the dict of steps
    # 17. if yes, add the steps to the queue
    # 18. if no, continue
    # 19. return False
    # 20. create a dict of stones and their indexes
    stones_dict = {stone: index for index, stone in enumerate(stones)}
    # 21. create a dict of stones and the steps it can take from that stone
    stones_steps = {stone: set() for stone in stones}
    # 22. create a queue of possible steps
    steps_queue = set()
    # 23. check if the last stone is in the dict of stones
    if stones[-1] not in stones_dict:
        # 24. if no, return False
        return False
    # 25. if yes, return True
    else:
        return True
    # 26. check if the last stone is in the dict of steps
    if stones[-1] not in stones_steps:
        # 27. if no, return False
        return False
    # 28. if yes, return True
    else:
        return True
    # 29. create a set of visited stones
    visited_stones = set()
    # 30

if __name__ == '__main__':
    canCross()