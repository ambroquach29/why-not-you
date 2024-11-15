from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from custom_stack import Stack
from custom_queue import Queue
from binary_tree import BinaryTree
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
            case DS.PQ:
                return priority_queue_methods()
            case DS.HT:
                return hash_table_methods()
            case DS.BT:
                return binary_tree_methods()
            case DS.BST:
                return binary_search_tree_methods()
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
        '''Test Stack Methods'''
        stack = Stack([1, 2, 3, 4])
        print(stack)

        stack.push(5)
        print(f'Top of stack: {stack.peek()}')
        print(stack)
        print(f'Popped element: {stack.pop()}')
        print(stack)

    def queue_methods():
        '''Test Queue Methods'''
        queue = Queue([9, 100, 207, 5000, 698])
        print(queue)
        queue.enqueue(179)
        queue.dequeue()
        print(queue)
    
    def priority_queue_methods(): pass
    def hash_table_methods(): pass
    def binary_tree_methods():
        binary_tree = BinaryTree()
        binary_tree.insert(1)
        binary_tree.insert(2)
        binary_tree.insert(3)
        binary_tree.insert(4)
        binary_tree.insert(5)
        binary_tree.insert(6)
        binary_tree.insert(7)
        binary_tree.insert(8)
        
        binary_tree.print()
        binary_tree.inorder_traversal()
        
        found_bfs = binary_tree.bfs(8)
        print(f'Value: {found_bfs} is found.') if found_bfs else print(f'No value is found:')
        found_dfs = binary_tree.dfs(8)
        print(f'Value: {found_dfs} is found.') if found_dfs else print(
            f'No value is found:')
        
        tree_height = binary_tree.get_height()
        print(f'Tree Height: {tree_height}')
        
        tree_size = binary_tree.get_size()
        print(f'Tree Size: {tree_size}')
        
        print(f'Tree is empty: {binary_tree.is_empty()}')
        binary_tree.level_order_traversal()
        
        tree_list = binary_tree.to_list_levelorder()
        print(f'Level Order List: {tree_list}')
        
        path = binary_tree.find_path_from_root(5)
        print(f'Path from root: {path}')
        
    def binary_search_tree_methods():
        pass
        

    switch_test_methods(DS.BT)
