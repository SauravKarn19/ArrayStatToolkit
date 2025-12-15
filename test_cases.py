def minimum(nums):
    min=nums[0]
    for i in nums: 
        if i<min:
            min=nums[i]
    return min        


nums=[4,3,2,1]
print(minimum(nums))