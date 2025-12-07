🎯 核心思路

我们将数组 按 k 大小分块，然后预处理两个数组：

prefixMax[i]：当前块里从左到 i 的最大值

suffixMax[i]：当前块里从 i 到该块右端的最大值

这样，在每个滑动窗口的最大值中：

如果窗口刚好对齐了一个完整的块（i % k == 0）：
→ 整块最大值就是 prefix 或 suffix 的值

如果窗口跨块：
→ 最大值 = 左块后缀最大（suffixMax[i]）     和    右块前缀最大（prefixMax[i+k−1]）的较大者。

最终我们可以在 O(1) 时间计算每个窗口最大值，总体复杂度 O(n)，与单调队列相同但实现更优美。

📌 prefixMax 和 suffixMax 的定义
prefixMax[i] 的转移：


📌 窗口最大值的求法

对于窗口 [i, i+k-1]：


✅ Python 实现（带注释）
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        # prefixMax[i]: 当前组中从左到 i 的最大值
        # suffixMax[i]: 当前组中从 i 到组尾的最大值
        prefixMax, suffixMax = [0] * n, [0] * n

        # 计算 prefixMax（从左向右）
        for i in range(n):
            if i % k == 0:
                # 每一组的第一个元素
                prefixMax[i] = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i - 1], nums[i])

        # 计算 suffixMax（从右向左）
        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                # 每组的最后一个元素
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i + 1], nums[i])

        # 每个窗口的最大值为对应 suffix 和 prefix 的最大值
        ans = [
            max(suffixMax[i], prefixMax[i + k - 1])
            for i in range(n - k + 1)
        ]
        return ans

