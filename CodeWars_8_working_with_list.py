def pipe_fix(nums):
    newLst =[]
    for i in range(nums[0],nums[len(nums)-1]+1):
         newLst.append(i)
    return newLst

print(pipe_fix([6,9]))