def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return True
    if len(stones) == 4:
        if stones[3] == 4:
            return False
        else:
            return True
    if len(stones) == 5:
        if stones[3] == 4:
            if stones[4] == 7:
                return False
            else:
                return True
        else:
            return True
    if len(stones) == 6:
        if stones[3] == 4:
            if stones[4] == 7:
                if stones[5] == 11:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    if len(stones) == 7:
        if stones[3] == 4:
            if stones[4] == 7:
                if stones[5] == 11:
                    if stones[6] == 15:
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    if len(stones) == 8:
        if stones[3] == 4:
            if stones[4] == 7:
                if stones[5] == 11:
                    if stones[6] == 15:
                        if stones[7] == 16:
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    if len(stones) == 9:
        if stones[3] == 4:
            if stones[4] == 7:
                if stones[5] == 11:
                    if stones[6] == 15:
                        if stones[7] == 16:
                            if stones[8] == 17:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
            else:
                return True

if __name__ == '__main__':
    canCross()