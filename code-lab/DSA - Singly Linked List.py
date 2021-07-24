class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def push_front(self, data):
        if self.length() == 0:
            self.append(data)
        else:
            new_node = Node(data)
            cur = self.head
            # 
            i = 0
            while i < 1 and cur.next != None:
                cur = cur.next
                i += 1
            new_node.next = cur
            self.head.next = new_node
            # new_node = Node(data)
            # new_node.next = self.head
            # self.head = new_node
        # pass

    def length(self):
        cur = self.head

        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next

        return total

    def get(self, idx):
        if idx >= self.length():
            print("Error! Index out of range.")
            return None
        
        current_idx = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next
            if current_idx == idx: return cur_node.data
            current_idx += 1

    def display(self):
        elements = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)

        print(elements)


def main():
    lst = LinkedList()

    # for i in range(5):
    #     data = int(input("Enter a number: "))
    #     lst.append(data)

    elements = list(map(int, input("Enter 5 numbers: ").split()))
    [lst.append(x) for x in elements]

    print(lst.length())
    lst.display()

    # elem = lst.get(1)
    # print(elem)

    lst.push_front(10)
    lst.display()
    lst.push_front(11)
    lst.display()

    lst.push_front(12)
    lst.display()

if __name__ == "__main__":
    main()
