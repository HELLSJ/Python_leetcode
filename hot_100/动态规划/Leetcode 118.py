# https://leetcode.cn/problems/pascals-triangle/submissions/683295392/?envType=study-plan-v2&envId=top-100-liked
# 把杨辉三角的每一排左对齐：
#
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]

# 设要计算的二维数组是 c，计算方法如下：

# 每一排的第一个数和最后一个数都是 1，即 c[i][0]=c[i][i]=1。
# 其余数字，等于左上方的数，加上正上方的数，即 c[i][j]=c[i−1][j−1]+c[i−1][j]。例如 4=1+3,6=3+3 等。

# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def generate(self, numRows):
    c = [[1] * (i + 1) for i in range(numRows)]
    for i in range(2, numRows):
        for j in range(1, i):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c