class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    return helper(root, float("-inf"), float("inf"))

def helper(root, minValue, maxValue):
    if root is None:
        return True
    print(root.val)
    if root.val <= minValue or root.val >= maxValue:
        return False
    validLeft = helper(root.left, minValue, root.val)
    validRight = helper(root.right, root.val, maxValue)
    return validLeft and validRight


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

if isValidBST(root):
    print("Is BST")
else:
    print("Not a BST")