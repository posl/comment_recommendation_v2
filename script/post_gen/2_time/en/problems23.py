Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

=======
Suggestion 2

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        result = 0
        while (minutesToTest/minutesToDie + 1)**result < buckets:
            result += 1
        return result

=======
Suggestion 3

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest//minutesToDie + 1))

=======
Suggestion 4

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets) / log(minutesToTest // minutesToDie + 1))

=======
Suggestion 5

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        import math
        return math.ceil(math.log(buckets, (minutesToTest // minutesToDie) + 1))

=======
Suggestion 6

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        n = minutesToTest//minutesToDie
        pigs = 0
        while n**pigs < buckets:
            pigs += 1
        return pigs

=======
Suggestion 7

def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
