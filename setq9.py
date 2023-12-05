nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_val = 12
print("Original list of numbers:")
print(nums)
print("Target value:", target_val)
nums = list(set(nums))
result = set()
    
   
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        complement = target_val - nums[i] - nums[j]
        if complement in nums[:i] + nums[j+1:]:
                result.add(tuple(sorted((nums[i], nums[j], complement))))
    
    
c=list(result)
print(c)