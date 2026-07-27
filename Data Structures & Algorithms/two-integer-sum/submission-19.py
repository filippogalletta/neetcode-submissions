class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # every input has exactly one pair of indices i and j that satisfy the condition

        for i in range(len(nums)):
            m = target - nums[i]
            if m in nums[:i] + nums[i+1:]:
                provisional_list = nums[:i] + nums[i+1:]
                m_index = provisional_list.index(m) + 1
                return [ i, m_index ]