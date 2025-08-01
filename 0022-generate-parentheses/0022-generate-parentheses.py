class Solution(object):
    def generateParenthesis(self,n):

        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == n * 2:
                result.append(current)
                return
            
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count +1)
            
        
        backtrack("", 0, 0)
        return result

