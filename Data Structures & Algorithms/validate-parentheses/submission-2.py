class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(',']':'[','}':'{'}
        q=[]

        for c in s:
            if c not in d:
                q.append(c)
            elif q and d[c]==q[-1]:
                q.pop()
            else:
                return False
        if q:
            return False

        return True