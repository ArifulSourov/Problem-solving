class Node:
    def __init__(this, data=None):
        this.data = data
        this.left = None
        this.right = None

class BST:
    def __init__(this):
        this.root = None

    def insert(this, data):
        if this.root is None:
            this.root = Node(data)
        else:
            this._insert(data, this.root)

    def _insert(this, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                this._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                this._insert(data, cur_node.right)

        else:
            print("Value is already in the tree")

    def find(this, data):
        if this.root:
            is_found = this._find(data, this.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(this, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return this._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return this._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def inorder_print_tree(this):
        if this.root:
            this._inorder_print_tree(this.root)

    def _inorder_print_tree(this, cur_node):
        if cur_node:
            this._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            this._inorder_print_tree(cur_node.right)

    def is_bst_satisfied(this):
        if this.root:
            is_satisfied = this._is_bst_satisfied(this.root, this.root.data)
            if is_satisfied is None:
                return True
            return False
        return True
    def _is_bst_satisfied(this, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return this._is_bst_satisfied(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return this._is_bst_satisfied(cur_node.right, cur_node.right.data)
            else:
                return False



bst = BST()
bst.insert(3)
bst.insert(6)
bst.insert(1)
bst.insert(5)
bst.insert(10)
print(bst.find(10))
print(bst.is_bst_satisfied())

tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
print(tree.is_bst_satisfied())
        
