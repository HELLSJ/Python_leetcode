# Leetcode 142 环形链表Ⅱ https://leetcode.cn/problems/linked-list-cycle-ii/description/?envType=study-plan-v2&envId=top-100-liked

# 方法1：依旧哈希表
def detectCycle1(self, head):
    seen = set()
    while head:
        if head in seen:
            return head
        seen.add(head)
        head = head.next
    return

# 方法2：快慢指针

# 使用两个指针，fast 与 slow。它们起始都位于链表的头部。随后，slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置。
# 如果链表中存在环，则 fast 指针最终将再次与 slow 指针在环中相遇。
# 设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇。此时，fast 指针已经走完了环的 n 圈，因此它走过的总距离为 a+n(b+c)+b=a+(n+1)b+nc。
# 根据题意，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍。因此，我们有
# a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)
# 有了 a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n−1 圈的环长，恰好等于从链表头部到入环点的距离。
# 这里的(n-1)(b+c)是slow在环里面绕圈
# 因此，当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。

def detectCycle2(self, head):
    if not head:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        else:
            return None
    ptr = head
    while ptr != slow:
        ptr = ptr.next
        slow = slow.next
    return ptr