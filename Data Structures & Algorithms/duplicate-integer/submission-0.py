class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set of elements in list
        # If len(set) < len(nums) -> Contains Duplicates
        num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        else:
            return False
         