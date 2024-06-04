class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key == current_node.value, do nothing (BSTs typically do not have duplicate elements)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None or current_node.value == key:
            return current_node
        if key < current_node.value:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current_node, key):
        if current_node is None:
            return current_node

        if key < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, key)
        elif key > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current_node.value = self._min_value_node(current_node.right).value
            # Delete the inorder successor
            current_node.right = self._delete_recursive(current_node.right, current_node.value)

        return current_node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=' ')
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.value, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end=' ')

# Example Usage
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(2)
    bt.insert(7)
    bt.insert(12)
    bt.insert(18)

    print("Inorder traversal:")
    bt.inorder_traversal(bt.root)
    print("\nPreorder traversal:")
    bt.preorder_traversal(bt.root)
    print("\nPostorder traversal:")
    bt.postorder_traversal(bt.root)

    print("\nSearch for node with value 7:")
    node = bt.search(7)
    print("Node found:", node.value if node else "Node not found")

    print("\nHeight of the tree:", bt.height(bt.root))

    print("\nDelete node with value 10")
    bt.delete(10)
    print("Inorder traversal after deletion:")
    bt.inorder_traversal(bt.root)