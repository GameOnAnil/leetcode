# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Sets to track unique children and parents
        children = set()
        parents = set()
        relations = {}

        # Build graph from parent to child, and add nodes to sets
        for d in descriptions:
            parent, child, isLeft = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in relations:
                relations[parent] = []
            relations[parent].append((child, isLeft))

        # Find the root node by checking which node is
        # in parents but not in children
        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        root = TreeNode(next(iter(parents)))
        q = deque([root])

        while q:
            curr = q.popleft()
            for c, isLeft in relations.get(curr.val,[]):
                child = TreeNode(c)
                q.append(child)
                if isLeft == 1:
                    curr.left = child
                else:
                    curr.right = child

        return root
