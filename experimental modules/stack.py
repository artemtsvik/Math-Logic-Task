class Stack:

    __slots__ = ('element',)
    
    def __init__(self, *args):
        self.element = None
        for x in args:
            self.push(x)

    def push(self, data):
        self.element = (data, self.element)

    def is_empty(self):
        return self.element is None

    def pop(self):
        if self.is_empty():
            raise IndexError

        data = self.element[0]
        self.element = self.element[1]
        return data

    def item(self):
        return self.element[0]

    def clear(self):
        self.element = None

    def __iter__(self):
        while self.element is not None:
            yield self.pop()

    def __repr__(self):
        if self.is_empty():
            return 'Stack(data=None)'
        return 'Stack(data=' + str(self.element[0]) + ')'

    def __bool__(self):
        return not self.is_empty()

