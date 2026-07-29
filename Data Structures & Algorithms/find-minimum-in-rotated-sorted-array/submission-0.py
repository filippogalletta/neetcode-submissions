class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        [1,2,3,4,5,6] -> 3<6 -> right = mid - 1
        [5,6,1] -> 6>1 -> left = mid+1
        [1]
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (right + left) // 2

            if left == right:
                return nums[mid]
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid 
            