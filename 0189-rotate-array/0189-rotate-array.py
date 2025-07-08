from collections import deque
class Solution(object):
    def rotate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(arr) if arr else 0
        print(k)

        if k > 0:
            arr[:] = arr[-k:] + arr[:-k]        
    