class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        left = [1] * n
        right = [1] * n

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            right[j] = right[j+1] * nums[j + 1]
        
        for x in range(len(nums)):
            output[x] = left[x] * right[x]
        
        return output