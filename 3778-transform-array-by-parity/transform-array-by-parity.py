class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        #x, y = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
                #x+=1
            else:
                nums[i]= 1
                #y+=1
        #zeroes = [0 for i in range(x)]
        #ones = [1 for i in range(y)]
        #nums = zeroes + ones
        return sorted(nums) # return nums