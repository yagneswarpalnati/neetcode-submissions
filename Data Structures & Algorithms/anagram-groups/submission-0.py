class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            ss=''.join(sorted(s))
            if ss in d:
                d[ss].append(s)
            else:
                d[ss]=[s]

        res=[]
        for key in d.keys():
            res.append(d[key])

        return res