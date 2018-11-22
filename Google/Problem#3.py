"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
class Codec:

    def serialize(self, root):
        def serializeHelper(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = serializeHelper(root.left, string)
                string = serializeHelper(root.right, string)
            return string
        return serializeHelper(root,"")

    def deserialize(self, data):
        def deserializeHeper(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = deserializeHeper(l)
            root.right = deserializeHeper(l)
            return root
        return deserializeHeper(data.split(','))
