#https://fufuleetcode.github.io/2019/12/31/lc-1/
from typing import List

class Solution:
    def twoSum(self,nums:List[int], target: int) -> List[int]:
        
        #build the mapping from element to the largest index
        hashmap = {}
        for i,num in enumerate(nums):
            hashmap[num] = i
        
        #for every curr, check if target - curr exists
        for idx, curr in enumerate(nums):
            rem = target -curr
            
            if rem in hashmap and hashmap[rem] != idx:
                return [idx, hashmap[rem]]

nums = [1,2,3,4]
so = Solution()
print(Solution().twoSum(nums,5))