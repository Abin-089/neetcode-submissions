class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pair = []
        for i in range(len(numbers)):
            num = target - numbers[i]
            for j in range(len(numbers)):
                if num == numbers[j]:
                   pair.append(i+1)
                   pair.append(j+1)
                   return pair 
