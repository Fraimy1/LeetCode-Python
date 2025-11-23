class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        k = 0
        length = len(nums)
        while i < length:
            
            if nums[i] != val:
                # print(i, nums)
                nums.insert(k, nums.pop(i))
                # print(i, nums, '\n')
                k += 1
            
            i += 1
        return k
        
# Solution.removeElement(Solution, [0,1,2,2,3,0,4,2], 2)