class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1

        while l <= r:
            row = int((r + l) / 2)
            if matrix[row][0] <= target and target <= matrix[row][cols - 1]:
                l = 0
                r = cols - 1
                while l <= r:
                    m = int((r + l) / 2)
                    if matrix[row][m] == target:
                        return True
                    elif target < matrix[row][m]:
                        r = m - 1
                    else:
                        l = m + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                l = row + 1
            
        return False