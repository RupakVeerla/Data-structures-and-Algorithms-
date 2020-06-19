#https://leetcode.com/problems/move-zeroes/

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    #nums.sort(key = lambda x:x == 0)
    
    idx = 0
    for i in range(len(nums)):
      if nums[i]!= 0:
        nums[idx], nums[i] = nums[i], nums[idx]
        idx+=1
