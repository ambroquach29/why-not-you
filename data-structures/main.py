from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from stack import Stack
from queue import Queue

if __name__ == '__main__':
    sll_flag = False
    dll_flag = True
    '''Test Singly Linked List Methods'''
    if sll_flag == True:
        singly = SinglyLinkedList()
        singly.add_last(1)
        singly.add_last(2)
        singly.add_last(3)
        singly.add_last(9)
        print(singly)
        singly.insert(5, 1)
        # singly.insert(4, 1)
        # singly.insert(6, 1)
        print(singly.remove_at_index(8))
        print(singly)

    '''Test Doubly Linked List Methods'''
    if dll_flag == True:
        doubly = DoublyLinkedList()
        doubly.insert_at_head("Ambro")
        doubly.insert_at_head("Betty")
        doubly.insert_at_tail("DeEnna")
        print(doubly)

        print(doubly.insert_at_position(1, "Sam"))
        doubly.traverse_forward()
        doubly.traverse_backward()
        doubly.search("Ambro")

        # print(doubly.delete_from_head())
        # print(doubly.delete_from_tail())
        print(doubly)
        print(doubly.delete_by_value("Jessie"))
        # print(doubly.delete_by_value("Ambro"))
        # print(doubly.delete_by_value("DeEnna"))
        print(doubly.delete_at_position(3))
        print(doubly.delete_at_position(1))
        print(doubly.delete_at_position(2))
        print(doubly.delete_at_position(1))
        print(doubly.delete_at_position(0))

        doubly.traverse_forward()
        doubly.traverse_backward()
        print(doubly)
