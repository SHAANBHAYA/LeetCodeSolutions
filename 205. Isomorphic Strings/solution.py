class Solution:
    def getListForSet(self,s):
        arr = []
        dict1 = {}
        for index , char in enumerate(s):
            if char not in dict1:
                dict1[char] = str(index)
            else:
                dict1[char]+=str(index)

        for key in dict1.keys():
            arr.append(dict1[key])

        return set(arr)


    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        set1=self.getListForSet(s)
        set2=self.getListForSet(t)
        return set1==set2



a=Solution()
print(a.isIsomorphic("aba","cba"))