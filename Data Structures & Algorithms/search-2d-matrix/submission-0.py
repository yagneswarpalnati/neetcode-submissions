class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        t,d=0,m-1
        while t<=d:
            row=(t+d)//2
            if target>matrix[row][-1]:
                t=row+1
            elif target<matrix[row][0]:
                d=row-1
            else:
                break
        if not (t<=d):return False
        row=(t+d)//2
        l,r=0,n-1
        while l<=r:
            col=(l+r)//2
            if target>matrix[row][col]:
                l=col+1
            elif target<matrix[row][col]:
                r=col-1
            else:
                return True
        return False



