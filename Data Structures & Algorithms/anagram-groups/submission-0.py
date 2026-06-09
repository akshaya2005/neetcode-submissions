class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dic = defaultdict(list)
        for i in range(len(strs)):
            string = ''.join(sorted(strs[i]))
            dic[string].append(strs[i])
        
        for string, strings in dic.items():
            result.append(strings)

        return result

        