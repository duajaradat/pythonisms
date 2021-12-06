class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection :
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):    
        self.head = Node(value, self.head)
    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node 
    def __getitem__(self, index):
        if index < 0:
            raise IndexError('Negative indexing not supported')
        for i, item in enumerate(self.head):
            if i == index:
                return item
        
    def __iter__(self):
        def  generator():
            current = self.head
            while current:
                yield current.value
                current = current.next 
        return generator()

    def __len__(self):
        return len(list(iter(self)))    

    def __str__(self):
        output = ''
        for item in self:
            output += f"[ {item} ] -> "
        output += 'None'
        return output

    