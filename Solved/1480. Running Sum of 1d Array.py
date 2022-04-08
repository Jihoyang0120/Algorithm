class Solution(object):
    def runningSum(self, nums):
        num_list = []
        sum = 0
        for num in nums:
            sum += num
            num_list.append(sum)
        return(num_list)