# Definition for a point.
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:

    def getSlope(self,point1,point2):
        return point2.x-point1.x,point2.y-point1.y

    def gcd(self,x,y):
        while (y):
            x, y = y, x % y
        return x

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        solpes_count={}
        max_points=0
        for i in range(len(points)):
            total_count=0
            overlapping_points=0
            vertical_points=0
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    overlapping_points+=1
                elif points[i].x==points[j].x:
                    vertical_points+=1
                else:
                    a,b=self.getSlope(points[i],points[j])
                    gcd_of_slope=self.gcd(a,b)
                    a=a/gcd_of_slope
                    b=b/gcd_of_slope
                    if (a,b,i) in solpes_count:
                        solpes_count[(a,b,i)]=solpes_count[(a,b,i)]+1
                    else:
                        solpes_count[(a,b,i)]=1
                    total_count=max(total_count,solpes_count[(a,b,i)])
                total_count=max(total_count,vertical_points)
            max_points=max(max_points,total_count+overlapping_points+1)

        return max_points


a=Solution()
points=[Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]
print(a.maxPoints(points))