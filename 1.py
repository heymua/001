class Listnode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.size = 0
        self.head = Listnode(0)
    
    def insertatindex(self, index, val):
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        to_add = Listnode(val)
        t   