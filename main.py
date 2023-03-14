"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 
"""

#creating a function that takes in the target value and an array of integers
def twoSum(nums, target):

  #creating a dictionary to store all the integers that have already been viewed
  viewed = {}

  #enumerate (iterate) over the given array
  for i, x in enumerate(nums):

    #calculate the difference between target and current integer
    difference = target - x

    #check to see if the current difference has been seen before
    if difference in viewed: #"if difference value is in viewed dictionary"

      # return the index of current number and compliment
      return [viewed[difference], i]

    # if it has not been seen before then we add it to the viewed dictionary
    viewed[x] = i

  # if theres no solution, then just return empty list
  return []

nums = [2, 7, 11, 15]
target = 9

indices = twoSum(nums, target)
print(indices)



