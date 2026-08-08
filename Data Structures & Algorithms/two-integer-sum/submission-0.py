class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        ans=[]
        for i in range(0,len(nums)):
            val = target-nums[i]
            if val in freq:
                ans.append(freq[val])
                ans.append(i)
                return ans
            else:
                freq[nums[i]]=i
        return ans

