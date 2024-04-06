class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        if capacity < 0:
            raise ValueError

    def __str__(self):
        n = self._size
        text = "🍪" * n
        return f"{text}"

    def deposit(self, n):
        balance = self._size + n
        self._size = balance
        if balance > self.capacity:
            raise ValueError
        return balance

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        else:
            balance = self._size - n
            self._size = balance
            return balance


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, value):
        self._capacity = value


    @property
    def size(self):
        if self.size > self.capacity:
            return self.size
        else:
            raise ValueError
    @size.setter
    def size(self, value):
        self._size = value
