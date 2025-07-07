class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        last = len(nums) - 1
        first = 0
        while first <= len(nums) -1:
            if nums[first] == val:
                count +=1
                nums.pop(first)
            else:
                first+=1