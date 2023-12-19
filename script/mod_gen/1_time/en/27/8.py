def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # count the number of 1s in each digit
    # 1. 1s in the ones digit: 1, 11, 21, 31, ... 11(n/10), 1(n/10+1)
    # 2. 1s in the tens digit: 10, 11, 12, ... 19, 110, 111, ... 119, 210, 211, ... 219, 310, 311, ... 319, ... 11(n/100), 1(n/100+1)
    # 3. 1s in the hundreds digit: 100, 101, 102, ... 199, 1100, 1101, 1102, ... 1199, 2100, 2101, ... 2199, 3100, 3101, ... 3199, ... 11(n/1000), 1(n/1000+1)
    # ...
    # 4. 1s in the thousands digit: 1000, 1001, 1002, ... 1999, 11000, 11001, 11002, ... 11999, 21000, 21001, ... 21999, 31000, 31001, ... 31999, ... 11(n/10000), 1(n/10000+1)
    # ...
    # 5. 1s in the ten thousands digit: 10000, 10001, 10002, ... 19999, 110000, 110001, 110002, ... 119999, 210000, 210001, ... 219999, 310000, 310001, ... 319999, ... 11(n/100000), 1(n/100000+1)
    # ...
    # 6. 1s in the hundred thousands digit: 100000, 100001, 100002, ... 199999, 1100000, 1100001, 1100002, ... 1199999, 2100000, 2100001, ... 2199999, 3100000, 3100001,

if __name__ == '__main__':
    countDigitOne()