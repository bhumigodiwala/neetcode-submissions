class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        max_good = ""
        while i <= len(num) - 3:
            window = num[i:i+3]
            if len(set(window)) == 1:
                if window > max_good:
                    max_good = window
            i += 1
        return max_good
                       

