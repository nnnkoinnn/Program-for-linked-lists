class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


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

try:
    new = int(input("Enter value to add: "))

    insert_menu = [
        "1. Insert at the beginning",
        "2. Insert at the end",
        "3. Insert at specific position",
    ]

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
except TypeError as e:
    print(f"{e}")
