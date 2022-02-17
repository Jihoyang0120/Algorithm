def runningSum(nums):
    num_list = []
    sum = 0
    for num in nums:
        sum += num
        num_list.append(sum)
    print(num_list)


runningSum([3, 1, 2, 10, 1])
