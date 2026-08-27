class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) time and O(1)/O(n+m) space
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)