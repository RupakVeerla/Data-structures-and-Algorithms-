#https://leetcode.com/problems/contains-duplicate

def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
          return False
        return True
