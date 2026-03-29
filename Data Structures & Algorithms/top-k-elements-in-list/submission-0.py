class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count -> Bucket -> Reverse Walk -> Found K
        #nums = [1,2,2,3,3,3], k = 2
        count = {} 
        for i in nums:
            count[i] = count.get(i, 0) + 1 #({1:1}{2:2}{3:3})
        
        bucket = [[] for _ in range(len(nums)+ 1)]

        for num, cnt in count.items():
            bucket[cnt].append(num) # [][1][2][3][][][]
        
        res = []
        for i in range(len(bucket) -1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if(len(res) == k):
                    return res