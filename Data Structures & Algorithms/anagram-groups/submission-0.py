class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        map = {}

        for str in strs:
            
            sorted_str = ''.join(sorted(str))

            if sorted_str in map:
                map[sorted_str].append(str)
            else:
                map[sorted_str] = [str]

        answer = []

        for entry in map:
            answer.append(map[entry])

        return answer
