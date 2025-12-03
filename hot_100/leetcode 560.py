# https://leetcode.cn/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
from collections import defaultdict


def subarraySum(self, nums, k):
    ans = 0  # 用于记录满足条件的子数组个数
    s = 0  # 当前的前缀和（从 nums[0] 到当前元素的累加和）
    cnt = defaultdict(int)  # 哈希表：记录每个前缀和出现的次数

    for x in nums:
        # 关键顺序：先记录当前前缀和 s 的出现次数
        cnt[s] += 1

        # 然后把当前元素 x 加入前缀和
        s += x

        # 检查是否存在某个之前的前缀和 s_prev，使得 s - s_prev == k
        # 即：s_prev = s - k
        ans += cnt[s - k]

    return ans