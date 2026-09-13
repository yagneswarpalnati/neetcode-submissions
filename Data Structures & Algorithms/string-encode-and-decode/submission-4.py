class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'@'+s
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=s.find('@',i)
            l=int(s[i:j])
            i=j+1
            res.append(s[i:i+l])
            i+=l

        return res

            


        

