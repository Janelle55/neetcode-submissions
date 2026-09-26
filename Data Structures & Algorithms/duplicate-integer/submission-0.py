class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}
        for i in nums:
            if i not in new_dict:
                new_dict[i] = 1

            else:
                new_dict[i] += 1
        
        for i in new_dict:
            if new_dict[i] > 1: 
                return True
        return False