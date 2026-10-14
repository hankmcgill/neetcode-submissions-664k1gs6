# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            num = (low + high) // 2

            if guess(num) == 0:
                return num
            elif guess(num) == 1:
                low = num + 1
            elif guess(num) == -1:
                high = num - 1