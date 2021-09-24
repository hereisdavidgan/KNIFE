### 144. 二叉树的前序遍历

"""
```
python
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res 
```
"""
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack,res = [root],[]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                if  node.right:
                    stack.append(node.right)
                if  node.left:
                    stack.append(node.left)
        return res