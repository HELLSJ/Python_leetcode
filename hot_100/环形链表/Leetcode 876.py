# Leetcode 876 链表的中间节点 https://leetcode.cn/problems/middle-of-the-linked-list/description/
# 设置快慢指针，快指针速度时慢指针两倍，快指针到终点的时候慢指针所在的位置刚好是中间位置
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow