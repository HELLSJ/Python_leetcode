# https://leetcode.cn/problems/reverse-linked-list-ii/

def reverseBetween(self, head, left, right):
    dummy = ListNode(next=head)
    p0 = dummy

    for _ in range(left - 1):
        p0 = p0.next
    pre = None
    cur = p0.next
    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    p0.next.next = cur
    p0.next = pre

    return dummy.next