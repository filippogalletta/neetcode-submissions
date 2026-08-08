class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #idea: crea un dizionario
        #k: array, v: stringa

        anagrams = defaultdict(list)

        for s in strs:

            count = [0] * 26

            for l in s:
                # aggiorna l'array
                num = ord(l) - ord('a')
                count[num] += 1

            anagrams[tuple(count)].append(s)

        return list(anagrams.values())