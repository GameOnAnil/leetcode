class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colL, colR = 0, len(matrix) - 1
        colIndex = 0
        while colL <= colR:
            mid = (colL + colR) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                colIndex = mid
                break
            elif target < matrix[mid][0]:
                colR = mid - 1
            else:
                colL = mid + 1
        rowL, rowR = 0, len(matrix[colIndex]) - 1
        while rowL <= rowR:
            mid = (rowL + rowR) // 2
            if target == matrix[colIndex][mid]:
                return True
            elif target < matrix[colIndex][mid]:
                rowR = mid - 1
            else:
                rowL = mid + 1
        return False
