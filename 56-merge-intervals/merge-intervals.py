# class Solution:
#     def merge(self, nums: List[List[int]]) -> List[List[int]]:
#         nums = sorted(nums, key = lambda x: (x[0]))
#         i = 0
#         n = len(nums)-1
#         while i<n:
#             if nums[i+1][0]<=nums[i][1]:
#                 if nums[i][1]<=nums[i+1][1]:
#                     a = nums.pop(i)
#                     b = nums.pop(i)
#                     nums.insert(i, [a[0],b[1]])
#                     n = n-1
#                 else:
#                     a = nums.pop(i)
#                     nums.pop(i)
#                     nums.insert(i, [a[0],a[1]])
#                     n = n-1
#             else:
#                 i+=1
#         return nums
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda val : val[0])

        lst = intervals[0]

        final_lst = []
        
        for item in intervals:
            if item[0] <= lst[1]:
                lst[1] = max(lst[1],item[1])
            else:
                final_lst.append(lst)
                lst = item
        final_lst.append(lst)
        
        return final_lst





        