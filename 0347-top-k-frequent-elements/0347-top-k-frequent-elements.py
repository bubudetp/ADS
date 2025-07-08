from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hashmap = defaultdict(int)
        output = []

        for num in nums:
            hashmap[num] += 1

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        output = [item[0] for item in sorted_items[:k]]
        return output
         