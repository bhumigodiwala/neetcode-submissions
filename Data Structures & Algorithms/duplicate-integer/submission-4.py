class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(1) time and O(1) space
        if len(nums) != len(set(nums)):
            return True
        return False