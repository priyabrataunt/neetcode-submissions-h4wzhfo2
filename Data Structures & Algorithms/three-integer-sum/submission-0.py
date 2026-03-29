class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        res = []
        nums.sort() # nums = [-1,-1,0,1,2,4]

        for i, a in enumerate(nums): # 1st - i = 0, a = -1
        # 2nd - i = 1, a = -1
            if a > 0: # False
                break
            
            if i > 0 and a == nums[i - 1]: # i = 0 (False)
            # 2nd - i > 0 (True) and a = nums[1-1] = nums[0] = -1
                continue

            l, r = i + 1, len(nums) - 1 # l= 2, r = 4
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res    