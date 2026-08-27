# One quick interview tip:
# Your solution is awesome and will absolutely pass. If the interviewer asks "Can we optimize the constant factors (make it slightly faster in practice, even if Big-O stays the same)?", you can point out that set(window) creates a new data structure every single loop.

# You could replace:
# if len(set(window)) == 1:
# with:
# if num[i] == num[i+1] == num[i+2]:

# This skips slicing the string and skips creating the set entirely, doing the same check slightly faster!
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        max_good = ""
        while i <= len(num) - 3:
            window = num[i:i+3]
            if num[i] == num[i+1] == num[i+2]:
                if window > max_good:
                    max_good = window
            i += 1
        return max_good
                       

