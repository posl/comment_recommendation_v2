def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    tails = []
    for _, h in envelopes:
        l, r = 0, len(tails)
        while l < r:
            mid = (l + r) // 2
            if tails[mid] < h:
                l = mid + 1
            else:
                r = mid
        if r == len(tails):
            tails.append(h)
        else:
            tails[r] = h
    return len(tails)

if __name__ == '__main__':
    maxEnvelopes()