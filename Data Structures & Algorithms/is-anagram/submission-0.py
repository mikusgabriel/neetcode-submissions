class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for x in s:
            if x in map:
                map[x] += 1 
            else:
                map[x] = 1

        for x in t:
            if x in map:
                map[x] -=1
            else:
                return False

        for x in map:
            if map[x] > 0:
                return False

        return True
        