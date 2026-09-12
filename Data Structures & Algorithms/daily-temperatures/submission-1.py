class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res=[0]
        ans=[(t[-1],len(t)-1)]

        for i in range(len(t)-2,-1,-1):
            while ans and t[i]>=ans[-1][0]:
                ans.pop()
            if ans:
                res.append(ans[-1][1]-i)
            else:
                res.append(0)
            ans.append((t[i],i))
            

        return res[::-1]


        