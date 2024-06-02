class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def isEmpty(self):
        return self.root is None
    def clear(self):
        self.root = None
    def _search(self,root,value):
        if root.key == value or root is None:
            return root
        if value > root.key:
            return self._search(self,root.right,value)
        return self._search(self,root.left,value)
    def search(self,value):
        return self._search(self.root,value)
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            return self._insert(self.root,value)
    def _insert(self,root,value):
        if value < root.key:
            if root.left is None:
                root.left = Node(value)
            else:
                return self._insert(root.left,value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                return self._insert(root.right,value)
    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self,root):
        if root:
            print(root.key,end=' ')
            self._preorder(root.left)
            self._preorder(root.right)
    def postorder(self):
        return self._postorder(self.root)
    def _postorder(self,root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.key,end=' ')
    def inorder(self):
        return self._inorder(self.root)
    def _inorder(self,root):
        if root:
            self._inorder(root.left)
            print(root.key,end=' ')
            self._inorder(root.right)
    def count(self):
        return self._count(self.root)
    def _count(self,root):
        if root is None:
            return 0
        else:
            return 1 + self._count(root.left) + self._count(root.right)
    def delete(self,value):
        return self._delete(self.root,value)
    def _delete(self, root, value):
        if root is None:
            return root

        if value < root.key:
            root.left = self._delete(root.left, value)
        elif value > root.key:
            root.right = self._delete(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._minValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return root
    def _minValueNode(self,node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr    
    def minValue(self):
        return self._minValueNode(self.root).key
    def _maxValueNode(self,node):
        curr = node
        while curr:
            curr = curr.right
        return curr
    def maxValue(self):
        return self._maxValueNode(self.root)
    def avg(self):
        pass
    def height(self):
        return self._height(self.root)
    def _height(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left),self._height(node.right))
    


if __name__ == '__main__':
    t = BinaryTree()
    arr = [12, 7, 1, 3, 2, 5, 10, 8, 6, 9]
    for i in arr:
        t.insert(i)

    t.preorder()
    print()
    t.inorder()
    print()
    t.postorder()
    