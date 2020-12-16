class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
            Time complexity is O(n)
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
            Time complexity is O(1)
        """
        self.items.append(item)

    def remove_front(self):
        """
            Time complexity is O(n)
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """
            Time complexity is O(1)
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """
            Time complexity is O(1)
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """
            Time complexity is O(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
            Time complexity is O(1)
        """
        return len(self.items)
        
    def is_empty(self):
        """
            Time complexity is O(1)
        """
        return self.items == []

def check_palindrome(input_str):

    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >= 2:
        front_item = my_d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False
    
    return True

print(check_palindrome('racecar'))
print(check_palindrome('oranges'))