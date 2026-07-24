class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        #contraints s.lenght => 1
        #contraints t.lenght <= 5

        for i in s:
            if i not in countS.keys():
                countS[i] = 1
            else:
                countS[i] += 1
        
        for i in t:
            if i not in countT.keys():
                countT[i] = 1
            else:
                countT[i] += 1

        # confronto
        """ for k in countS.keys():
            if k not in countT.keys():
                return False
            else:
                if countS[k] != countT[k]:
                    return False
        
        for k in countT.keys():
            if k not in countS.keys():
                return False
            else:
                if countT[k] != countS[k]:
                    return False

        return True"""

        return countS == countT