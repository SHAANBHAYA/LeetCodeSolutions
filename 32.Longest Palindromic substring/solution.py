class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_num_paren=0
        total_num_paren=0
        stack =[]
        for char in s:
            if char==")" and len(stack)>0:
                stack.pop()
                total_num_paren+=2
                if total_num_paren>max_num_paren:
                    max_num_paren=total_num_paren
            else:
                total_num_paren=0
            if char=="(":
                stack.append(char)
        return max_num_paren

a=Solution()
print(a.longestValidParentheses(")()())"))


