class Node:
    def __init__(self, data, next_node = None):
        self.__data = data
        self.__next_node = next_node

   # @data.setter
    def data(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if value is not int:
            raise TypeError("data must be integer")
        self.__data = value


    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, value):
        if value is not None or type(Node):
            raise TypeError("next_node must be Node object")
        self.__next = value

class SinglyLinkedList:
    """
    docstring
    """
    def __init__(self):
        self.__head = None
    
    def __repr__(self):
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "_>".join(nodes)
    
l = SinglyLinkedList()
print(l)