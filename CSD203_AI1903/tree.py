'''class TreeNode:
    def __init__(self,data):
        self.root = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        self.child = child
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level
    def print_tree(self):
        print(' '*self.get_level() + '|--', end='')
        print(self.data)
        if self.children:
            for each in self.children:
                each.print_tree()
'''




class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(node):
    if node is None:
        return 
    Inorder(node.left)
    print(node.data,end=' ')
    Inorder(node.right)

def Postorder(node):
    if node:
        Postorder(node.left)
        Postorder(node.right)
        print(node.data,end=' ')
    else:
        return
def Preorder(node):
    if node:
        print(node.data)
        Preorder(node.left)
        Preorder(node.right)
    return
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print(Inorder(root))
    print(Postorder(root))
