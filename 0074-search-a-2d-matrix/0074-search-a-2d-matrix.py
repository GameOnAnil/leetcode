class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        group = 0
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or target == matrix[mid][-1]:
                return True
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                group = mid
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, len(matrix[group]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[group][mid] == target:
                return True
            elif target < matrix[group][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
