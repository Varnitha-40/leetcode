class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits)))
        num_str = str(num + 1)
        return [int(d) for d in num_str]
