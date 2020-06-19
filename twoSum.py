# https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for k,v in enumerate(nums):
            req_num = target - v
            if req_num not in h:
                h[v] = k
                continue
            return [h[req_num],k]
