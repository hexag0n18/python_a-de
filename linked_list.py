#! /usr/bin/env python

# LISTA ENLAZADA

# CLASE NODO
'''
  data    -> guarda el dato del nodo en la lista enlazada
  _next_  -> guarda la direccion al siguiente nodo de la lista
'''
class Node(object):
  data = 0
  _next_ = None
  def __init__(self, data, _next_ = None):
    self.data = data
    self._next_ = _next_

  def setData(self, data):
    self.data = data

  def setNext(self, node):
    self._next_ = node

  def getData(self):
    return self.data

  def getNext(self):
    return self._next_

class LinkedList(object):
  init = None
  tail = None
  aux = None
  def __init__(self, data):
    self.init = Node(data)
    self.tail = self.init

  def checkNode(self, node, data):
    if node == None:
      return False
    if data == node.getData():
      return node.getNext()
    else:
      self.aux = node
    return self.checkNode(node.getNext(), data)

  def deleteNode(self, init, data):
    node = self.checkNode(init, data)
    if self.aux != None:
      self.aux.setNext(node)
    else:
      self.init = node
    if not node:
      return False
    return True

  def indexNode(self, node, index):
    if index == 0:
      return node.getNext()
    else:
      self.aux = node
    index -= 1
    return self.indexNode(node.getNext(), index)

  def add(self, data):
    new_node = Node(data)
    self.tail.setNext(new_node)
    self.tail = new_node

  # mode -> 'first' (default), 'all', 'index'
  def remove(self, data, mode = 'first'):
    self.aux = None
    if mode == 'first':
      self.deleteNode(self.init, data)
    elif mode == 'all':
      while True:
        res = self.deleteNode(self.init, data)
        if not res:
          return
    elif mode == 'index':
      node = self.indexNode(self.init, data)
      if self.aux != None:
        self.aux.setNext(node)
      else:
        self.init = node

  def getDataNode(self, node):
    data = f"{node.getData()}"
    if node.getNext():
      data += ' -> ' + self.getDataNode(node.getNext())
    return data

  def printer(self):
    print(self.getDataNode(self.init))
