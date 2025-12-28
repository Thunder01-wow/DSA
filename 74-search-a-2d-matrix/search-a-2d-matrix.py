class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top,bottom=0,rows-1

        while top<=bottom:
            curr=(top+bottom)//2
            if target > matrix[curr][-1]:
                top=curr+1
            elif target < matrix[curr][0]:
                bottom=curr-1
            else:
                break
        curr=(top+bottom)//2
        l,r=0,cols-1
        while l<=r:
            mid=(l+r)//2
            if target ==matrix[curr][mid]:
                return True
            elif target > matrix[curr][mid]:
                l=mid+1
            else:
                r=mid-1
        return False