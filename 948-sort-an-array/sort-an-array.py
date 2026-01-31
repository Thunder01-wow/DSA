class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr,L,Mid,R):
            left=arr[L:Mid+1]
            right=arr[Mid+1:R+1]
            i,j,k=L,0,0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            
            while j < len(left):
                arr[i] = left[j]
                j+=1
                i+=1
            
            while k < len(right):
                arr[i] = right[k]
                k+=1
                i+=1
            
        def MergeSort(arr,l,r):
            if l == r:
                return arr
            
            mid = (l+r)//2
            MergeSort(arr,l,mid)
            MergeSort(arr,mid+1,r)
            merge(arr,l,mid,r)
            return arr
        
        return MergeSort(nums,0,len(nums)-1)

            

        