class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def insert_list(self, list):
        for i in list:
            self.insert(i)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def check_for_duplicates(self, list, duplicates):
        for i in list:
            if self.contains(i):
                duplicates.append(i)
        return duplicates