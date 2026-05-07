class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords=defaultdict(list)
        for word in strs:
            sortedword= ''.join(sorted(word))
            sortedWords[sortedword].append(word)

        return list(sortedWords.values())