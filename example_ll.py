#! /usr/bin/env python
from linked_list import LinkedList

linked_list = LinkedList(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
print(linked_list.printer())
linked_list.remove(4)
print(linked_list.printer())