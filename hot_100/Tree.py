# leetcode 94 https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked
def inorderTraversal(self, root):
    """
    递归实现中序遍历
    """
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)  # 先遍历左子树
        res.append(node.val)  # 再访问根节点
        dfs(node.right)  # 最后遍历右子树

    dfs(root)
    return res

# leetcode 104 https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked

def maxDepth(self, root):
    if root is None:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

# leetcode 226 https://leetcode.cn/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-100-liked

def invertTree(self, root):
    if not root:
        return
    else:
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

# leetcode 101 https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked

def isSymmetric(self, root):
    """
    判断二叉树是否是轴对称的（镜像对称）
    思路：将问题转化为——比较左子树和右子树是否互为镜像
    通过递归比较两个子树：
        - 它们的根节点值相等
        - 左子树的左孩子 与 右子树的右孩子 对称
        - 左子树的右孩子 与 右子树的左孩子 对称
    """

    def check(p, q):
        """
        递归函数：判断两棵树 p 和 q 是否互为镜像
        """
        # 情况1：两个节点都为空 → 对称
        if not p and not q:
            return True

        # 情况2：其中一个为空，另一个不为空 → 不对称
        # 或者两个都不空但值不相等 → 不对称
        if not p or not q or p.val != q.val:
            return False

        # 情况3：当前节点值相等，继续递归检查：
        #   p 的左子树 应该和 q 的右子树 对称
        #   p 的右子树 应该和 q 的左子树 对称
        return check(p.left, q.right) and check(p.right, q.left)

    # 从根节点开始，把自己和自己做镜像比较
    # 如果 root 为 None，check(None, None) 会返回 True（空树是对称的）
    return check(root, root)