# Leetcode 160 相交链表 https://leetcode.cn/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked
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

# Leetcode 206 反转链表 https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

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

# Leetcode 234 回文列表 https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked
# 复制链表值到数组列表中。
# 使用双指针法判断是否为回文。
# 第一步，我们需要遍历链表将值复制到数组列表中。我们用 currentNode 指向当前节点。每次迭代向数组添加 currentNode.val，并更新 currentNode = currentNode.next，当 currentNode = null 时停止循环。
#
# 执行第二步的最佳方法取决于你使用的语言。在 Python 中，很容易构造一个列表的反向副本，也很容易比较两个列表。而在其他语言中，就没有那么简单。因此最好使用双指针法来检查是否为回文。我们在起点放置一个指针，在结尾放置一个指针，每一次迭代判断两个指针指向的元素是否相同，若不同，返回 false；相同则将两个指针向内移动，并继续判断，直到两个指针相遇。
#
# 在编码的过程中，注意我们比较的是节点值的大小，而不是节点本身。正确的比较方式是：node_1.val == node_2.val，而 node_1 == node_2 是错误的。

def isPalindrome(self, head):
    vals=[]
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals==vals[::-1]

# Leetcode 141 https://leetcode.cn/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-100-liked


# 遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。
#
# 使用哈希表来存储所有已经访问过的节点。每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。重复这一过程，直到我们遍历完整个链表即可。

def hasCycle(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

