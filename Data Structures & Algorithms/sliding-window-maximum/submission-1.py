class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=deque()
        res=[]
        for i in range(k):
            while d and (nums[d[-1]]<nums[i] or d[0]<(i-k+1)):
                d.pop()
            d.append(i)
        res.append(nums[d[0]])
        for i in range(k,len(nums)):
            while d and (nums[d[-1]]<nums[i]):
                # print("inside:",d)
                d.pop()
            d.append(i)
            if d[0]<(i-k+1):
                d.popleft()
            
            # print(d)
            res.append(nums[d[0]])

        return res
            
