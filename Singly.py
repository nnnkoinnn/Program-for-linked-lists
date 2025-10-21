def singly_menu():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def reverse(head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def update_list(head):
        if head.next is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        reversed_list = mid.next
        mid.next = None
        reversed_list = reverse(reversed_list)
        curr1 = head
        curr2 = reversed_list
        while curr2 is not None:
            x = curr1.data
            curr1.data = curr2.data - x
            curr2.data = x
            curr1 = curr1.next
            curr2 = curr2.next
        mid.next = reverse(reversed_list)
        return head

    def search_list(head, key):
        if head is None:
            return False
        if head.data == key:
            return True
        return search_list(head.next, key)

    def delete_front(head):
        if head is None:
            return None
        temp = head
        head = head.next
        temp = None
        return head

    def delete_end(head):
        if head is None:
            return None
        if head.next is None:
            return None
        second_last = head
        while secondLast.next.next is not None:
            secondLast = secondLast.next
        second_last.next = None
        return head

    def delete_pos(head, pos):
        temp = head
        if pos == 1:
            head = temp.next
            return head
        prev = None
        for i in range(1, pos):
            prev = temp
            temp = temp.next

        prev.next = temp.next
        return head

    def insert_front(head, x):
        new_node = Node(x)
        new_node.next = head
        return new_node

    def insert_end(head, x):
        new_node = Node(x)
        if head is None:
            return new_node
        last_node = head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        return head


    def insert_pos(head, pos, val):
        if pos < 1:
            return head
        if pos == 1:
            new_node = Node(val)
            new_node.next = head
            return new_node
        curr = head
        for i in range(1, pos - 1):
            if curr is None:
                return head
            curr = curr.next
        if curr is None:
            return head
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        return head


    def print_list(head):
        curr = head
        while curr is not None:
            print(curr.data, end=" ")
            if curr.next is not None:
                print("->", end=" ")
            curr = curr.next
        print()


    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    head = node1
    temp = head

    count = 0

    while temp is not None:
        count += 1
        temp = temp.next

    insert_menu = [
        "1. Insert at the beginning",
        "2. Insert at the end",
        "3. Insert at specific position"
        ]

    delete_menu = [
        "1. Delete head",
        "2. Delete tail",
        "3. Delete specific position"
    ]

    singly_options = [
            "1. Insertion",
            "2. Deletion",
            "3. Searching",
            "4. Reverse",
            "5. Exit"
        ]

    try:
        while True:
            print("=====SINGLY=LIST=====")
            print()
            for options_i in singly_options:
                print(options_i)
            menu_choice = int(input("Choose: "))
            match(menu_choice):
                case 1:
                    new = int(input("Enter value to add: "))
                    for i in insert_menu:
                        print(i)
                    choice = int(input("Choose: "))
                    match (choice):
                        case 1:
                            head = insert_front(head, new)
                            print_list(head)
                        case 2:
                            head = insert_end(head, new)
                            print_list(head)
                        case 3:
                            pos = int(input("Position: "))
                            if pos == count:
                                head = insert_end(head, new)
                                print_list(head)
                            else:
                                head = insert_pos(head, pos, new)
                                print_list(head)
                case 2:
                    for i in delete_menu:
                        print(i)
                    choice = int(input("Choose:"))
                    match(choice):
                        case 1:
                            node1 = delete_front(node1)
                            print_list(node1)
                        case 2:
                            node1 = delete_end(node1)
                            print_list(node1)
                        case 3:
                            pos = int(input("Position: "))
                            node1 = delete_pos(node1, pos)
                            print_list(node1)
                case 3:
                    key = int(input("Value to find: "))
                    if search_list(head, key):
                        print(f"Value {key} is in the linked list.")
                    else:
                        print(f"Value {key} is not in the linked list.")
                case 4:
                    head = update_list(head)
                    print_list(head)
                case 5:
                    break
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    singly_menu()