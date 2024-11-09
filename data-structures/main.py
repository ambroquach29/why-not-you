from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList

if __name__ == '__main__':
    '''Test Singly Linked List'''
    linked_list = SinglyLinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)
    linked_list.add_last(9)
    print(linked_list)
    linked_list.insert(5, 1)
    # linked_list.insert(4, 1)
    # linked_list.insert(6, 1)
    print(linked_list.remove_at_index(8))
    print(linked_list)
