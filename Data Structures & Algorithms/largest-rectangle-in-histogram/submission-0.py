class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Maxarea = 0
        stack = []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index,height = stack.pop()
                Maxarea = max(Maxarea,height*(i-index))
                start = index
            stack.append((start,h))
        for i,h in stack:
            Maxarea = max(Maxarea,h*(len(heights)-i))
        return Maxarea