"""
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two cells sharing a common edge is 1.

    Example 1:
        Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
        Output: [[0,0,0],[0,1,0],[0,0,0]]

    Example 2:
        Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
        Output: [[0,0,0],[0,1,0],[1,2,1]]

"""


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        height = len(mat)
        width = len(mat[0])
        queue = []
        head = 0  # Tracks the first index of the queue

        # Populate return matrix
        for i in range(height):
            for j in range(width):

                # If 0, then add to queue
                if mat[i][j] == 0:
                    queue.append((i, j))

                # Otherwise, add # symbol
                else:
                    mat[i][j] = "#"

        # Down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while head < len(queue):

            # Retrieve cell coordinates at front of queue, and move head
            row, col = queue[head]  # Tuple
            head += 1

            # Look at 4 neighbors of cell
            for row_change, col_change in directions:
                new_row = row + row_change
                new_column = col + col_change

                # If cell is inbounds and contains a "#"
                if 0 <= new_row < height and 0 <= new_column < width and mat[new_row][new_column] == "#":
                    # Update cell value to be (original queued cell value + 1)
                    mat[new_row][new_column] = mat[row][col] + 1

                    # Add new cell coordinates to queue
                    queue.append((new_row, new_column))

        return mat


mat1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]  # [[0,0,0],[0,1,0],[1,2,1]]

test = Solution()
print(test.updateMatrix(mat1))
