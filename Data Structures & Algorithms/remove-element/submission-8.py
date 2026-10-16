class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
               
            else:
                i += 1  
                
        return len(nums)
           """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # On supprime physiquement tout ce qui dépasse de k
        del nums[k:]
        
        return k 



        