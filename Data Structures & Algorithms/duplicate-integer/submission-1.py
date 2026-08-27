class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach 1: Hashset
        # O(n) time and O(n) space
        # Create a hashset
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        # Create a set of elements in list
        # If len(set) < len(nums) -> Contains Duplicates
        # num_set = set(nums)
        # if len(num_set) < len(nums):
        #     return True
        # else:
        #     return False
         