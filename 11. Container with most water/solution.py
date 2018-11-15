class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        max_area=0
        while(start <=end):
            min_height=min(height[end],height[start])
            temp_area=(end-start)*min_height
            if temp_area > max_area:
                max_area=temp_area

            if min_height==height[end]:
                end-=1
            else:
                start+=1
        return max_area

a=Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))

