from tables.nodes.filenode import new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


def addOnedataonhead(node1, data):
    new_node = Node(data)
    new_node.next = node1
    return new_node

def addNodeOnLast(last_node, data):
    last_node = last_node
    new_node = Node(data)
    last_node.next = new_node
    return new_node

new_node = addOnedataonhead(node1, 00)
last_node = addNodeOnLast(node4, 50)

def linklistview(node1):
    current = node1
    count = 0
    while current:
        count += 1
        print(current.data, end=" -> ")
        current = current.next
    return count

total = linklistview(new_node)
print("\n","Total number",total)

def searchElementInLinklist(first_node, target):
    current = first_node
    while current:
        if target == current.data:
            return True
        current = current.next
    return  False

print(searchElementInLinklist(new_node, 90))

