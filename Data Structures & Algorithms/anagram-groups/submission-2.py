class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            
            sorted_str = ''.join(sorted(str))

            if sorted_str in groups:
                groups[sorted_str].append(str)
            else:
                groups[sorted_str] = [str]

        return list(groups.values())
