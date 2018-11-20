class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_of_s = len(s)
        is_Palindrome=[]
        for i in range(len_of_s):
            list=[]
            for j in range(len_of_s):
                if i==j:
                    list.append(1)
                else:
                    list.append(0)
            is_Palindrome.append(list)

        max_left=0
        max_right=0

        for j in range(1,len_of_s):
            range_for_i=len_of_s-j
            for i in range(0,range_for_i):
                left=i
                right=j+i
                right_S=s[right]
                left_S=s[left]
                if right-left<2:
                    if left_S==right_S:
                        is_Palindrome[left][right]=1
                        if right-left>max_right-max_left:
                            max_right=right
                            max_left=left

                elif left_S==right_S and is_Palindrome[left+1][right-1]==1:
                        is_Palindrome[left][right]=1
                        if right-left>max_right-max_left:
                            max_right=right
                            max_left=left

        return s[max_left:max_right+1]


a=Solution()
print(a.longestPalindrome("abba"))