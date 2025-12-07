# https://leetcode.cn/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-100-liked
# 先统计链表长度，判断是否还有 k 个节点可反转
# 使用 dummy 和 p0 锁定每一组的前驱节点
# 反转这一组的 k 个节点
# 反转后有三段链表：前段(pre)、反转段、后段(p0.next)
# 用个nxt存储p0下一个节点，然后通过 p0.next.next 和 p0.next 完成三段重新拼接，然后将 p0 移动到下一段起点(p0=next)，循环继续
# 不足 k 个的直接退出循环，不翻转
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(self, head, k):
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(next=head)
    p0 = dummy
    pre = None
    cur = p0.next
    while n >= k:
        n -= k
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        nxt = p0.next
        p0.next.next = cur
        p0.next = pre
        p0 = nxt

    return dummy.next