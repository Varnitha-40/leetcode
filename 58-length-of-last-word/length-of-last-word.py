class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        for i in words:
            last=i
        return len(last)        