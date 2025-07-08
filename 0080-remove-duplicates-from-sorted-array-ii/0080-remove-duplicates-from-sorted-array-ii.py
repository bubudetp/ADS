class Solution(object):
    def removeDuplicates(self,nums):
        first = 0
        counts = {}

        while first < len(nums):
            val = nums[first]
            counts[val] = counts.get(val, 0) + 1

            if counts[val] > 2:
                nums.pop(first)  # Don't increment `first`, element has shifted
            else:
                first += 1       # Keep element, go to next index

        return len(nums)
