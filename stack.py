class Stack:

    def  __init__(self):
        self.items = []

    def push(self, item):
        """
            Time complexity is O(1)
        """
        self.items.append(item)

    def pop(self):
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
            Time complexity is O(1)
        """
        return len(self.items)

    def is_empty(self):
        return self.items == []


def match_symbols(symbol_str):

    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0

    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else:
            if my_stack.is_empty():
                return False
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False

print(match_symbols('([{}])'))
print(match_symbols('(({}])'))
                

