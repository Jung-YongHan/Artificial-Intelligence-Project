class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.__position = position
        self.__parent = parent
        self.__f = g + h
        self.__g = g
        self.__h = h

    def set_position(self):
        pass
    def set_parent(self, parent):
        self.__parent = parent
    def set_f(self, f):
        self.__f = f
    def set_g(self, g):
        self.__g = g
    def set_h(self, h):
        self.__h = h

    def get_position(self):
        return self.__position
    def get_parent(self):
        return self.__parent
    def get_f(self):
        return self.__f
    def get_g(self):
        return self.__g
    def get_h(self):
        return self.__h