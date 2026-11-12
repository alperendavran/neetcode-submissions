class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Sayı → frekans
        frequency_count = {}

        for num in nums:
            if num not in frequency_count:
                frequency_count[num] = 0

            frequency_count[num] += 1

        # 2. Frekans → o frekansta geçen sayılar
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in frequency_count.items():
            buckets[count].append(num)

        # 3. En yüksek frekanstan başlayarak k sayı topla
        result = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result