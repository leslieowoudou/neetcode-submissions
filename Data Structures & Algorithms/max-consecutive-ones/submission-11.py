class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        
        
        
        for i in range (len(nums)):
            courant=nums[i]
            count=0
            j=i
            while courant==1 :
                count+=1
                if  j+1<len(nums):
                   j+=1
                   courant = nums[j]

                else :
                    break
                
            if max<count:
                max=count
            
        return max
        