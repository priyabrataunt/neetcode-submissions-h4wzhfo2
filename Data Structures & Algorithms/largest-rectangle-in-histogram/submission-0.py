class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for current_index, h in enumerate(heights):
            start = current_index
            while stack and stack[-1][1] > h:
                start_index, height = stack.pop()
                area = height * (current_index - start_index)
                max_area = max(max_area, area)
                start = start_index
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)
        return max_area
