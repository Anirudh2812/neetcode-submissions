class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+ "@" +s
        return result
    def decode(self, s: str) -> List[str]:
            result = []
            i = 0
            while i < len(s):
                j = s.index("@", i)        # find the @ symbol
                length = int(s[i:j])       # number before @ is the length
                result.append(s[j+1: j+1+length])  # read that many characters
                i = j + 1 + length         # move pointer forward
            return result