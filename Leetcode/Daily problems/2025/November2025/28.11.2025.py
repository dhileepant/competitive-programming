class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        g = defaultdict(list)
        deg = [0] * n
        cnt = 0
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = deque(i for i in range(n) if deg[i] == 1)

        while q:
            u = q.popleft()
            deg[u] -= 1
            add = 0

            if values[u] % k == 0:
                cnt += 1
            else:
                add = values[u]

            for nei in g[u]:
                if deg[nei] == 0:
                    continue
                deg[nei] -= 1
                values[nei] += add
                if deg[nei] == 1:
                    q.append(nei)

        return cnt
