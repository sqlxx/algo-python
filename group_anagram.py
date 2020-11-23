class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        map = {}

        for string in strs:
            sorted_value = ''.join(sorted(string))
            if sorted_value in map:
                map[sorted_value].append(string)
            else:
                map[sorted_value] = [string]


        result = []
        for value in map.values():
            result.append(value)

        
        return result