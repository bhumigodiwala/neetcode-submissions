class Solution:

    def encode(self, strs: List[str]) -> str:
        # let hash be delimiter because that is no ascii
        # hash followed by length of str m and total no of strings = n
        # addprefix to string of hash and length of str
        res = ""
        for string in strs: 
            res += str(len(string))+"#"+string
        return (res)

    def decode(self, s: str) -> List[str]:
        # encodes str  -> 5#Hello5#World
        # ouput is list of strs
        res, i = [], 0
        # i is the pointer index in the encoded str

        while i < len(s):
            # read char by char
            # first position is integer = 5 
            # use anothe rpointer index j to find the delimiter
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #this gives us 5
            # there now my first string is going to start from j+1 to length
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

       