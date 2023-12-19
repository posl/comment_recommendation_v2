def canCross(self, stones: List[int]) -> bool:
    if stones[1] != 1:
        return False
    
    d = {}
    for stone in stones:
        d[stone] = set()
    d[stones[1]].add(1)
    
    for stone in stones[1:]:
        for step in d[stone]:
            for i in range(step-1, step+2):
                if i > 0 and stone+i in d:
                    d[stone+i].add(i)
    
    return len(d[stones[-1]]) > 0

if __name__ == '__main__':
    canCross()