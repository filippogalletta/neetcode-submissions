class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # every input has exactly one pair of indices i and j that satisfy the condition

        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums:
                if i != nums.index(num):
                    res = []
                    res.append(i)
                    res.append(nums.index(num))
                    res.sort()
                    return res
        return False