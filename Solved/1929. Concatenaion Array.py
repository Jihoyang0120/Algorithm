class Solution(object):
    def getConcatenation(self, nums):
        num_list = []
        for num in nums:
            num_list.append(num)
        return nums + num_list
