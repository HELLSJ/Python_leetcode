# https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked
# https://cloud.tencent.com/developer/article/1649537


def rotate(self, matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]