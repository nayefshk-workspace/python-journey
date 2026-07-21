# Problem 1:
 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
 
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

#input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target: "))

#function
def Sum(nums, target):
    
    total_elements = len(nums) 
#looops  
    for i in range(0, total_elements):

        for j in range(i + 1, total_elements): 

            first_number = nums[i]
            second_number = nums[j]

            if first_number + second_number == target:
                print(i,j)
#output
# print(Sum(nums, target))     
Sum(nums, target)
