class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

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

    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next

    secondLast.next = None
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
        "3. Insert at specific position",
    ]

delete_menu = [
    "1. Delete head",
    "2. Delete tail",
    "3. Delete specific position"
]

singly_menu = [
        "1. Insertion",
        "2. Deletion",
        "3. Searching",
        "4. Update",
        "5. Exit"
    ]

for options_i in singly_menu:
    print(options_i)

try:
    while True:
        menu_choice = int(input("Choose: "))
        match(menu_choice):
            case 1:
                new = int(input("Enter value to add: "))
                for i in insert_menu:
                    print(i)
                choice = int(input("Choose: "))
                match (choice):
                    case 1:
                        node1 = insert_front(node1, new)
                        print_list(node1)
                    case 2:
                        node1 = insert_end(node1, new)
                        print_list(node1)
                    case 3:
                        pos = int(input("Position: "))
                        if pos == count:
                            node1 = insert_end(node1, new)
                            print_list(node1)
                        else:
                            node1 = insert_pos(node1, pos, new)
                            print_list(node1)
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
                pass
            case 5:
                break
except ValueError as e:
    print(f"Error: {e}")
