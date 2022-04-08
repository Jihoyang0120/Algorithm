def search(nums, target):
    i = 0
    while(nums[i] != target):
        i += 1
        if (i == len(nums)):
            return -1
    return(i)


search([-1, 0, 3, 5, 9, 12], 2)
