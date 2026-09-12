class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='':
            return ''
        d=Counter(t)
        have=0
        need=len(d)
        d1={}
        l=0
        res=float('inf')
        ans=''
        for r,c in enumerate(s):
            d1[c]=d1.get(c,0)+1
            if c in d and d[c]==d1[c]:
                have+=1
            
            while have==need:
                res=min(res,r-l+1)
                if res==(r-l+1):
                    ans=s[l:r+1]

                d1[s[l]]-=1
                if s[l] in d and d1[s[l]]<d[s[l]]:
                    have-=1
                l+=1

        return ans if res!=float('inf') else ''
