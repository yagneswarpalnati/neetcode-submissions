class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        s=set(nums)
        for n in nums:
            if n-1 not in s:
                ans=1
                while n+ans in s:
                    ans+=1
                res=max(res,ans)

        return res

        