class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self, val=None):
        self.root = val

    def add_node(self, node, val):
        if node is None:
            node = TreeNode(val)
            if not self.root:
                self.root = node
        else:
            if val > node.val:
                if node.right:
                    self.add_node(node.right, val)
                else:
                    node.right = TreeNode(val)
            elif val < node.val:
                if node.left:
                    self.add_node(node.left, val)
                else:
                    node.left = TreeNode(val)

    def insert(self, val):
        self.add_node(self.root, val)

    def remove_node(self, node, val):
        """ broken """
        if node == None:
            return None

        if val < node.val:
            node.left = self.remove_node(node.left, val)
        elif val > node.val:
            node.right = self.remove_node(node.right, val)
        elif node.val == val:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right

            cursor = node.right
            val = cursor.val
            while cursor.left:
                cursor = cursor.left
                val = cursor.val
            node.val = val
            node.right = self.remove_node(node.right, node.val)

        return node

    def delete(self, val):
        self.remove_node(self.root, val)

    def get_node(self, node, val):
        if node == None or node.val == val:
            return node
        elif val < node.val:
            return self.get_node(node.left, val)
        elif val > node.val:
            return self.get_node(node.right, val)

    def get(self, val):
        return self.get_node(self.root, val)

    def search(self, val):
        return self.get(self.root, val)

    def report(self, node):
        # Pre order
        if node:
            print node.val
            self.report(node.left)
            self.report(node.right)

    def traverse(self):
        self.report(self.root)

def main():
    a = BST()
    a.insert(2)
    a.insert(5)
    a.insert(1)
    a.insert(3)
    #a.traverse()
    print(a.root.val)
    print(a.get(4))
    print(a.get(2))

if __name__ == '__main__':
    main()
