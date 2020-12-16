class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
            Time complexity is O(n)
        """
        self.items.insert(0, item)

    def dequere(self):
        """
            Time complexity is O(1)
        """
        if self.items:
            return self.items.pop()
        else:
            None

    def peek(self):
        """
            Time complexity is O(1)
        """
        if self.items:
            return self.items[-1]
        else:
            None

    def size(self):
        """
            Time complexity O(1)
        """
        return len(self.items)

    def is_empty(self):
        """
            Time complexity O(1)
        """
        return self.items == []