class NumMatrix(object):
    # caching smarter
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return
        height, width = len(matrix), len(matrix[0])
        self.dp = [[0]* (width + 1) for i in range(height + 1)]
        for i in range(height):
            for j in range(width):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + \
                                        self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
               self.dp[row2 + 1][col1] + self.dp[row1][col1]
