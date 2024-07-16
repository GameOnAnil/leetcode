# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lcm = self.findLCM(root,startValue,destValue)
        leftPath = self.findPath(lcm,[],startValue)
        rightPath = self.findPath(lcm,[],destValue)
        res = []
        res.extend("U"*len(leftPath))
        res.extend(rightPath)
        return "".join(res)

    def findPath(self,node,path,dest):
        if not node:
            return None
        if node.val == dest:
            return path
        path.append("L")
        left = self.findPath(node.left,path,dest)
        if left:
            return left
        path.pop()
        path.append("R")
        right =  self.findPath(node.right,path,dest)
        if right:
            return right
        path.pop()



    def findLCM(self,node:Optional[TreeNode],startValue:int,destValue:int):
        if not node:
            return None
        if startValue == node.val or destValue == node.val:
            return node
        left = self.findLCM(node.left,startValue,destValue)
        right = self.findLCM(node.right,startValue,destValue)
        if not left:
            return right
        if not right:
            return left
        return node
        