# Leetcode 160 https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked
# 使用双指针的方法，可以将空间复杂度降至 O(1)。
#
# 只有当链表 headA 和 headB 都不为空时，两个链表才可能相交。因此首先判断链表 headA 和 headB 是否为空，如果其中至少有一个链表为空，则两个链表一定不相交，返回 null。
#
# 当链表 headA 和 headB 都不为空时，创建两个指针 pA 和 pB，初始时分别指向两个链表的头节点 headA 和 headB，然后将两个指针依次遍历两个链表的每个节点。具体做法如下：
#
# 每步操作需要同时更新指针 pA 和 pB。
#
# 如果指针 pA 不为空，则将指针 pA 移到下一个节点；如果指针 pB 不为空，则将指针 pB 移到下一个节点。
#
# 遇到各自链表终点时：
#
# pA 走到 A 的尾部，再跳到 B 的头；
#
# pB 走到 B 的尾部，再跳到 A 的头。

# 最终 两者会在相交节点相遇

def getIntersectionNode(self, headA, headB):
    if not headA or not headB:
        return None

    pA, pB = headA, headB
    while pA != pB:
        if pA:
            pA = pA.next
        else:
            pA = headB
        pB = pB.next if pB else headA
    return pA

# Leetcode 206 https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

def reverseList(self, head):
    cur, pre = head, None
    while cur:
        tmp = cur.next  # 暂存后继节点 cur.next
        cur.next = pre  # 修改 next 引用指向
        pre = cur  # pre 暂存 cur
        cur = tmp  # cur 访问下一节点
    return pre

# def reverseList(self, head):
#     def recur(cur, pre):
#         if not cur:
#             return pre     # 终止条件
#         res = recur(cur.next, cur) # 递归后继节点
#         cur.next = pre             # 修改节点引用指向
#         return res                 # 返回反转链表的头节点

#     return recur(head, None)       # 调用递归并返回