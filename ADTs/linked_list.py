class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def insertFirst(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insertAtEnd(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp

    def insertAtPosition(self, data, position):
        count = 1
        temp = Node(data)
        curr = self.head
        while count < position - 1 and curr != None:
            curr = curr.next
            count += 1
        temp.next = curr.next
        curr.next = temp
    
    def deleteNode(self, key):

        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def length(self):
        curr = self.head
        n = 0
        while curr is not None:
            n += 1
            curr = curr.next
        return n
    
    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                return curr.data
                curr = curr.next 

    def connect(self, linked_list):
        curr = self.head
        while curr is not None:


first_node = Node("a")
second_node = Node("b")
third_node = Node("c")
my_list = linkedList()
my_list.head = first_node
first_node.next = second_node
second_node.next = third_node
fourth_node = Node("x")
fifth_node = Node("y")
sixth_node = Node("z")
my_list2 = linkedList()
my_list2.head = fourth_node
fourth_node.next = fifth_node
fifth_node.next = sixth_node
my_list.traverse()
print("")
my_list.insertFirst("d")
my_list.traverse()
print("")
my_list.insertAtEnd("3")
my_list.traverse()
print("")
my_list.insertAtPosition("9", 3)
my_list.traverse()
print("")
my_list.deleteNode("9")
my_list.traverse()
print("")
print(my_list.length())
print("")
print(my_list.search("d"))
print("")
my_list.connect(my_list2)
