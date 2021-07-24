class Node:
    def __init__(self, data, next1):
        self.data = data
        self.next = next1


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_at_the_beginning(self, data):
        self.insert_with_index(0, data)

    def insert_at_the_ending(self, data):
        self.insert_with_index(self.size, data)

    def insert_with_index(self, index, data):
        if index > self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        if index == 0:
            self.head = Node(data, self.head)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
        self.size += 1

    def peek_top(self):
        return self.peek_index(0)

    def peek_bottom(self):
        return self.peek_index(self.size - 1)

    def peek_index(self, index):
        if index >= self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def peek_element(self, data):
        current = self.head
        while current.data != data:
            if current.next is None:
                print("element", data, "not found")
                return False
            current = current.next
        print("element", data, "is found")
        return True

    def delete_top_element(self):
        return self.delete_with_index(0)

    def delete_bottom_element(self):
        return self.delete_with_index(self.size - 1)

    def delete_with_index(self, index):
        if index >= self.size or index < 0:
            print("check given", index, "index value and enter again")
            return False
        self.size -= 1
        if index == 0:
            temp = self.head
            self.head = self.head.next
            return temp.data
        current = self.head
        for i in range(index - 1):
            current = current.next
        temp = current.next
        current.next = current.next.next
        return temp.data

    def delete_with_value(self, data):
        current = self.head
        previous = current
        while current.data != data:
            if current.next is None:
                print("element", data, "not found")
                return False
            previous = current
            current = current.next
        temp = previous.next
        previous.next = current.next
        print("element", data, "is found and deleted")
        self.size -= 1
        return temp.data

    def print_val(self):
        current = self.head
        while current:
            print(current.data, "\b--->", end="")
            current = current.next
        print()


linked_list = Linkedlist()


def trail1():
    linked_list.insert_at_the_beginning(45)
    linked_list.insert_at_the_beginning(65)
    linked_list.insert_at_the_beginning(34)
    linked_list.insert_at_the_beginning(56)
    linked_list.insert_at_the_beginning(78)
    linked_list.insert_at_the_beginning(98)
    linked_list.insert_at_the_beginning(63)
    linked_list.insert_at_the_beginning(31)
    linked_list.print_val()


def trail2():
    linked_list.insert_at_the_beginning(78)
    linked_list.insert_at_the_ending(67778)
    linked_list.insert_at_the_ending(899)
    linked_list.insert_at_the_ending(99)
    linked_list.print_val()
    trail1()


def trail3():
    linked_list.insert_at_the_beginning(34)
    linked_list.insert_at_the_beginning(56)
    linked_list.insert_at_the_beginning(78)
    linked_list.insert_at_the_beginning(31)
    linked_list.insert_at_the_ending(12)
    linked_list.insert_at_the_ending(14)
    linked_list.insert_at_the_ending(56)
    linked_list.insert_with_index(90, 345)
    linked_list.insert_with_index(5, 23)
    print(linked_list.peek_index(2))
    print(linked_list.peek_bottom())
    print(linked_list.peek_top())
    linked_list.peek_element(16)
    linked_list.peek_element(33)
    linked_list.insert_at_the_beginning(128)
    linked_list.insert_at_the_beginning(784)
    linked_list.insert_at_the_beginning(314)
    linked_list.print_val()
    print(linked_list.delete_with_index(5))
    linked_list.print_val()
    print(linked_list.delete_top_element())
    linked_list.print_val()
    print(linked_list.delete_bottom_element())
    linked_list.print_val()
    linked_list.delete_with_value(12)
    linked_list.print_val()
    # trail2()

    # this is siva
    # signing off


if __name__ == "__main__":
    trail3()