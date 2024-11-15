from tree_node import TreeNode
from custom_queue import Queue
from custom_stack import Stack


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def is_empty(self):
        return self.root == None

    def get_height(self):
        def helper(root):
            if root is None:
                return 0

            left_subtree = helper(root.left)
            right_subtree = helper(root.right)

            return max(left_subtree, right_subtree) + 1
        return helper(self.root)

    def get_size(self):
        def helper(root):
            if root is None:
                return 0

            left_subtree = helper(root.left)
            right_subtree = helper(root.right)

            return left_subtree + right_subtree + 1
        return helper(self.root)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        queue = Queue()
        queue.enqueue(self.root)
        new_node = TreeNode(value)

        while len(queue) != 0:
            node = queue.dequeue()
            if node.left is None:
                node.left = new_node
                return
            else:
                queue.enqueue(node.left)

            if node.right is None:
                node.right = new_node
                return
            else:
                queue.enqueue(node.right)

    def delete(self, value):
        pass

    def preorder_traversal(self, node):
        print('Preorder Traversal:')

        def helper(node):
            if node is None:
                return

            print(node.value, end=' ')
            helper(node.left)
            helper(node.right)
        helper(self.root)
        print()

    def inorder_traversal(self):
        print('Inorder Traversal:')

        def helper(node):
            if node is None:
                return

            helper(node.left)
            print(node.value, end=' ')
            helper(node.right)
        helper(self.root)
        print()

    def postorder_traversal(self, node):
        print('Postorder Traversal:')

        def helper(node):
            if node is None:
                return

            helper(node.left)
            helper(node.right)
            print(node.value, end=' ')
        helper(self.root)
        print()

    def level_order_traversal(self):
        if self.root is None:
            return

        print('Level Order Traversal:')
        queue = Queue([self.root])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.dequeue()
                print(node.value, end=' ')

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        print()

    def bfs(self, value):
        if not self.root:
            return None

        queue = Queue([self.root])
        while queue:
            node = queue.dequeue()

            if node.value == value:
                return node.value

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return None

    def dfs(self, value):
        def search(node, value):
            if not node:
                return None

            if node.value == value:
                return node.value

            left_subtree = search(node.left, value)
            if left_subtree:
                return left_subtree

            return search(node.right, value)
        return search(self.root, value)

    def find_path_from_root(self, value):
        def find(root, value):
            if not root:
                return None

            if root.value == value:
                return [root.value]

            left_path = find(root.left, value)
            if left_path is not None:
                return [root.value] + left_path

            right_path = find(root.right, value)
            if right_path is not None:
                return [root.value] + right_path

            return None
        return find(self.root, value)

    def find_lca(self, value1, value2):
        pass

    def to_list_levelorder(self):
        if self.root is None:
            return

        tree_list = []
        queue = Queue([self.root])
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.dequeue()
                tree_list.append(node.value)

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        return tree_list

    def print(self):
        if not self.root:
            return

        print('Binary Tree:')
        queue = Queue([self.root])
        while len(queue) > 0:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.dequeue()
                print(node.value, end=' ')

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            print()
        print()
