class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1

        while l <= r:
            mRow = l + (r - l) // 2
            if matrix[mRow][0] <= target and target <= matrix[mRow][cols - 1]:
                # conduct binary search in row
                l = 0
                r = cols - 1

                while l <= r:
                    m = l + (r - l) // 2
                    if matrix[mRow][m] == target:
                        return True
                    elif matrix[mRow][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
            elif matrix[mRow][0] > target:
                r = mRow - 1
            else:
                l = mRow + 1
        
        return False