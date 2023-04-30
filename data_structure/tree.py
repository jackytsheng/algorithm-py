class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_helper(self, node, val):
        if val > node.value:
            if node.right == None:
                node.right = Node(val)
                return
            self.insert_helper(node.right, val)
        elif val < node.value:
            if node.left == None:
                node.left = Node(val)
                return
            self.insert_helper(node.left, val)

    def search_helper(self, node, val):
        if node == None:
            return False
        if node.value == val:
            return True
        if val > node.value:
            return self.search_helper(node.right, val)
        elif val < node.value:
            return self.search_helper(node.left, val)

    def print_helper(self, node, traversal):
        if node == None:
            return ""
        traversal += str(node.value) + self.print_helper(node.left,
                                                         traversal) + self.print_helper(node.right, traversal)
        return traversal

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
        pass

    def __str__(self):
        return "preorder: {}".format(self.print_helper(self.root, "-")[1::])

    def search(self, find_val):
        return self.search_helper(self.root, find_val)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""

        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return str(self.root.value) + self.preorder_print(self.root.left, "") + self.preorder_print(self.root.right, "")

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start == None:
            return False
        elif find_val == start.value:
            return True
        else:
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start == None:
            return traversal

        traversal += "-" + str(start.value) + self.preorder_print(
            start.left, traversal) + self.preorder_print(start.right, traversal)
        return traversal
