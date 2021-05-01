class Node:
    def __init__(this, data):
        this.data = data
        this.next = None
        this.prev = None

class DoublyLinkedList:
    def __init__(this):
        this.head = None

    def append(this, data):
        if not this.head:
            new_node = Node(data)
            new_node.prev = None
            this.head = new_node

        else:
            new_node = Node(data)
            cur = this.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None


    def print_list(this):
        cur = this.head
        while cur:
            print(cur.data)
            cur = cur.next

    def prepend(this, data):
        if not this.head:
            new_node = Node(data)
            new_node.prev = None
            this.head = new_node
        
        else:
            new_node = Node(data)
            this.head.prev = new_node 
            new_node.next = this.head 
            this.head = new_node
            new_node.prev = None

    def add_after_node(this, key, data):
        cur = this.head
        while cur:
            if cur.next is None and cur.data == key:
                this.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(this, key, data):
        cur = this.head
        while cur:
            if cur.prev is None and cur.data == key:
                this.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next

    def delete(this, key):
        cur = this.head
        while cur:
            if cur.data == key and cur == this.head:
                if not cur.next:
                    cur = None
                    this.head = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    cur.prev = None
                    cur.next = None
                    cur = None
                    this.head = nxt
                    return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
                    
            cur = cur.next

    def delete_node(this, node):
        cur = this.head
        while cur:
            if cur == node and cur == this.head:
                if not cur.next:
                    cur = None
                    this.head = None
                    return
                else:
                    nxt = cur.next
                    nxt.prev = None
                    cur.prev = None
                    cur.next = None
                    cur = None
                    this.head = nxt
                    return
            elif cur == node:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
                    
            cur = cur.next

    def reverse(this):
        tmp = None
        cur = this.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next =  tmp
            cur = cur.prev
        if tmp:
            this.head = tmp.prev

    def remove_duplicates(this):
        cur = this.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                this.delete_node(cur)
                cur = nxt

    def pairs_with_sum(this, target):
        pairs = []
        p = this.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data+q.data == target:
                    pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs



dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)
dlist.print_list()
print("\n")
print(dlist.pairs_with_sum(5))
dlist.print_list()
            
