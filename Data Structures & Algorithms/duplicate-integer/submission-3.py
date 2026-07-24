class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in nums:
            if i not in duplicates.keys():
                duplicates[i] = 1
            else: 
                duplicates[i] += 1
        for i in duplicates.values():
            print(i)
            if i != 1:
                return True
        else:
            return False