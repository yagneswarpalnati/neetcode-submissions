class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        mip=prices[0]

        for n in prices:
            res=max(res,n-mip)
            mip=min(n,mip)

        return res
            
        