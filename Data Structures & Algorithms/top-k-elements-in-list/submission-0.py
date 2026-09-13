class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        res=[]
        for key in d:
            heapq.heappush(res,(d[key],key))
            if len(res)>k:
                heapq.heappop(res)

        return [val for key,val in res]
        