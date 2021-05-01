class Node:
    def __init__(this, data):
        this.data = data
        this.next = None

class LinkedList:
    def __init__(this):
        this.head = None
        
    def append(this, data):
        new_node = Node(data)
        if this.head is None:
            this.head = new_node
            return

        last_node = this.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print(this):
        cur_node = this.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(this, data):
        new_node = Node(data)
        new_node.next = this.head
        this.head = new_node

    def insert_after_node(this, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            print("ohhh no")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_iterative(this):
        count = 0
        cur_node = this.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(this, node):
        if node is None:
            return 0
        return 1 + this.len_recursive(node.next)

    def delete_node(this, data):
        cur_node = this.head
        if cur_node and cur_node.data == data:
            this.head = cur_node.next
            cur_node = None

        prev = None
        while cur_node and cur_node.data != data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_position(this, index):
        cur_node = this.head
        prev = None
        count = 1
        if index == 0:
            this.head = cur_node.next
            cur_node = None
            return
        while cur_node and count != index:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def swap_nodes(this, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        cur_1 = this.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = this.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            this.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            this.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_iteratively(this):
        prev = None
        cur_node = this.head
        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
        this.head = prev

    def reverse_recursively(this):
        def _reverse_recursively(cur_node, prev):
            if not cur_node:
                return prev
            
            nxt = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = nxt
            return _reverse_recursively(cur_node, prev)
        this.head = _reverse_recursively(cur_node=this.head, prev=None)

    def merge_sorted(this, llist):
        p = this.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_node

    def remove_duplicates(this):
        
        cur_node = this.head
        prev = None
        
        dup_values = dict()
        
        while cur_node:
            if cur_node.data in dup_values:
                prev.next = cur_node.next
                cur_node = None
            else:
                dup_values[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next

    def print_nth_from_last_1(this, n):
        total_len = this.len_iterative()
        cur_node = this.head
        while cur_node:
            if total_len == n:
                print(cur_node.data)
                return cur_node
            total_len -= 1
            cur_node = cur_node.next
        if cur_node is None:
            return
        
    def print_nth_from_last_2(this, n):
        p = this.head
        q = this.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count_occurences_iterative(this, data):
        cur_node = this.head
        count = 0
        while cur_node:
            if cur_node.data == data:
                count += 1
            cur_node = cur_node.next
        return count

    def count_occurences_recursive(this, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + this.count_occurences_recursive(node.next, data)
        else:
            return this.count_occurences_recursive(node.next, data)
            
    def move_tail_to_head(this):
        last = this.head
        second_last = None
        while last.next:
            second_last = last
            last = last.next
        last.next = this.head
        second_last.next = None
        this.head = last

    def rotate(this, k):
        p = this.head
        q = this.head
        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p =  prev
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = this.head
        this.head = p.next
        p.next = None

    def is_palindrome_1(this):
        s = ""
        p = this.head
        while p:
            s += p.data
            p = p.next

        return s == s[::-1]

    def is_palindrome_2(this):
        p = this.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = this.head
        data = []
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(this):
        p = this.head
        q = this.head
        prev = []
        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        count = 1
        while count <= i//2+1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

ll = LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("B")
ll.append("A")
#ll.append("A")
#print(ll.is_palindrome_1())
print(ll.is_palindrome_3())
#ll.print()

        
