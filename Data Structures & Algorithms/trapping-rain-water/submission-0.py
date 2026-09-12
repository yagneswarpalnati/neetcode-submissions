class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1
        lm,rm=height[l],height[r]
        while l<r:
            if lm<rm:
                res+=lm-height[l]
                l+=1
                if height[l]>lm:
                    lm=height[l]
            else:
                res+=rm-height[r]
                r-=1
                if height[r]>rm:
                    rm=height[r]

        return res