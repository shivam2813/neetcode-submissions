class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += s + '/'
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        data=""
        for c in s:
            if c == '/':
                res.append(data)
                data=""
            else:
                data+=c
        return res