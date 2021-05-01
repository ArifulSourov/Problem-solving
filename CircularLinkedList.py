class Node:
    def __init__(this, data):
        this.data = data
        this.next = None

class CircularLinkedList:
    def __init__(this):
        this.head = None

    def append(this, data):
        if not this.head:
            this.head = Node(data)
            this.head.next = this.head

        else:
            new_node = Node(data)
            cur = this.head
            while cur.next != this.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = this.head

    def print_list(this):
        cur = this.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == this.head:
                break

    def prepend(this, data):
        new_node = Node(data)
        cur = this.head
        new_node.next = this.head
        if not this.head:
            new_node.next = new_node
        else:
            while cur.next != this.head:
                cur = cur.next
            cur.next = new_node
            this.head = new_node

    def remove(this, key):
        if this.head.data == key:
            cur = this.head
            while cur.next != this.head:
                cur = cur.next
            cur.next = this.head.next
            this.head = this.head.next
        else:
            cur = this.head
            prev = None
            while cur.next != this.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next


    def __len__(this):
        count = 0
        cur = this.head
        while cur:
            count += 1
            cur = cur.next
            if cur == this.head:
                break
        return count

    def split_list(this):
        size = len(this)
        if size == 0:
            return None
        if size == 1:
            return this.head

        mid = size//2
        count = 0
        cur = this.head
        prev = None
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = this.head
        split_clist = CircularLinkedList()
        while cur.next != this.head:
            split_clist.append(cur.data)
            cur = cur.next
        split_clist.append(cur.data)
        this.print_list()
        print()
        split_clist.print_list()

    def remove_node(this, node):
        if this.head == node:
            cur = this.head
            while cur.next != this.head:
                cur = cur.next
            cur.next = this.head.next
            this.head = this.head.next
        else:
            cur = this.head
            prev = None
            while cur.next != this.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(this, step):
        cur = this.head
        while len(this) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("removed node:" + str(cur.data))
            this.remove_node(cur)
            cur = cur.next
                    
        




clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)

clist.josephus_circle(2)
clist.print_list()
                
