#!/bin/python3

class Node(object):
  data = 0
  _next_ = 'null'
  def __init__(self, data, _next_ = 'null'):
    self.data = data
    self._next_ = _next_

  def setNext(self, node):
    self._next_ = node

  def getData(self):
    return self.data

  def getNext(self):
    return self._next_

class LinkedList(object):
  init = 'null'
  tail = 'null'
  def __init__(self, data):
    self.init = Node(data)
    self.tail = self.init

  def createNode(self, data):
    new_node = Node(data)
    self.tail.setNext(new_node)
    self.tail = new_node

  def getDataNode(self, node):
    data = f"{node.getData()}"
    if node.getNext() != 'null':
      data += ' -> ' + self.getDataNode(node.getNext())
    return data

  def printer(self):
    print(self.getDataNode(self.init))
    # print(self.init.getData())


linked_list = LinkedList(1)
linked_list.createNode(2)
linked_list.createNode(3)
linked_list.createNode(4)
linked_list.createNode(5)
print(linked_list.printer())