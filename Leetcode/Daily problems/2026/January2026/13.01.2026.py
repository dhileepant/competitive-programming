class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        my, ta = 0, 0
        for x, y, l in squares:
            ta += l**2
            my = max(my, y + l)

        def check(ly):
            area = 0
            for x, y, l in squares:
                if y < ly:
                    area += l * min(ly - y, l)
            return area >= ta / 2

        l, ans = 0, my
        i = 1e-5
        while abs(ans - l) > i:
            mid = (ans + l) / 2
            if check(mid):
                ans = mid
            else:
                l = mid

        return ans
