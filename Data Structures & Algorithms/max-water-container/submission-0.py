class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        Amax=0
        i,j=0,len(heights)-1
        while i<j:
            A=(j-i)*min(heights[i],heights[j])
            Amax=max(A,Amax)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return Amax

        