class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2) time and O(1) space
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # One pass solution 
        # use hashet
        # O(n) time
        hashset = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in hashset:
                return [hashset[diff], idx]
            hashset[val] = idx