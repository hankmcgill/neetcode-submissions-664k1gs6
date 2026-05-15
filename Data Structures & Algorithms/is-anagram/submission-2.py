class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for char in t:
            if not char in letters:
                return False
            letters[char] -= 1
            if letters[char] < 0:
                return False

        for letter in letters:
            if letters[letter] > 0:
                return False
        return True