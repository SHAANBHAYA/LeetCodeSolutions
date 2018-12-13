class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dict_of_sol={}
        dict_of_sum_of_two_elements={}
        length_of_nums=len(nums)
        for i in range(0,length_of_nums-1):
            for j in range(i+1,length_of_nums):
                sum=nums[i]+nums[j]
                if sum in dict_of_sum_of_two_elements :
                    dict_of_sum_of_two_elements[sum].append([i,j])
                else:
                    dict_of_sum_of_two_elements[sum]=[[i,j]]

        for i in range(0, length_of_nums - 1):
            for j in range(i + 1, length_of_nums):
                sum=nums[i]+nums[j]
                if (target-sum) in dict_of_sum_of_two_elements:
                    for e in dict_of_sum_of_two_elements[target-sum]:
                        if e[0]!=i and e[0] != j and e[1]!=i and e[1]!=j:
                            sol_arr=[nums[e[0]],nums[e[1]],nums[i],nums[j]]
                            sorted_arr=sorted(sol_arr)
                            dict_of_sol[(sorted_arr[0],sorted_arr[1],sorted_arr[2],sorted_arr[3])]=sorted_arr
        return list(dict_of_sol.values())





a=Solution()
print(a.fourSum([1, 1,1,1,1,1,1,1,1,1],4))