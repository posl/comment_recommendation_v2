def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    visited = {}
    def dfs(visited, desiredTotal):
        if desiredTotal <= 0:
            return False
        key = tuple(visited)
        if key in visited:
            return visited[key]
        for i in range(maxChoosableInteger, 0, -1):
            if i not in visited:
                visited.add(i)
                if not dfs(visited, desiredTotal - i):
                    visited.remove(i)
                    visited[key] = True
                    return True
                visited.remove(i)
        visited[key] = False
        return False
    return dfs(visited, desiredTotal)

if __name__ == '__main__':
    canIWin()