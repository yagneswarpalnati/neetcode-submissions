class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        l=set('({[')
        q=[]

        for c in s:
            if c in l:
                q.append(c)
            elif q and d[c]==q[-1]:
                q.pop()
            else:
                return False
        if q:
            return False

        return True