# leetcode 239 https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked
import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)

        # 构建一个最大堆，但 Python 只有最小堆，所以存 (-值, 下标)
        # 先把前 k 个元素放进堆中
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)   # 建堆 O(k)

        # 堆顶元素就是当前窗口的最大值（注意要取负号）
        ans = [-q[0][0]]

        # 从第 k 个元素开始往右滑动窗口
        for i in range(k, n):
            # 将新进入窗口的元素压入堆
            heapq.heappush(q, (-nums[i], i))

            # 堆顶的元素可能已经滑出窗口范围，需要不断弹出
            # 只保留下标在 [i-k+1, i] 这个窗口中的元素
            while q[0][1] <= i - k:
                heapq.heappop(q)

            # 此时堆顶一定是窗口内最大的值
            ans.append(-q[0][0])

        return ans