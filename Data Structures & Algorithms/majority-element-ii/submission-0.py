from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums_freq = defaultdict(int)
        for n in nums:
            nums_freq[n] +=1
        
        for key in nums_freq:
            if nums_freq[key] > len(nums) // 3:
                res.append(key)
        return res