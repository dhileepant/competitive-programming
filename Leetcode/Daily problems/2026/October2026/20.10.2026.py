class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        ts132 = 0

        for k in divisors:
            dna = True
            prev_max = float('-inf')

            for i in range(0, n, k):
                drops = 0
                block_min = nums[i]
                block_max = nums[i]

                for j in range(i, i + k - 1):
                    block_min = min(block_min, nums[j])
                    block_max = max(block_max, nums[j])
                    if nums[j] > nums[j + 1]:
                        drops += 1

                block_min = min(block_min, nums[i + k - 1])
                block_max = max(block_max, nums[i + k - 1])

                if block_min < prev_max:
                    dna = False
                    break

                if drops > 1:
                    dna = 0
                    break
                elif drops == 1:
                    if nums[i + k - 1] > nums[i]:
                        dna = 0
                        break

                prev_max = block_max

            if dna:
                ts132 += k

        return ts132
