class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        
        while i < j:
            if height[i] < height[j]:
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    ans += left_max - height[i]
                i += 1
            else:
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    ans += right_max - height[j]
                j -= 1
                
        return ans