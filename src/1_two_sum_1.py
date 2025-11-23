# O(n^2)
# class Solution(object):
#     def twoSum(self, nums, target):
#         summ = 0

#         for i, num1 in enumerate(nums):
#             search_value = target - num1
#             for j, num2 in enumerate(nums[i+1:], start=i+1):
#                 # print(num1, num2, search_value)
#                 if num2 == search_value:
#                     return [i, j]


# O(n)
class Solution(object):
    def twoSum(self, nums, target):
        summ = 0
        hashmap = {}

        for i, num1 in enumerate(nums):
            expected = target - num1
            j = hashmap.get(expected)
            # print(expected, hashmap, j)
            if j is not None:
                return [i, j]
            else:
                hashmap[num1] = i

