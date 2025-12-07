# Leetcode 206 反转链表 https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
# 简单做法
def reverseList(self, head):
    cur, pre = head, None
    while cur:
        tmp = cur.next  # 暂存后继节点 cur.next
        cur.next = pre  # 修改 next 引用指向
        pre = cur  # pre 暂存 cur
        cur = tmp  # cur 访问下一节点
    return pre
# 递归做法
# def reverseList(self, head):
#     def recur(cur, pre):
#         if not cur:
#             return pre     # 终止条件
#         res = recur(cur.next, cur) # 递归后继节点
#         cur.next = pre             # 修改节点引用指向
#         return res                 # 返回反转链表的头节点

#     return recur(head, None)       # 调用递归并返回