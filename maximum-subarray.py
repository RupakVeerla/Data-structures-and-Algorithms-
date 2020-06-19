#https://en.wikipedia.org/wiki/Maximum_subarray_problem

def maxSubArray(self, nums: List[int]) -> int:
        # current_best = best = nums[0]
        # for i in nums[1:]:
        #     current_best = max(i, current_best+i)
        #     best = max(current_best, best)
        
        current_best = 0
        best = min(nums)
        for i in nums:
            current_best=current_best+i
            if current_best<i:
                current_best = i
            if best < current_best:
                best = current_best
        
        return best
