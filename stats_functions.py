import math

def mean(nums):
    if len(nums)==0:
        return None #handles the empty list 
    
    total=0
    for num in nums:
        total+=num
    
    return total/len(nums)   


def median(nums):
    if len(nums) == 0:
        return None 

    sortedNums = sorted(nums)  # returns a new sorted list
    n = len(sortedNums)

    if n % 2 == 1:
        return sortedNums[n // 2]
    else:
        mid1 = sortedNums[n // 2 - 1]
        mid2 = sortedNums[n // 2]
        return (mid1 + mid2) / 2


def mode(nums):
    if len(nums) == 0:
        return None 
    
    freq=dict()

     #buidling frequency table 
    for i in nums: 
        if i not in freq:
            freq[i]=1
        else: 
          freq[i]+=1
      #finding the actual mode:
    freq_max=0
    mod_val=None
    
    for num in freq:
        if freq[num]>freq_max:
            freq_max=freq[num]
            mod_val=num
    return mod_val              

 #function to find minimum in a list    
def minimum(nums):
    if len(nums)==0:
        return None
    min_num=nums[0]
    for i in nums: 
        if i<min_num:
            min_num=i
    return min_num        

 #function to find maximum in a list  
def maximum(nums):
    if len(nums)==0:
        return None
    max_num=nums[0]
    for i in nums: 
        if i>max_num:
            max_num=i
    return max_num  

#function to find range
def data_range(nums):
    if len(nums)==0:
        return None
    return max(nums)-min(nums)  

#function to find the variance
    
def variance(nums):
    if len(nums)==0:
        return None
    mean_val=sum(nums)/len(nums)

    squared_diff=[(x-mean_val)**2 for x in nums]
    total=sum(squared_diff)
    var= total/len(nums)
    return var

#function to find standard deviation

def std_dev(nums):
    var=variance(nums)
    if var is None:
        return None
    return math.sqrt(var)