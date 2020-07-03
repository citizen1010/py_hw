"""

BST: insert, delete, search, number of elements less than a given number
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, insert_value):  # добавление
        if insert_value < self.value:
            if self.left is None:
                self.left = Node(insert_value)
            else:
                self.left.insert(insert_value)
        else:
            if self.right is None:
                self.right = Node(insert_value)
            else:
                self.right.insert(insert_value)

    def min_value_node_delete(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, delete_value):  # удаление
        if delete_value < self.value:
            self.left = self.left.delete(delete_value)
        elif delete_value > self.value:
            self.right = self.right.delete(delete_value)
        else:
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp
            temp = self.min_value_node_delete(self.right)
            self.value = temp.value
            self.right = self.right.delete(temp.value)
        return self

    def search(self, search_value):  # поиск
        if search_value == self.value:
            return True
        elif search_value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(search_value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(search_value)

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    def numbers_min_than(self, root, num):  # кол-во элементов в дереве меньше заданного
        array = self.inorder_traversal(root)
        result = 0
        for x in array:
            if num > x:
                result += 1
        print(result)


def main():
    node = Node(50)
    node.insert(30)
    node.insert(20)
    node.insert(40)
    node.insert(70)
    node.insert(60)
    node.insert(80)

    print("Inorder: ---------")
    print(node.inorder_traversal(node))
    print("Number of elements less than a given number:")
    node.numbers_min_than(node, 60)
    print("")
    print("Results of search:")
    print(node.search(10))
    print(node.search(90))
    print(node.search(70))
    print("")
    node.delete(20)
    node.delete(30)
    node.delete(50)
    print("Inorder after delete: ")
    print(node.inorder_traversal(node))
    print("Number of elements less than a given number:")
    node.numbers_min_than(node, 60)


if __name__ == "__main__":
    main()
