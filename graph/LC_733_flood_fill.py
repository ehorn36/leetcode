"""
https://leetcode.com/problems/flood-fill/

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value
of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image
starting from the pixel image[sr][sc].

To perform a flood fill:
    1) Begin with the starting pixel and change its color to color.

    2) Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
    either horizontally or vertically) and shares the same color as the starting pixel.

    3) Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color
    if it matches the original color of the starting pixel.

    4) The process stops when there are no more adjacent pixels of the original color to update.
    Return the modified image after performing the flood fill.
"""


class Solution(object):
    def floodFill(self, image, sr, sc, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        # Determine array lengths
        length_r = len(image)
        length_c = len(image[0])

        # Save starting color to know which other pixels should be processed
        color = image[sr][sc]

        # If current color matches new color
        if color == new_color:
            return image

        # Define DFS function
        def dfs(r, c):
            """
            If the pixel contains the target color, the color is updated and DFS continues on valid adjacent pixels.
            Only valid pixels connected to the starting pixel will be updated.
            """

            # If pixel == color
            if image[r][c] == color:

                # Update to new color
                image[r][c] = new_color

                # Call DFS on adjacent pixels
                # If valid top
                if r >= 1:
                    dfs(r - 1, c)

                # If valid bottom
                if r + 1 < length_r:
                    dfs(r + 1, c)

                # If valid left
                if c >= 1:
                    dfs(r, c - 1)

                # If valid right
                if c + 1 < length_c:
                    dfs(r, c + 1)

        # Call DFS on starting pixel
        dfs(sr, sc)
        return image



# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# sr = 1
# sc = 1
# color = 2

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0

test = Solution()
print(test.floodFill(image, sr, sc, color))
