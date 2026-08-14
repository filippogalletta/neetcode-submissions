class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # every input has exactly one pair of indices i and j that satisfy the condition

        indices = defaultdict(int)
        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            num = target - nums[i]
            if num in indices and indices[num] != i:
                return [i, indices[num]]
        return []