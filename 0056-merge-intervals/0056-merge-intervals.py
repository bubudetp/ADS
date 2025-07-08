class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []
        t1, t2 = 0, 1
        current_interval = intervals[0]

        while t2 < len(intervals):
            next_interval = intervals[t2]

            if current_interval[1] >= next_interval[0]:
                current_interval[1] = max(next_interval[1], current_interval[1])
            else:
                result.append(current_interval)
                current_interval = next_interval

            t2 += 1
        
        result.append(current_interval)
        return result
        
            

