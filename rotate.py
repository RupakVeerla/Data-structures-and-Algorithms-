#https://leetcode.com/problems/rotate-array/

def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # nums[k:],nums[:k] = nums[:-k], nums[-k:]
        
        nums[:] = nums[-k:]+nums[:-k]
