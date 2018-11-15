class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator==0:
            return float('NaN')
        if numerator==0:
            return "0"


        pre_value=""
        post_value=""
        if numerator < 0 and denominator >0:
            pre_value=pre_value+"-"
            numerator=numerator*-1
        elif denominator <0 and numerator >0:
            pre_value=pre_value+"-"
            denominator=denominator*-1

        string_div_result= str(int(numerator/denominator))
        pre_value+=string_div_result.split(".")[0]
        numerator=numerator%denominator
        list_of_three=""
        first_time=False
        if numerator==0:
            return pre_value
        nums_dict={}
        while  numerator != 0:
            quest, new_num = self.getValue(numerator, denominator)
            if numerator in nums_dict:
                if nums_dict[numerator][0]+1 >= 2:
                    #post_value = post_value.replace(nums_dict[numerator][1], "", 1)
                    post_value = post_value.replace(nums_dict[numerator][1], "(" + nums_dict[numerator][1])
                    count=post_value.count("(" + nums_dict[numerator][1])
                    if count>1:
                        post_value=post_value.replace("(" + nums_dict[numerator][1],"", count-1)
                    post_value += ")"
                    break
                nums_dict[numerator] = (nums_dict[numerator][0] + 1, quest)
            else:
                nums_dict[numerator]=(1,quest)
            post_value+=str(quest)

            numerator=new_num

        return pre_value+"."+post_value

    def rreplace(self,s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

    def getValue(self,num,denom):
        quest=""
        i=0
        while num <= denom:
            i+=1
            num=num*10
            if i>1:
                quest+="0"
        quest+=str(int(num/denom))
        num=num%denom
        return quest,num


a=Solution()
print(a.fractionToDecimal(1,214748364))

