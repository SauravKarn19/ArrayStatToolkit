# importing all functions
from stats_functions import mean, median, mode, minimum, maximum, data_range, variance, std_dev

data=input("enter the numbers:")
data=data.replace(","," ")
data_list=list(data.split())
nums=[float(x) for x in data_list]
print(nums)

if not nums:
    print("No numbers entered. exiting the program")
    exit()

print("\n--- Statistics Toolkit Results ---")
print(f"Mean: {mean(nums)}")
print(f"Median: {median(nums)}")
print(f"Mode: {mode(nums)}")
print(f"Minimum: {minimum(nums)}")
print(f"Maximum: {maximum(nums)}")
print(f"Range: {data_range(nums)}")
print(f"Variance: {variance(nums)}")
print(f"Standard Deviation: {std_dev(nums)}")

print("-------------------------------")