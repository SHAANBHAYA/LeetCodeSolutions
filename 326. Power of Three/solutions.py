class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return self.convertToBase3(n)


    def convertToBase3(self, num):
        while (num > 1):
            rem = num % 3
            if rem!=0:
                return False
            num = int(num / 3)
        if num !=1:
            return False
        return True



a=Solution()
print(a.isPowerOfThree(2434))