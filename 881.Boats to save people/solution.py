
def numRescueBoats( people, limit):
    """
    To solve this ,we will use the two pointers greedy approach.
    We will sort the array and then see if the sum of first and last element is less than
    or equal to the limit .if not we conclude that the last element is a lone traveller in
    boat.Else we have a pair so we increment the first and last pointer and carry on until
    both the pointers match.

    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    total_boat=0
    people=sorted(people)
    start_pointer=0
    end_pointer=len(people)-1
    while(start_pointer<=end_pointer):
        if people[start_pointer]+people[end_pointer]<=limit:
            start_pointer+=1
        end_pointer-=1
        total_boat+=1
    return total_boat
print(numRescueBoats([1,2,10,3,4,2],10))