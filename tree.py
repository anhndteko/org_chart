from typing import ByteString, List, Any


class Node:
    value: str
    child: List
    level: int

    def __init__(self, value: str, level=0):
        self.value = value
        self.child = []
        self.level = level

    def add_child(self, value):
        node = Node(value=value, level=self.level+1)
        self.child.append(node)

    def __str__(self):
        child = ""
        for i in (self.child):
            child += str(i.value) + " "
        child = child if child != '' else 'None'
        return "level " + str(self.level) + ", value: " + str(self.value) + ", child: " + str(child)


class Tree:
    def __init__(self):
        self.root = Node("binh.mt@teko.vn")

    def insert(self, value_child, value_parent):
        parent = self.__bfs(value_parent)
        if not parent:
            raise Exception
        parent.add_child(value_child)

    def delete(self, value):
        parent, index = self.__bfs_find_parent(value=value)
        if not parent:
            raise Exception
        node = parent.child[index]
        if len(node.child) != 0:
            raise Exception

        parent.child.remove(node)

    def __bfs(self, value):
        queue = []
        res = None
        queue.append(self.root)
        while queue:
            s = queue.pop(0)
            if s.value == value:
                res = s
                break
            for i in s.child:
                queue.append(i)

        return res

    def __bfs_find_parent(self, value):
        queue = []
        res = None
        queue.append(self.root)
        while queue:
            s = queue.pop(0)

            for i in range(len(s.child)):
                if s.child[i].value == value:
                    res = s
                    return res, i
                queue.append(s.child[i])

        return None, -1

    def __str__(self) -> str:
        result = ''
        queue = []
        queue.append(self.root)
        index = self.root.level
        while queue:
            s = queue.pop(0)
            if index != s.level:
                print()
                index += 1
            print(s.value, end=" ")
            for i in s.child:
                queue.append(i)
        return result


tree = Tree()

f = open("data.txt", "r")
for x in f:
    x = x[:-1]
    arr = x.split(" ")
    for i in range(1, len(arr)):
        tree.insert(arr[i], arr[0])

# tree.delete("anh.nd@teko.vn")

# print(tree.root)
# print(tree.root.child[0])
# print(tree.root.child[1])
# print(tree.root.child[1].child[0])
print(tree)
