class Solution:
    def maxArea(height):
        left, right, y = 0, len(height) - 1, 0
        max_water = 0
        while left < right:
            x = (right - left - 2)

            if height[left] <= height[right]:
                y = height[left]
                left += 1
            else:
                y = height[right]
                right -= 1

            max_water = max(x * y, max_water)

        return max_water

    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea(range(10000)))