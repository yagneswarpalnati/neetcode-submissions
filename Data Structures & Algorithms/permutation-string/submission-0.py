class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        l,l1=[0]*26,[0]*26

        for i in range(len(s1)):
            l[ord(s1[i])-ord('a')]+=1
            l1[ord(s2[i])-ord('a')]+=1
        
        matches=0
        for i in range(26):
            if l[i]==l1[i]:
                matches+=1
        i=0
        for r in range(len(s1),len(s2)):
            if matches==26:return True

            idx=ord(s2[r])-ord('a')
            l1[idx]+=1
            if l[idx]==l1[idx]:
                matches+=1
            elif l[idx]+1==l1[idx]:
                matches-=1

            idx=ord(s2[i])-ord('a')
            l1[idx]-=1
            if l[idx]==l1[idx]:
                matches+=1
            elif l[idx]-1==l1[idx]:
                matches-=1

            i+=1

        return matches==26
        