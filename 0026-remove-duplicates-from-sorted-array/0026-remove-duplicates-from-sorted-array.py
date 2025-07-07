class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        last = len(nums) - 1
        first = 0
        seen = []
        while first <= len(nums) - 1:
            last= len(nums) - 1
            if nums[first] in seen:
                nums.pop(first)
            else:
                seen.append(nums[first])
                first+=1