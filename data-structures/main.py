from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from stack import Stack
from queue import Queue
from enum import Enum


class DS(Enum):
    SLL = 'singly linked list'
    DLL = 'doubly linked list'
    STACK = 'stack'
    QUEUE = 'queue'
    PQ = 'priority queue'
    HT = 'hash table'
    BT = 'binary tree'
    BST = 'binary search tree'
    TRIE = 'trie'
    MIN_H = 'min heap'
    MAX_H = 'max heap'
    GRAPH = 'graph'


if __name__ == '__main__':
    def switch_test_methods(choice):
        match choice:
            case DS.SLL:
                return singly_linked_list_methods()
            case DS.DLL:
                return doubly_linked_list_methods()
            case DS.STACK:
                return stack_methods()
            case DS.QUEUE:
                return queue_methods()
            case _:
                return 'No data structure selected.'

    def singly_linked_list_methods():
        '''Test Singly Linked List Methods'''
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

    def doubly_linked_list_methods():
        '''Test Doubly Linked List Methods'''
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

    def stack_methods():
        stack = Stack([1, 2, 3, 4])
        print(stack)

        stack.push(5)
        print(f'Top of stack: {stack.peek()}')
        print(stack)
        print(f'Popped element: {stack.pop()}')
        print(stack)

    def queue_methods(): pass

    switch_test_methods(DS.STACK)
