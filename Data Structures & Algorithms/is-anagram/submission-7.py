class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for l in s:
            countS[l] = countS.get(l, 0) + 1
        for l in t:
            countT[l] = countT.get(l, 0) + 1

        return countS == countT