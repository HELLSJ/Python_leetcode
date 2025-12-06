class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# 方法1：哈希表
# 遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过。
#
# 使用哈希表来存储所有已经访问过的节点。每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。重复这一过程，直到我们遍历完整个链表即可。

def hasCycle1(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False


# 方法2：龟兔思路
# 本方法需要读者对「Floyd 判圈算法」（又称龟兔赛跑算法）有所了解。
#
# 假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。当「乌龟」和「兔子」从链表上的同一个节点开始移动时，如果该链表中没有环，那么「兔子」将一直处于「乌龟」的前方；如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，即套了「乌龟」若干圈。
#
# 定义两个指针，一快一慢。慢指针每次只移动一步，而快指针每次移动两步。初始时，慢指针在位置 head，而快指针在位置 head.next。
# 这样一来，如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。

def hasCycle2(self, head):
    if not head or not head.next:
         return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

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

# Leetcode 21 合并两个链表 https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-100-liked

# 每次从两个链表的当前节点中选取更小的，把它作为结果链表的下一节点，然后递归处理剩下的节点
def mergeTwoLists(self, list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val<list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list2.next, list1)
        return list2

# Leetcode 02 两数之和 https://leetcode.cn/problems/add-two-numbers/?envType=study-plan-v2&envId=top-100-liked

# 1. 准备一个 虚拟头节点 dummy，再用指针 cur 指向它，用来构造结果链表。
#
# 2. 准备一个整型变量 carry，初始为 0。
#
# 3. 遍历两个链表，条件可以写为：while l1 or l2 or carry：
# 取出当前位的值：
# x = l1.val if l1 else 0
# y = l2.val if l2 else 0
# 计算这一位的总和：total = x + y + carry
# 得到当前位数字：digit = total % 10
# 更新进位：carry = total // 10
# 创建新节点 digit 挂到 cur.next，然后 cur = cur.next
# l1 和 l2 往后移动（如果存在的话）
# 4. 循环结束后，dummy.next 就是结果链表的头结点。
def addTwoNumbers(self, l1, l2):
    num_0 = 0  # 当前位的和（个位）
    num_10 = 0  # 进位（carry）
    cur = dum = ListNode()  # 虚拟头节点（dummy node）

    while l1 or l2:
        # 如果某个链表走完了，就用值为 0 的新节点代替（处理链表不等长的问题）
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)

        # 计算当前位的和与进位
        total = l1.val + l2.val + num_10
        num_0 = total % 10  # 当前位结果（个位数是多少）
        num_10 = total // 10  # 新的进位（十位）

        # 构建结果链表
        cur.next = ListNode(val=num_0)
        cur = cur.next

        # 移动指针
        l1 = l1.next
        l2 = l2.next

    # 处理最后的进位（如 999 + 1 = 1000）
    if num_10 != 0:
        cur.next = ListNode(val=num_10)  # cur是虚拟头节点，所以cur.next直接当作是头节点了

    return dum.next  # 返回真实头节点

# Leetcode 19.删除链表的倒数第 N 个结点
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-100-liked

# 定义两个指针，一个left一个right
# 再创建一个dummy哨兵节点，next指向头节点，因为倒数第n个节点就是头节点，删除了就没有头节点了
# 假设链表长度为m, 要删除倒数第n个节点就是第m-n+1个节点，先让right走n步，然后再让left和right同时走，right走到结尾需要m-n步，left也一样走m-n步
# 这样当right走到倒数第一个节点时，left刚好在要删除的倒数第n个节点的左边，这个时候left.next = left.next.next就能把要删除的节点删掉了
# 最后再返回dummy.next（头节点）
def removeNthFromEnd(self, head, n):

    dummy = ListNode(next=head)
    right = dummy
    for i in range(n):
        right = right.next
    left = dummy
    while right.next:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next

# 24.两两交换链表中的节点 https://leetcode.cn/problems/swap-nodes-in-pairs/submissions/683066739/?envType=study-plan-v2&envId=top-100-liked
# 创建哨兵节点 dummy，表示节点 0。
# 下面用 node0 表示 0，node1 表示 1，依此类推。
# 1.把 node0 指向 node2.
# 2.把 node2 指向 node1。3.把 node1 指向 node3.
# 4. 更新 node0为 node1,更新 node1为 node3。
# 5.如果 node1 和 node1.next 都不为空就回到第一步，执行下一轮交换。
# 6. 最后返回 dummy.next，作为新链表的头节点。

def swapPairs(self, head):
    node0 = dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
    node1 = head
    while node1 and node1.next:  # 至少有两个节点
        node2 = node1.next
        node3 = node2.next

        node0.next = node2  # 0 -> 2
        node2.next = node1  # 2 -> 1
        node1.next = node3  # 1 -> 3

        node0 = node1  # 下一轮交换，0 是 1
        node1 = node3  # 下一轮交换，1 是 3
    return dummy.next  # 返回新链表的头节点

# Leetcode 138.随机链表的复制  https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked
# 如果没有 random 指针，只需在遍历链表的同时，依次复制每个节点（创建新节点并复制 val），添加在新链表的末尾。
# 有 random 指针，问题就变得复杂了，我们需要知道 random 指向的那个节点，在新链表中是哪个节点。
# 所以必须记录原链表节点到新链表节点的映射（map）。这样可以通过原链表 random 指向的节点，知道新链表的 random 应该指向哪个节点。
# 可以把新链表和旧链表「混在一起」。
#
# 例如链表 1→2→3，依次复制每个节点（创建新节点并复制 val 和 next），把新节点直接插到原节点的后面，形成一个交错链表：
# 1→1′→2→2′→3→3′
# 如此一来，原链表节点的下一个节点，就是其对应的新链表节点了！
# 然后遍历这个交错链表，假如节点 1 的 random 指向节点 3，那么就把节点 1′的 random 指向节点 3 的下一个节点 3′，这样就完成了对 random 指针的复制。
# 最后，从交错链表中分离出 1′→2′→3′，即为深拷贝后的链表

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(self, head):
    if head is None:
        return None

    # 复制每个节点，把新节点直接插到原节点的后面
    # A->B->C 变成 A->A'->B->B'->C->C'
    cur = head
    while cur:
        cur.next = Node(cur.val, cur.next)
        cur = cur.next.next

    # 遍历交错链表中的原链表节点
    cur = head
    while cur:
        if cur.random:
            # 要复制的 random 是 cur.random 的下一个节点
            cur.next.random = cur.random.next
        cur = cur.next.next

    # 把交错链表分离成两个链表
    new_head = head.next # A'(新链表的头节点)
    cur = head
    while cur.next.next: # 每次都要遍历下一个节点（原链表.next）还有下下个节点是否存在（新链表.next）
        copy = cur.next # 新链表 copy = A.next = A'
        cur.next = copy.next  # 恢复原节点的 next A.next = A'.next = B
        copy.next = copy.next.next  # 设置新节点的 next A'.next = B.next = B'
        cur = cur.next # 遍历下一个节点
    cur.next = None  # 恢复原节点的 next
    return new_head