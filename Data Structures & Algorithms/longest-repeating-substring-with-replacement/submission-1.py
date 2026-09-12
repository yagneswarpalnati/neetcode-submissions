class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        mx=0
        d={}

        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            mx=max(mx,d[s[r]])
            while (r-l+1)-mx>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)

        return res
