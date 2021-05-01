class Node:
    def __init__(this, value):
        this.value = value
        this.left = None
        this.right = None
        
class Queue(object):
    def __init__(this):
        this.items = []

    def enqueue(this, item):
        this.items.insert(0, item)

    def dequeue(this):
        if not this.is_empty():
            return this.items.pop()

    def is_empty(this):
        return len(this.items) == 0

    def peek(this):
        if not this.is_empty():
            return this.items[-1].value

    def __len__(this):
        return this.size()

    def size(this):
        return len(this.items)
    
class Stack(object):
    def __init__(this):
        this.items = []
        
    def push(this, item):
        this.items.append(item)

    def pop(this):
        if not this.is_empty():
            return this.items.pop()
    def is_empty(this):
        return len(this.items) == 0
    
    def peek(this):
        if not this.is_empty():
            return this.items[-1].value

    def __len__(this):
        return this.size()

    def size(this):
        return len(this.items)
    
class BinaryTree:
    def __init__(this, root):
        this.root = Node(root)

    def print_tree(this, traversal_type):
        if traversal_type == "preorder":
            return this.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return this.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return this.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return this.levelorder_traversal(tree.root)
        elif traversal_type == "reverselevelorder":
            return this.reverse_levelorder_traversal(tree.root)
        else:
            print("Traversal type " + traversal_type + "is not supported")
            return False
            
    def preorder_print(this, start, traversal):
        '''root -> left -> right'''
        if start:
            traversal += (str(start.value) + "-")
            traversal = this.preorder_print(start.left, traversal)
            traversal = this.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(this, start, traversal):
        '''left -> root -> right'''
        if start:
            traversal = this.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = this.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(this, start, traversal):
        '''left -> right -> root'''
        if start:
            traversal = this.postorder_print(start.left, traversal)
            traversal = this.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_traversal(this, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_traversal(this, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal
            
    def height(this, node):
        if node is None:
            return -1
        left_height = this.height(node.left)
        right_height = this.height(node.right)
        return 1 + max(left_height, right_height)

    def size_of_tree(this, start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
                
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value)
            
        return len(traversal)

    def size_iterative(this):
        if this.root is None:
            return 0
        stack = Stack()
        stack.push(this.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size

    def size_recursive(this, node):
        if node is None:
            return 0
        return 1 + this.size_recursive(node.left) + this.size_recursive(node.right)
            
            
        



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))
print(tree.height(tree.root))
print(tree.size_of_tree(tree.root))
print(tree.size_iterative())
print(tree.size_recursive(tree.root))

            
