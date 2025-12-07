# https://leetcode.cn/problems/reorder-list/description/
# 第一步：找中点
# 为了重排成 前一个、最后一个、第二个、倒数第二个……，我们自然会把链表想象成两半：
# 前半段：L0, L1, L2, ...
# 后半段：..., Lk, ..., Ln-1, Ln
# 如果我们能：拿着前半段，从前往后走：L0, L1, L2, ...
# 拿着“后半段的倒序”：Ln, Ln-1, Ln-2, ...
# 那么交替拼接就很自然了。

# 第二步：反转链表
# 我们想要的顺序是：
# 从前半段：L0, L1, L2, ...
# 从后半段：Ln, Ln-1, Ln-2, ...

# 第三步： 交替连接：
# 每次从前半拿一个、从后半（倒序）拿一个
# 用指针重新连接成 前 → 后 → 下一前
# 不断推进，完成整条链表的重排
class Solution(object):
    # Leetcode 876 链表的中间节点
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Leetcode 206 反转链表
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 暂存后继节点 cur.next
            cur.next = pre  # 修改 next 引用指向
            pre = cur  # pre 暂存 cur
            cur = tmp  # cur 访问下一节点
        return pre

    def reorderList(self, head):
        mid = self.middleNode(head)
        head2= self.reverseList(mid)
        while head2.next:
            # 后半段通常 不比前半段长（长度是 ⌊n/2⌋ 或 ⌈n/2⌉）
            # 每次循环我们会插入一个来自后半的节点（head2）
            # 当 head2.next 为 None 时，说明 head2 是最后一个“后半节点”了，再插下去就会超出需要的模式，容易乱指或者成环
            # 用 head2.next 作为条件，可以保证我们不把最后一个后半节点再往前插一次
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head=nxt
            head2=nxt2