class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        make_zero=False
        for i in range(0, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1 or make_zero:
                obstacleGrid[i][0] = 0
                make_zero=True
            else:
                obstacleGrid[i][0] = 1

        make_zero=False
        for i in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][i]==1 or make_zero:
                obstacleGrid[0][i]=0
                make_zero=True
            else:
                obstacleGrid[0][i]=1


        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[i])):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
        return obstacleGrid[-1][-1]






a=Solution()
print(a.uniquePathsWithObstacles([[0],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[0],[0],[0],[0],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[1],[0],[0],[1],[0],[0],[0],[0],[1]]))




