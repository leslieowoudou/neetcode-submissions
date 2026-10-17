class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        i = 0
        
        while i != index and current is not None:
            current = current.next
            i += 1

        if current is None:
            return -1

        return current.value

    def insertHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        
        # Si c'était le premier élément, tail doit aussi pointer dessus
        if self.tail is None:
            self.tail = newnode

    def insertTail(self, val: int) -> None:
        newnode = Node(val)
        
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            # Sécurité anti-bug : si tail est devenu None par erreur, on le recalcule
            if self.tail is None:
                current = self.head
                while current.next is not None:
                    current = current.next
                self.tail = current
                
            self.tail.next = newnode
            self.tail = newnode

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
            
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
            
        current = self.head
        i = 0
        
        while i < index - 1 and current is not None:
            current = current.next
            i += 1
            
        if current is None or current.next is None:
            return False
            
        if current.next == self.tail:
            self.tail = current
            
        current.next = current.next.next
        return True

    def getValues(self) -> list[int]:
        my_list = []
        current = self.head
        
        while current is not None:
            my_list.append(current.value)
            current = current.next
            
        return my_list