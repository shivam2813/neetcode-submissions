class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data={}

        for s in strs:
            sort="".join(sorted(s))
            print(sort)
            if sort not in data:
                data[sort]=[]
            data[sort].append(s)

        return list(data.values())